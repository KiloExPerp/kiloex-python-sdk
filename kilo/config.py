import configparser
import os

# Configure environment, default is BNBTEST (testing environment), BNB is production environment.
environment = 'BNBTEST'  # or BNB

print("current environment =", environment)

config_data = configparser.ConfigParser()
config_data.read('config.ini')

current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, "../.env.ini")
env_config_data = configparser.ConfigParser()
env_config_data.read(config_path)

chain_id = int(config_data.get(environment, 'chain_id'))
rpc = config_data.get(environment, 'rpc')
wallet = env_config_data.get(environment, 'wallet')
private_key = env_config_data.get(environment, 'private_key')
market_contract = config_data.get(environment, 'market_contract')
order_book_contract = config_data.get(environment, 'order_book_contract')
usdt_contract = config_data.get(environment, 'usdt_contract')
vault_address = config_data.get(environment, 'vault_address')
view_address = config_data.get(environment, 'view_address')
eth_product_id = int(config_data.get(environment, 'eth_product_id'))
btc_product_id = int(config_data.get(environment, 'btc_product_id'))
bnb_product_id = int(config_data.get(environment, 'bnb_product_id'))
precision = int(config_data.get(environment, 'precision'))
execution_fee = int(config_data.get(environment, 'execution_fee'))
gas_price = int(config_data.get(environment, 'gas_price'))
gas = int(config_data.get(environment, 'gas'))