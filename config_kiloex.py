import configparser
import os

BASE = int(1e8)
BASE12 = int(1e12)
MARGIN_MIN = int(10)
LEVERAGE = int(2)

BNBTEST = 'BNBTEST'
OTEST = 'OTEST'
MANTA = 'MANTA'
OPBNB = 'OPBNB'

config_data = configparser.ConfigParser()
config_data.read('config_kiloex.ini')

current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, '.env.ini')
env_config_data = configparser.ConfigParser()
env_config_data.read(config_path)

class KiloConfig:
    def __init__(self, chain='', chain_id=0, rpc='', wallet='', private_key='',
                 margin_contract='', market_contract='', order_book_contract='', vault_address='', view_address='', usdt_contract='',
                 execution_fee=0, gas=0):
        self.chain = chain
        self.chain_id = chain_id
        self.rpc = rpc
        self.wallet = wallet
        self.private_key = private_key
        self.margin_contract = margin_contract
        self.market_contract = market_contract
        self.order_book_contract = order_book_contract
        self.vault_address = vault_address
        self.view_address = view_address
        self.usdt_contract = usdt_contract
        self.execution_fee = execution_fee
        self.gas = gas

    def __str__(self):
        return f"KiloConfig(chain={self.chain}, chain_id={self.chain_id}, rpc={self.rpc}, wallet={self.wallet}, margin_contract={self.margin_contract}, market_contract={self.market_contract}, order_book_contract={self.order_book_contract}, vault_address={self.vault_address}, view_address={self.view_address}, usdt_contract={self.usdt_contract}, execution_fee={self.execution_fee}, gas={self.gas})"

kiloconfigs = {}
for chain in [BNBTEST, OTEST, MANTA, OPBNB] :
    kiloconfigs[chain] = KiloConfig(
        chain = chain,
        chain_id = int(config_data.get(chain, 'chain_id')),
        rpc = config_data.get(chain, 'rpc'),
        wallet = env_config_data.get(chain, 'wallet'),
        private_key = env_config_data.get(chain, 'private_key'),
        margin_contract = config_data.get(chain, 'margin_contract'),
        market_contract = config_data.get(chain, 'market_contract'),
        order_book_contract = config_data.get(chain, 'order_book_contract'),
        vault_address = config_data.get(chain, 'vault_address'),
        view_address = config_data.get(chain, 'view_address'),
        usdt_contract = config_data.get(chain, 'usdt_contract'),
        execution_fee = int(config_data.get(chain, 'execution_fee')),
        gas = int(config_data.get(chain, 'gas')),
        )
    print("chain=", chain, ", kiloconfig=", kiloconfigs[chain])
