import configparser
import os

BASE = int(1e8)
BASE12 = int(1e12)
MARGIN_MIN = int(10)
LEVERAGE_MIN = int(2)

BNBTEST = 'BNBTEST'
OTEST = 'OTEST'
MANTA = 'MANTA'
OPBNB = 'OPBNB'
BNB = 'BNB'
B2 = 'B2'
TAIKO = 'TAIKO'
BASE_MAINNET = 'BASE_MAINNET'

config_data = configparser.ConfigParser()
config_data.read('config_kiloex.ini')

current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, '.env.ini')
env_config_data = configparser.ConfigParser()
env_config_data.read(config_path)

def newKiloConfig(chain, configname, wallet_id=''):
    kiloconfig = KiloConfig(
        chain = chain,
        wallet = env_config_data.get(chain, 'wallet'),
        private_key = env_config_data.get(chain, 'private_key'),
        chain_id = int(config_data.get(configname, 'chain_id')),
        rpc = config_data.get(configname, 'rpc'),
        margin_contract = config_data.get(configname, 'margin_contract'),
        market_contract = config_data.get(configname, 'market_contract'),
        market_trigger_contract = config_data.get(configname, 'market_trigger_contract'),
        order_book_contract = config_data.get(configname, 'order_book_contract'),
        vault_address = config_data.get(configname, 'vault_address'),
        view_address = config_data.get(configname, 'view_address'),
        usdt_contract = config_data.get(configname, 'usdt_contract'),
        execution_fee = int(config_data.get(configname, 'execution_fee')),
        gas = int(config_data.get(configname, 'gas')),
    )
    print("chain=", chain, ", configname=", configname, ", kiloconfig=", kiloconfig)
    return kiloconfig
class KiloConfig:
    def __init__(self, chain='', chain_id=0, rpc='', wallet='', private_key='',
                 margin_contract='', market_contract='', market_trigger_contract='', order_book_contract='', vault_address='', view_address='', usdt_contract='',
                 execution_fee=0, gas=0):
        self.chain = chain
        self.chain_id = chain_id
        self.rpc = rpc
        self.wallet = wallet
        self.private_key = private_key
        self.margin_contract = margin_contract
        self.market_contract = market_contract
        self.market_trigger_contract = market_trigger_contract
        self.order_book_contract = order_book_contract
        self.vault_address = vault_address
        self.view_address = view_address
        self.usdt_contract = usdt_contract
        self.execution_fee = execution_fee
        self.gas = gas

    def __str__(self):
        return f"KiloConfig(chain={self.chain}, wallet={self.wallet}, chain_id={self.chain_id}, rpc={self.rpc}, margin_contract={self.margin_contract}, market_contract={self.market_contract}, market_trigger_contract={self.market_trigger_contract}, order_book_contract={self.order_book_contract}, vault_address={self.vault_address}, view_address={self.view_address}, usdt_contract={self.usdt_contract}, execution_fee={self.execution_fee}, gas={self.gas})"

kiloconfigs = {}
#for chain in [BNBTEST, OTEST]:
for chain in [BNBTEST, OTEST, MANTA, OPBNB, BASE_MAINNET]:
    kiloconfigs[chain] = newKiloConfig(chain, chain)
