import logging
from web3 import Web3
import time
import usdt_kiloex
from config_kiloex import BASE,BASE12,kiloconfigs,BNBTEST

# pip install web3

vaultV2 = True
with open('./abi/VaultStakeReward.abi', 'r') as f:
    abi = f.read()

with open('./abi/Usdt.abi', 'r') as f:
    usdt_abi = f.read()


def deposit(config, amount, user):
    try:
        # Automatically authorize USDT limit.
        usdt_kiloex.approve_usdt_allowance(config, config.market_contract, 100000)
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        vault_contract_w3 = w3.eth.contract(address=config.vault_address, abi=abi)
        contract = w3.eth.contract(address=config.usdt_contract, abi=usdt_abi)
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas_price = w3.eth.gas_price
        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': gas_price,
            'chainId': int(config.chain_id)
        }

        base_decimals = BASE
        if vaultV2:
            base_decimals = 10 ** contract.functions.decimals().call()
        # Build transaction data
        txn = vault_contract_w3.functions.deposit(int(amount * base_decimals), user).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("deposit tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'deposit error: {e}')
        logging.exception(e)
        raise e


def redeem(config, shares, receiver, owner):
    try:
        w3 = Web3(Web3.HTTPProvider(config.rpc))
        vault_contract_w3 = w3.eth.contract(address=config.vault_address, abi=abi)
        # Get transaction count
        nonce = w3.eth.get_transaction_count(config.wallet)
        gas_price = w3.eth.gas_price

        # Build transaction object
        tx = {
            'from': config.wallet,
            'nonce': nonce,
            'gas': config.gas,
            'gasPrice': gas_price,
            'chainId': int(config.chain_id)
        }

        # Build transaction data
        txn = vault_contract_w3.functions.redeem(shares, receiver, owner).build_transaction(tx)

        # Sign transaction data
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=config.private_key)

        # Send signed transaction data and get transaction hash
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash_str = tx_hash.hex()
        print("redeem tx_hash =", tx_hash_str)

        return tx_hash
    except Exception as e:
        logging.error(f'redeem error: {e}')
        logging.exception(e)
        raise e


def get_share(config, account):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    vault_contract_w3 = w3.eth.contract(address=config.vault_address, abi=abi)
    share = vault_contract_w3.functions.getShare(account).call()
    return share


if __name__ == '__main__':
    config = kiloconfigs[BNBTEST]
    # Recharge funds into the vault to earn profits.
    deposit(config, 1, config.wallet)
    time.sleep(8)
    # Obtain the current shares of the vault that you hold.
    #share = get_share(config, config.wallet)
    #print("share =", share)
    #time.sleep(8)
    # Withdraw from the vault and redeem your USDT. The redeem operation requires a period of time to pass. If the error "Vault: not in period" is thrown, you need to wait for the time period to expire before redeeming.
    #redeem(config, int(share / 1e18 * 1e8), config.wallet, config.wallet)
