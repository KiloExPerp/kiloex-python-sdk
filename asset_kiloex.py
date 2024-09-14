from web3 import Web3
from config_kiloex import MARGIN_MIN,BNBTEST,OTEST,MANTA,OPBNB,BNB,B2,kiloconfigs

import usdt_kiloex
import perp_kiloex

def get_asset(mconfig, oconfig):
    ids = []
    asset = usdt_kiloex.get_balance(mconfig) + usdt_kiloex.get_balance(oconfig)
    mpositions = perp_kiloex.get_positions(mconfig, ids)
    for mposition in mpositions:
        asset += mposition.margin
    opositions = perp_kiloex.get_positions(oconfig, ids)
    for oposition in opositions:
        asset += oposition.margin
    return asset

if __name__ == '__main__':
    print(get_asset(kiloconfigs[BNBTEST], kiloconfigs[OTEST]))
    #print(get_asset(kiloconfigs[MANTA], kiloconfigs[OPBNB]))
    #print(get_asset(kiloconfigs[BNB], kiloconfigs[B2]))
