from web3 import Web3
import config

w3 = Web3(Web3.HTTPProvider(config.rpc))

with open('../abi/Usdt.abi', 'r') as f:
    usdt_abi = f.read()

# Automatically authorize USDT limit with customizable value configuration.
def approve_usdt_allowance(to_address, amount):
    account = w3.eth.account.from_key(config.private_key)
    contract = w3.eth.contract(address=config.usdt_contract, abi=usdt_abi)
    allowance = contract.functions.allowance(config.wallet, to_address).call()
    allowance = allowance / 1e18
    # If the limit is below 1000 USDT, authorization is required.
    if allowance < 50000:
        print('Allowance is insufficient, approving...')
        data = contract.functions.approve(w3.to_checksum_address(to_address), int(amount * 1e18)).build_transaction({
            'from': config.wallet,
            'nonce': w3.eth.get_transaction_count(config.wallet),
            'gas': 200000,
            'gasPrice': w3.eth.gas_price
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
            print('An error occurred:', e)
        return False
    else:
        print('Allowance is already sufficient.')
        return True


if __name__ == '__main__':
    approve_usdt_allowance(config.market_contract, 10000)
