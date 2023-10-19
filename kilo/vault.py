import logging
from web3 import Web3
import config
import usdt
import time

# pip install web3==5.31.3

web3 = Web3(Web3.HTTPProvider(config.rpc))

with open('../abi/VaultStakeReward.abi', 'r') as f:
    abi = f.read()

vault_contract = web3.eth.contract(address=config.vault_address, abi=abi)


def deposit(amount, user):
    try:
        # Automatically authorize USDT limit.
        usdt.approve_usdt_allowance(config.market_contract, 100000)
        # Get transaction count
        nonce = web3.eth.get_transaction_count(config.wallet)
        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': web3.toWei(int(config.gas_price), 'gwei'),
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = vault_contract.functions.deposit(amount, user).buildTransaction(tx)

        # Sign transaction data
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("deposit tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'deposit error: {e}')
        logging.exception(e)
        raise e


def redeem(shares, receiver, owner):
    try:
        # Get transaction count
        nonce = web3.eth.get_transaction_count(config.wallet)

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': web3.toWei(int(config.gas_price), 'gwei'),
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = vault_contract.functions.redeem(shares, receiver, owner).buildTransaction(tx)

        # Sign transaction data
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("redeem tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'redeem error: {e}')
        logging.exception(e)
        raise e


def get_share(account):
    share = vault_contract.functions.getShare(account).call()
    return share


if __name__ == '__main__':
    # Recharge funds into the vault to earn profits.
    deposit(int(2000 * config.precision), config.wallet)
    time.sleep(8)
    # Obtain the current shares of the vault that you hold.
    share = get_share(config.wallet)
    print("share =", share)
    time.sleep(8)
    # Withdraw from the vault and redeem your USDT. The redeem operation requires a period of time to pass. If the error "Vault: not in period" is thrown, you need to wait for the time period to expire before redeeming.
    redeem(int(share / 1e18 * 1e8), config.wallet, config.wallet)
