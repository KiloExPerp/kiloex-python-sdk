from web3 import Web3
from config_kiloex import MARGIN_MIN,BNBTEST,kiloconfigs

with open('./abi/Usdt.abi', 'r') as f:
    usdt_abi = f.read()

# Automatically authorize USDT limit with customizable value configuration.
def approve_usdt_allowance(config, to_address, amount):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    account = w3.eth.account.from_key(config.private_key)
    contract = w3.eth.contract(address=config.usdt_contract, abi=usdt_abi)
    allowance = contract.functions.allowance(config.wallet, to_address).call()
    base_decimals = 10 ** contract.functions.decimals().call()
    allowance = allowance / base_decimals
    # If the limit is below amount + 50000 USDT, authorization is required.
    amount = amount + 50000
    if allowance < amount:
        print(config.chain, 'Allowance is insufficient, approving... allowance:', allowance)
        gas_price = w3.eth.gas_price
        data = contract.functions.approve(w3.to_checksum_address(to_address), int(amount * base_decimals)).build_transaction({
            'from': config.wallet,
            'nonce': w3.eth.get_transaction_count(config.wallet),
            'gas': config.gas,
            'gasPrice': gas_price
        })

        signed_txn = account.sign_transaction(data)
        try:
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt['status'] == 1:
                return True
            else:
                return False
        except Exception as e:
            print(config.chain, 'An error occurred:', e)
        return False
    else:
        print(config.chain, 'Allowance is already sufficient. allowance:', allowance)
        return True


def get_balance(config):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    contract = w3.eth.contract(address=config.usdt_contract, abi=usdt_abi)
    balance = contract.functions.balanceOf(config.wallet).call()
    base_decimals = 10 ** contract.functions.decimals().call()
    return balance / base_decimals

def get_available_balance(mconfig, oconfig):
    balance = int(min(get_balance(mconfig), get_balance(oconfig))) // MARGIN_MIN * MARGIN_MIN - MARGIN_MIN
    if balance < MARGIN_MIN:
        balance = 0
    return balance

if __name__ == '__main__':
    for chain in [BNBTEST]:
        config = kiloconfigs[chain]
        print(get_balance(config))
        print(get_available_balance(config, config))
        approve_usdt_allowance(config, config.market_contract, 10000)
