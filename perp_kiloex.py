import logging
from web3 import Web3
from config_kiloex import BASE,BASE12,kiloconfigs,BNBTEST, OPBNB

with open('./abi/PerpTradeReader.abi', 'r') as f:
    view_abi = f.read()

class Position:
    def __init__(self, productId=0, leverage=0, price=0, oraclePrice=0, margin=0, account='', lastIncreasedTime=0,
                 isTrue=False, funding=0, borrowing=0):
        self.productId = productId
        self.leverage = int(leverage / BASE)
        self.price = price / BASE
        self.oraclePrice = oraclePrice / BASE
        self.margin = int(margin / BASE)
        self.account = account
        self.lastIncreasedTime = lastIncreasedTime
        self.isTrue = isTrue
        self.funding = funding / BASE12
        self.borrowing = borrowing / BASE12

    def __eq__(self, other):
        if isinstance(other, Position):
            #print(other.productId, other.margin, other.leverage)
            return self.productId == other.productId and self.margin == other.margin and self.leverage == other.leverage
        return False

    def __str__(self):
        return f"Position(productId={self.productId}, margin={self.margin}, isTrue={self.isTrue}, lastIncreasedTime={self.lastIncreasedTime}, leverage={self.leverage}, price={self.price}, funding={self.funding})"

def init_position():
    return Position()

def get_positions(config, product_ids):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    view_contract_w3 = w3.eth.contract(address=config.view_address, abi=view_abi)
    positions_raw = view_contract_w3.functions.getPositions(config.wallet, product_ids).call()
    positions = []
    for position_raw in positions_raw:
        position = Position(*position_raw)
        if position.margin > 0:
            positions.append(position)

    return positions

def match_position(positions, product_id):
    for position in positions:
        if product_id == position.productId:
            return position
    return None #init_position()

def get_position(config, product_id):
    positions = get_positions(config, [product_id])
    return match_position(positions, product_id)

class Product:
    def __init__(self, productId=0, fundingRates=0, maxOpenForLong=0, maxOpenForShort=0, isActive=False,openInterestLong=0, openInterestShort=0):
        self.product_id = productId
        self.open_interest_long = int(openInterestLong / BASE)
        self.open_interest_short = int(openInterestShort / BASE)
        self.max_open_for_long = int(maxOpenForLong / BASE)
        self.max_open_for_short = int(maxOpenForShort / BASE)
        self.isActive = isActive
        self.hourly_funding_rate = fundingRates/BASE/24/365

    def __str__(self):
        return f"Product(product_id={self.product_id}, open_interest_long={self.open_interest_long}, open_interest_short={self.open_interest_short}, max_open_for_long={self.max_open_for_long}, max_open_for_short={self.max_open_for_short}, isActive={self.isActive}, hourly_funding_rate={self.hourly_funding_rate})"

def init_product():
    return Product()

def get_products(config, ids):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    view_contract_w3 = w3.eth.contract(address=config.view_address, abi=view_abi)
    products_raw = view_contract_w3.functions.productSummary(ids).call()
    products = []
    for i in range(len(ids)):
        product = Product(ids[i], products_raw[0][i], products_raw[1][i], products_raw[2][i], products_raw[3][i], products_raw[4][i], products_raw[5][i])
        print(product)
    return products

# @notice Returns the spread for position
# @param productId id of product
# @param isLong true-long false-short
# @param amount amount of position, base 1e8
# @param isOpen open-true or close-false
# @return the spread base 1e8 50000=>50000/1e8=0.05%
def calculate_spread(productId, isLong=True, amount=0, is_open=True):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    view_contract_w3 = w3.eth.contract(address=config.view_address, abi=view_abi)
    return view_contract_w3.functions.calculateSpread(productId, isLong,amount, is_open).call()

if __name__ == '__main__':
    amount = 20  # margin = 20USDT
    leverage = 2  # leverage = 2x
    ids = [1, 2, 23, 31]

    config = kiloconfigs[OPBNB]
    print(int(BASE))

    print(init_position())
    print(init_product())

    print(get_position(config, 1))
    print(get_products(config, ids))

    print('calculate_spread', calculate_spread(110, True, 1000*10**8, True))
