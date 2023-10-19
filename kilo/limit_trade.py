import logging
from web3 import Web3
import config
import time

# pip install web3==5.31.3

web3 = Web3(Web3.HTTPProvider(config.rpc))

with open('../abi/OrderBook.abi', 'r') as f:
    abi = f.read()

limit_contract = web3.eth.contract(address=config.order_book_contract, abi=abi)


def open_limit_increase_order(product_id, margin, leverage, is_long, trigger_price, trigger_above_threshold,
                              execution_fee,
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
    - execution_fee (int): Execution fee
    - referral_code (str): Referral code

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        # Get transaction count
        nonce = web3.eth.get_transaction_count(config.wallet)

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': web3.toWei(int(config.gas_price), 'gwei'),
            'value': int(config.execution_fee),
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = limit_contract.functions.createIncreaseOrder(product_id, margin, leverage, is_long, trigger_price,
                                                           trigger_above_threshold,
                                                           execution_fee, referral_code).buildTransaction(tx)

        # Sign transaction data
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("open_limit_increase_order tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'open_limit_increase_order error: {e}')
        logging.exception(e)
        raise e


def open_limit_decrease_order(product_id, size, is_long, trigger_price, trigger_above_threshold, execution_fee):
    """
    Open a limit decrease order.

    Args:
    - product_id (str): Product ID
    - size (int):
    - is_long (bool): Whether to close a long position (True for yes, False for no)
    - trigger_price (int): trigger price
    - trigger_above_threshold (bool): False, triggered by breaking below the trigger price & True, triggered by breaking above the trigger price
    - execution_fee (int): Execution fee

    Returns:
    - tx_hash (str): Transaction hash

    Raises:
    - Exception: If an error occurs.
    """
    try:
        # Get transaction count
        nonce = web3.eth.get_transaction_count(config.wallet)

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': web3.toWei(int(config.gas_price), 'gwei'),
            'value': int(config.execution_fee),
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = limit_contract.functions.createDecreaseOrder(product_id, size, is_long, trigger_price,
                                                           trigger_above_threshold, execution_fee).buildTransaction(tx)

        # Sign transaction data
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("open_limit_decrease_order tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'open_limit_decrease_order error: {e}')
        logging.exception(e)
        raise e


if __name__ == '__main__':
    amount = 200  # margin = 200USDT
    leverage = 10  # leverage = 10x

    # Open a limit increase order, place a limit buy order if it drops below $1700
    open_limit_increase_order(config.eth_product_id, amount * config.precision,
                              int(leverage * config.precision), True, int(1700 * config.precision), False,
                              int(config.execution_fee), bytearray(32))
    time.sleep(8)
    # Open a limit increase order, place a limit sell order if it breaks above $2000
    open_limit_increase_order(config.eth_product_id, amount * config.precision,
                              int(leverage * config.precision), False, int(2000 * config.precision), True,
                              int(config.execution_fee), bytearray(32))

    time.sleep(8)
    # Stop-loss for long positions
    open_limit_decrease_order(config.eth_product_id, int(2000 * config.precision), True, int(1880 * config.precision), False,
                              int(config.execution_fee))
    time.sleep(8)
    # Take-profit for long positions
    open_limit_decrease_order(config.eth_product_id, int(2000 * config.precision), True, int(2000 * config.precision), True,
                              int(config.execution_fee))

    time.sleep(8)
    # Stop-loss for short positions
    open_limit_decrease_order(config.eth_product_id, int(2000 * config.precision), False, int(2000 * config.precision), True,
                              int(config.execution_fee))
    time.sleep(8)
    # Take-profit for short positions
    open_limit_decrease_order(config.eth_product_id, int(2000 * config.precision), False, int(1500 * config.precision), False,
                              int(config.execution_fee))
