import logging
from web3 import Web3
import time

from config_kiloex import BASE,BASE12,kiloconfigs,BNBTEST

# pip install web3

with open('./abi/OrderBook.abi', 'r') as f:
    abi = f.read()

def open_limit_increase_order(config, product_id, margin, leverage, is_long, trigger_price, trigger_above_threshold,
                              referral_code):
    """
    Open a limit increase order.

    Args:
    - product_id (str): Product ID
    - margin (int): Margin amount
    - leverage (int): Leverage multiplier
    - is_long (bool): Whether to open a long order (True for yes, False for no)
    - trigger_price (int): trigger price
    - trigger_above_threshold (bool): False, triggered by breaking below the trigger price & True, triggered by breaking above the trigger price
    - referral_code (str): Referral code

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        limit_contract_w3 = w3.eth.contract(address=config.order_book_contract, abi=abi)

        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas = config.gas
        gas_price = w3.eth.gas_price
        execution_fee = config.execution_fee

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': gas,
            'gasPrice': gas_price,
            'value': execution_fee,
            'chainId': config.chain_id
        }

        # Build transaction data
        txn = limit_contract_w3.functions.createIncreaseOrder(product_id, int(margin * BASE), int(leverage * BASE), is_long, int(trigger_price * BASE),
                                                           trigger_above_threshold, config.execution_fee, referral_code).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("open_limit_increase_order tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'open_limit_increase_order error: {e}')
        logging.exception(e)
        raise e


def open_limit_decrease_order(config, product_id, size, is_long, trigger_price, trigger_above_threshold):
    """
    Open a limit decrease order.

    Args:
    - product_id (str): Product ID
    - size (int):
    - is_long (bool): Whether to close a long position (True for yes, False for no)
    - trigger_price (int): trigger price
    - trigger_above_threshold (bool): False, triggered by breaking below the trigger price & True, triggered by breaking above the trigger price

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        limit_contract_w3 = w3.eth.contract(address=config.order_book_contract, abi=abi)

        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas = config.gas
        gas_price = w3.eth.gas_price
        execution_fee = config.execution_fee

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': gas,
            'gasPrice': gas_price,
            'value': execution_fee,
            'chainId': config.chain_id
        }

        # Build transaction data
        txn = limit_contract_w3.functions.createDecreaseOrder(product_id, int(size * BASE), is_long, int(trigger_price * BASE),
                                                           trigger_above_threshold, config.execution_fee).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("open_limit_decrease_order tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'open_limit_decrease_order error: {e}')
        logging.exception(e)
        raise e


if __name__ == '__main__':
    amount = 20  # margin = 20USDT
    leverage = 2  # leverage = 2x
    ids = [1, 2, 31]

    config = kiloconfigs[BNBTEST]
    product_id = 1

    # Open a limit increase order, place a limit buy order if it drops below $3700
    open_limit_increase_order(config, product_id, amount, int(leverage), True, int(3700), False, bytearray(32))
    time.sleep(8)
    # Open a limit increase order, place a limit sell order if it breaks above $4000
    open_limit_increase_order(config, product_id, amount, int(leverage), False, int(4000), True, bytearray(32))

    time.sleep(8)
    # Stop-loss for long positions
    open_limit_decrease_order(config, product_id, int(4000), True, int(3880), False)
    time.sleep(8)
    # Take-profit for long positions
    open_limit_decrease_order(config, product_id, int(4000), True, int(4000), True)

    time.sleep(8)
    # Stop-loss for short positions
    open_limit_decrease_order(config, product_id, int(4000), False, int(4000), True)
    time.sleep(8)
    # Take-profit for short positions
    open_limit_decrease_order(config, product_id, int(4000), False, int(3500), False)
