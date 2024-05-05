import logging
from web3 import Web3
import config
import time
import usdt
import asyncio
from pythclient.pythaccounts import PythPriceAccount, PythPriceStatus
from pythclient.solana import SolanaClient, SolanaPublicKey, PYTHNET_HTTP_ENDPOINT, PYTHNET_WS_ENDPOINT

# pip install web3

w3 = Web3(Web3.HTTPProvider(config.rpc))

with open('../abi/PositionRouter.abi', 'r') as f:
    abi = f.read()

with open('../abi/KiloPerpView.abi', 'r') as f:
    view_abi = f.read()

trade_contract_w3 = w3.eth.contract(address=config.market_contract, abi=abi)
view_contract_w3 = w3.eth.contract(address=config.view_address, abi=view_abi)


def open_market_increase_position(product_id, margin, leverage, is_long, acceptable_price, execution_fee,
                                  referral_code):
    # Automatically authorize USDT limit.
    usdt.approve_usdt_allowance(config.market_contract, 100000)
    print(product_id, margin, leverage, is_long, acceptable_price, execution_fee, referral_code)
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
    - execution_fee (int): Execution fee
    - referral_code (str): Referral code

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': w3.to_wei(int(config.gas_price), 'gwei'),
            'value': int(config.execution_fee),
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = trade_contract_w3.functions.createIncreasePosition(product_id, margin, leverage, is_long, acceptable_price,
                                                              execution_fee, referral_code).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("create_market_increase_position tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'create_market_increase_position error: {e}')
        logging.exception(e)
        raise e


def open_market_decrease_position(product_id, margin, is_long, acceptable_price, execution_fee):
    """
    Open a market decrease position.

    Args:
    - product_id (str): Product ID
    - margin (int): Margin amount
    - is_long (bool): Whether to open a long position (True for yes, False for no)
    - acceptable_price (int): Acceptable price (if long position, will trigger when market price is lower than acceptable price;
                              if short position, will trigger when market price is higher than acceptable price;
                              actual execution price will be based on fast oracle price)
    - execution_fee (int): Execution fee

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': w3.to_wei(int(config.gas_price), 'gwei'),
            'value': int(config.execution_fee),
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = trade_contract_w3.functions.createDecreasePosition(product_id, margin, is_long, acceptable_price,
                                                              execution_fee).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("open_market_decrease_position tx_hash =", tx_hash_str)

        return tx_hash_str
    except Exception as e:
        logging.error(f'open_market_decrease_position error: {e}')
        logging.exception(e)
        raise e


class Position:
    def __init__(self, productId=0, leverage=0, price=0, oraclePrice=0, margin=0, account='', lastIncreasedTime=0,
                 isTrue=False, funding=0, borrowing=0):
        self.productId = productId
        self.leverage = leverage / config.precision
        self.price = price / config.precision
        self.oraclePrice = oraclePrice / config.precision
        self.margin = margin / config.precision
        self.account = account
        self.lastIncreasedTime = lastIncreasedTime
        self.isTrue = isTrue
        self.funding = funding / 1e12
        self.borrowing = borrowing / 1e12


def get_positions(account, ids):
    positions_raw = view_contract_w3.functions.getPositions(account, ids).call()
    positions = []
    for position_raw in positions_raw:
        position = Position(*position_raw)
        if position.margin > 0:
            positions.append(position)

    return positions


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


def init_position():
    return Position()


if __name__ == '__main__':
    amount = 20  # margin = 20USDT
    leverage = 2  # leverage = 2x
    ids = [1, 2, 3]

    market_price = asyncio.run(get_price())
    print(market_price)

    positions = get_positions(config.wallet, ids)
    for position in positions:
        print(position.__dict__)

    print(int(amount * config.precision))

    print(Position().__dict__)
    # Long at market price. When going long, the execution price must be lower than the acceptable_price to be executed.
    open_market_increase_position(int(config.eth_product_id), int(amount * config.precision),
                                  int(leverage * config.precision), True,
                                  int((market_price * 0.002 + market_price) * config.precision),
                                  int(config.execution_fee),
                                  bytearray(32))

    time.sleep(8)
    # Short at market price.When going short, the execution price must be higher than the acceptable_price to be executed.
    open_market_increase_position(int(config.eth_product_id), int(amount * config.precision),
                                  int(leverage * config.precision), False,
                                  int((market_price - (market_price * 0.002)) * config.precision),
                                  int(config.execution_fee),
                                  bytearray(32))

    time.sleep(8)
    # Close long position at market price.When closing a long position, the execution price must be higher than the acceptable_price to be executed.
    open_market_decrease_position(int(config.eth_product_id), int(amount * config.precision), True,
                                  int((market_price - (market_price * 0.002)) * config.precision),
                                  int(config.execution_fee))

    time.sleep(8)
    # Close short position at market price.When closing a short position, the execution price must be lower than the acceptable_price to be executed.
    open_market_decrease_position(int(config.eth_product_id), int(amount * config.precision), False,
                                  int((market_price * 0.002 + market_price) * config.precision),
                                  int(config.execution_fee))
