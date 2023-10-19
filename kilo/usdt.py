from web3 import Web3
import config

web3 = Web3(Web3.HTTPProvider(config.rpc))

with open('../abi/Usdt.abi', 'r') as f:
    usdt_abi = f.read()

# Automatically authorize USDT limit with customizable value configuration.
def approve_usdt_allowance(to_address, amount):
    account = web3.eth.account.privateKeyToAccount(config.private_key)
    contract = web3.eth.contract(address=config.usdt_contract, abi=usdt_abi)
    allowance = contract.functions.allowance(config.wallet, to_address).call()
    allowance = allowance / 1e18
    # If the limit is below 1000 USDT, authorization is required.
    if allowance < 50000:
        data = contract.functions.approve(web3.toChecksumAddress(to_address), int(amount * 1e18)).buildTransaction({
            'from': config.wallet,
            'nonce': web3.eth.getTransactionCount(config.wallet),
            'gas': 200000,
            'gasPrice': web3.eth.gasPrice
        })

        signed_txn = account.signTransaction(data)
        try:
            tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
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
