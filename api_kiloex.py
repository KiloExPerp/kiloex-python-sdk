import requests
from config_kiloex import BNBTEST,OTEST,MANTA,OPBNB

def apienv(chain):
    if chain == MANTA:
        return 'manta'
    elif chain == OPBNB:
        return 'op'
    elif chain == BNBTEST:
        return 'test'
    elif chain == OTEST:
        return 'test'

def queryKiloCache(chain):
    res = requests.get('https://' + apienv(chain) +'api.kiloex.io/common/queryKiloCache')
    return res

def queryProducts(chain): # getProductsV2
    res = requests.get('https://' + apienv(chain) +'api.kiloex.io/common/queryProducts')
    return res

def index_prices(chain=OPBNB):
    res = requests.get('https://' + apienv(chain) +'api.kiloex.io/index/prices')
    return res

def index_price(product_id, chain=OPBNB):
    res = index_prices(chain).json()['current']
    result = float(res[str(product_id)])
    return result

if __name__ == "__main__":
    print(queryKiloCache(BNBTEST).json())
    print(queryProducts(BNBTEST).json())
    print(index_prices().json())
    print(index_price(1))