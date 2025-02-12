import requests
from config_kiloex import BNBTEST,OTEST,MANTA,OPBNB,BNB,TAIKO

from functools import wraps
import time
import logging

def retry_conservative(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        index = 0
        while True:
            try:
                return fn(*args, **kwargs)
            except Exception:
                index = index + 1
                time.sleep(index)
                if index > 5:
                    raise
                else:
                    logging.info("meet Exception, retry:%s" % index)
                    continue

    return wrapper


def apienv(chain):
    if chain == MANTA:
        return 'manta'
    elif chain == OPBNB:
        return 'op'
    elif chain == BNB:
        return 'bnb'
    elif chain == TAIKO:
        return 'taiko'
    elif chain == BNBTEST:
        return 'test'
    elif chain == OTEST:
        return 'test'
    return 'op'

# 'https://app.kiloex.io/backendstatic/' + urlenv(chain) +'/symbols.json'
# res.status_code == 20
@retry_conservative
def index_symbols(chain=OPBNB):
    apistr = 'https://' + apienv(chain) +'api.kiloex.io/index/symbols?types=all'
    res = requests.get(apistr)
    return res.json()

def index_symbol(product_id, chain=OPBNB):
    res = index_symbols(chain)
    result = {}
    for i in res:
        result[i['id']] = i['name']

    return result.get(product_id)

@retry_conservative
def query_fundingList(chain):
    apistr = 'https://' + apienv(chain) +'api.kiloex.io/common/queryKiloCache'
    res = requests.get(apistr)
    return res.json()['kiloCache']['fundingBorrowList']

@retry_conservative
def query_productList(chain): # getProductsV2
    apistr = 'https://' + apienv(chain) +'api.kiloex.io/common/queryProducts'
    res = requests.get(apistr)
    return res.json()['productList']

@retry_conservative
def index_prices_current(chain=OPBNB):
    apistr = 'https://' + apienv(chain) +'api.kiloex.io/index/prices'
    res = requests.get(apistr)
    return res.json()['current']

def index_price(product_id, chain=OPBNB):
    res = index_prices_current(chain)
    result = float(res[str(product_id)])
    return result

if __name__ == "__main__":
    print(index_symbols())
    print(index_symbol(222))
    print(query_fundingList(BNBTEST))
    print(query_productList(BNBTEST))
    print(index_prices_current())
    print(index_price(1))
