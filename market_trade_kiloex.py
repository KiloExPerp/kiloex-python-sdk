import logging
from web3 import Web3
from config_kiloex import BASE,BASE12,kiloconfigs,BNBTEST

import time
import usdt_kiloex
import api_kiloex
import asyncio
from pythclient.pythaccounts import PythPriceAccount, PythPriceStatus
from pythclient.solana import SolanaClient, SolanaPublicKey, PYTHNET_HTTP_ENDPOINT, PYTHNET_WS_ENDPOINT

# pip install web3

with open('./abi/PositionRouter.abi', 'r') as f:
    abi = f.read()

def open_market_increase_position(config, product_id, margin, leverage, is_long, acceptable_price, referral_code):
    # Automatically authorize USDT limit.
    usdt_kiloex.approve_usdt_allowance(config, config.market_contract, margin)

    """
    Open a market increase position.

    Args:
    - product_id (str): Product ID
    - margin (int): Margin amount
    - leverage (int): Leverage multiplier
    - is_long (bool): Whether to open a long position (True for yes, False for no)
    - acceptable_price (int): Acceptable price (if long position, will trigger when market price is lower than acceptable price;
                              if short position, will trigger when market price is higher than acceptable price;
                              actual execution price will be based on fast oracle price)
    - referral_code (str): Referral code

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas_price = w3.eth.gas_price

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': gas_price,
            'value': config.execution_fee,
            'chainId': config.chain_id
        }

        # Build transaction data
        trade_contract_w3 = w3.eth.contract(address=config.market_contract, abi=abi)
        txn = trade_contract_w3.functions.createIncreasePosition(product_id, int(margin * BASE), int(leverage * BASE), is_long, int(acceptable_price * BASE),
                                                                 config.execution_fee, referral_code).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("create_market_increase_position tx_hash =", tx_hash_str, "gas_price=", gas_price, "execution_fee=", config.execution_fee)

        return tx_hash
    except Exception as e:
        logging.error(f'create_market_increase_position error: {e}')
        logging.exception(e)
        raise e


def open_market_decrease_position(config, product_id, margin, is_long, acceptable_price):
    """
    Open a market decrease position.

    Args:
    - product_id (str): Product ID
    - margin (int): Margin amount
    - is_long (bool): Whether to open a long position (True for yes, False for no)
    - acceptable_price (int): Acceptable price (if long position, will trigger when market price is lower than acceptable price;
                              if short position, will trigger when market price is higher than acceptable price;
                              actual execution price will be based on fast oracle price)

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas_price = w3.eth.gas_price

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': gas_price,
            'value': config.execution_fee,
            'chainId': config.chain_id
        }

        # Build transaction data
        trade_contract_w3 = w3.eth.contract(address=config.market_contract, abi=abi)
        txn = trade_contract_w3.functions.createDecreasePosition(product_id, int(margin * BASE), is_long, int(acceptable_price * BASE),
                                                                 config.execution_fee).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("open_market_decrease_position tx_hash =", tx_hash_str, "gas_price=", gas_price, "execution_fee=", config.execution_fee)

        return tx_hash_str
    except Exception as e:
        logging.error(f'open_market_decrease_position error: {e}')
        logging.exception(e)
        raise e


async def get_price():
    account_key = SolanaPublicKey("JBu1AL4obBcCMqKBBxhpWCNUt136ijcuMZLFvTP7iWdB")
    solana_client = SolanaClient(endpoint=PYTHNET_HTTP_ENDPOINT, ws_endpoint=PYTHNET_WS_ENDPOINT)
    price: PythPriceAccount = PythPriceAccount(account_key, solana_client)
    await price.update()
    price_status = price.aggregate_price_status
    if price_status == PythPriceStatus.TRADING:
        # Sample output: "ETH/USD is 1836.9580823200001 ± 1.13014117"
        print("ETH/USD is", price.aggregate_price, "±", price.aggregate_price_confidence_interval)
        return price.aggregate_price
    else:
        print("Price is not valid now. Status is", price_status)
    await solana_client.close()

if __name__ == '__main__':
    amount = 20  # margin = 20USDT
    leverage = 2  # leverage = 2x
    ids = [1, 2, 31]

    config = kiloconfigs[BNBTEST]
    product_id = 1

    market_price = api_kiloex.index_price(product_id) #asyncio.run(get_price())
    print(market_price)

    # Long at market price. When going long, the execution price must be lower than the acceptable_price to be executed.
    open_market_increase_position(config, product_id, amount, leverage, True, market_price * 1.001, bytearray(32))

    time.sleep(8)
    # Short at market price.When going short, the execution price must be higher than the acceptable_price to be executed.
    open_market_increase_position(config, product_id, amount, leverage, False, market_price * 0.999, bytearray(32))

    time.sleep(8)
    # Close long position at market price.When closing a long position, the execution price must be higher than the acceptable_price to be executed.
    open_market_decrease_position(config, product_id, amount, True, market_price * 0.999)

    time.sleep(8)
    # Close short position at market price.When closing a short position, the execution price must be lower than the acceptable_price to be executed.
    open_market_decrease_position(config, product_id, amount, False, market_price * 1.001)
