import logging
from web3 import Web3
from config_kiloex import BASE,BASE12,kiloconfigs,BNBTEST
import market_trade_kiloex

import time
import usdt_kiloex
import api_kiloex

with open('./abi/MarketOrderWithTriggerOrder.abi', 'r') as f:
    abi = f.read()

def open_market_tirgger_increase_position(config, product_id, margin, leverage, is_long, acceptable_price, referral_code, stop_loss_price, take_profit_price):
    # Automatically authorize USDT limit.
    usdt_kiloex.approve_usdt_allowance(config, config.market_trigger_contract, margin)

    try:
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas = config.gas * 2
        gas_price = w3.eth.gas_price
        execution_fee = config.execution_fee * 3

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
        print(int(stop_loss_price * BASE))
        print(int(take_profit_price * BASE))
        trade_contract_w3 = w3.eth.contract(address=config.market_trigger_contract, abi=abi)
        txn = trade_contract_w3.functions.createIncreasePositionWithCloseTriggerOrders(product_id, int(margin * BASE), int(leverage * BASE), is_long, int(acceptable_price * BASE),
                                                                 config.execution_fee, referral_code, int(stop_loss_price * BASE), int(take_profit_price * BASE)).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("create_market_tirgger_increase_position tx_hash =", tx_hash_str, "gas_price=", gas_price, "execution_fee=", execution_fee)

        return tx_hash
    except Exception as e:
        logging.error(f'create_market_tirgger_increase_position error: {e}')
        logging.exception(e)
        raise e

if __name__ == '__main__':
    amount = 20  # margin = 20USDT
    leverage = 2  # leverage = 2x

    config = kiloconfigs[BNBTEST]
    product_id = 1
    market_price = api_kiloex.index_price(product_id)

    open_market_tirgger_increase_position(config, product_id, amount, leverage, True, market_price * 1.001, bytearray(32), market_price * 0.75, market_price * 1.5)
    time.sleep(8)

    open_market_tirgger_increase_position(config, product_id, amount, leverage, False, market_price * 0.999, bytearray(32), market_price * 1.25, market_price * 0.5)
    time.sleep(8)

    market_trade_kiloex.open_market_decrease_position(config, product_id, amount, True, market_price * 0.999)
    time.sleep(8)

    market_trade_kiloex.open_market_decrease_position(config, product_id, amount, False, market_price * 1.001)
