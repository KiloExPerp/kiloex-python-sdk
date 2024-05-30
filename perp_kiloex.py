import logging
from web3 import Web3
from config_kiloex import BASE,BASE12,kiloconfigs,BNBTEST

with open('./abi/KiloPerpView.abi', 'r') as f:
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
    def __init__(self, productId=0, openInterestLong=0, openInterestShort=0, maxExposure=0, maxShift=0, reserve=0,
                 fundingMultiplier=0):
        self.product_id = productId
        self.open_interest_long = int(openInterestLong / BASE)
        self.open_interest_short = int(openInterestShort / BASE)
        self.max_exposure = int(maxExposure / BASE)
        self.max_shift = int(maxShift / BASE)
        self.reserve = int(reserve / BASE)
        self.funding_multiplier = fundingMultiplier / BASE12

    def __str__(self):
        return f"Product(product_id={self.product_id}, open_interest_long={self.open_interest_long}, open_interest_short={self.open_interest_short}, max_exposure={self.max_exposure}, funding_multiplier={self.funding_multiplier})"

def init_product():
    return Product()

def get_products(config, ids):
    w3 = Web3(Web3.HTTPProvider(config.rpc))
    view_contract_w3 = w3.eth.contract(address=config.view_address, abi=view_abi)
    products_raw = view_contract_w3.functions.getProductsV2(config.wallet, ids).call()
    products = []
    for product_raw in products_raw:
        product = Product(*product_raw) # TODO
        products.append(product)

    return products

if __name__ == '__main__':
    amount = 20  # margin = 20USDT
    leverage = 2  # leverage = 2x
    ids = [1, 2, 23, 31]

    config = kiloconfigs[BNBTEST]
    print(int(BASE))

    print(init_position())
    print(init_product())

    print(get_position(config, 1))

