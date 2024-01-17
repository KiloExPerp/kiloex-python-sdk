# kilo-sdk



## Getting started

### File Description

```
# Basic Configuration Data Including Chain ID, RPC, etc.
kilo/config.ini 

# Load corresponding configuration based on environment setup, such as BNBTEST BNB.
kilo/config.py 

# Here is an example of market order API, including opening long and short positions with multiple orders, and closing long and short positions.
kilo/market_trade.py

# This is an example file of limit orders, which includes limit buy orders, limit sell orders, and limit orders with take profit and stop loss.
kilo/limit_trade.py

# This is an example file for a vault, which includes examples of how to deposit, check shares, and redeem.
kilo/vault.py

# This file mainly contains the logic of automatically authorizing the USDT quota. The logic and amount here can be configured according to actual needs.
kilo/usdt.py
```

### Key configuration.
```
# This file is a template data for .env.ini. First, you need to rename this file to .env.ini and change the wallet and private key inside to your own configuration.
env-example

[BNBTEST]
wallet = 0xBdC1248427332eCD8e08B2a3b2a1292CE37daB1b
private_key = 0xab57804aaacd2ba0a24a6657fcafb27bc126f3b5ba262b82218ad14722f6621e

[BNB]
wallet = 0xBdC1248427332eCD8e08B2a3b2a1292CE37daB1b
private_key = 0xab57804aaacd2ba0a24a6657fcafb27bc126f3b5ba262b82218ad14722f6621e
```

### Environment Switching
```
# This file can configure the environment parameter, currently there are 2 sets of environments that can be switched, including BNBTEST and BNB environment. You just need to specify the corresponding environment to complete the environment switching. 
kilo/config.py

environment = 'BNBTEST'  # or BNB
```

## Contract Address
```




```
## Quote and Candlestick

We using pyth network as our Oracle, So you can get price and candlestick history  from the pyth network, we use this too

https://benchmarks.pyth.network/docs#/TradingView/tradingview_streaming_route_v1_shims_tradingview_streaming_get 

## Basic Information

from the following interface you can get the symbol information in manta/opbnb/bnb

https://app.kiloex.io/backendstatic/manta/symbols.json

https://app.kiloex.io/backendstatic/opbnb/symbols.json

https://app.kiloex.io/backendstatic/bnb/symbols.json


### REST API 
```
Get information such as funding rates

https://api.kiloex.io/common/queryKiloCache
https://opapi.kiloex.io/common/queryKiloCache
https://mantaapi.kiloex.io/common/queryKiloCache

{
    "status":true,
    "time":1705497822973,
    "kiloCache":{
        "kiloConfig":{
            "minMargin":1000000000,//min margin
            "maxShift":200000,
            "minProfitTime":120,//The position must be greater than this time, otherwise pnl=0
            "exposureMultiplier":"15000",
            "utilizationMultiplier":"20000",
            "maxExposureMultiplier":"3",
            "liquidationBounty":"5000",
            "liquidationThreshold":"9000",
            "canUserStake":true,
            "allowPublicLiquidator":false,
            "isTradeEnabled":true,
            "adlMultiplier":"9"//When the profit exceeds 900%, the position is forced to be reduced
        },
        "fundingBorrowList":[
            {
                "productId":1, 
                "fundingRate":"48765542909", //1h funding rate % = 48765542909 / 1e12 / 365 / 24 * 100
                "cumulativeFunding":"12860196359",
                "borrowingRate":"14602690210",//1h borrowing rate % = 14602690210 / 1e12 / 365 / 24 * 100
                "cumulativeBorrowing":"4426068133",
                "funding":"12860165433"
            }
        ],
        "vaultBalance":"114070847080649",
        "prMinExecutionFee":"210000000000000", //market order execution Fee 210000000000000 / 1e18
        "obMinExecutionFee":"210000000000000" //limit order execution Fee 210000000000000 / 1e18
    }
}

Get python network oracle price

https://api.kiloex.io/index/prices
https://opapi.kiloex.io/index/prices
https://mantaapi.kiloex.io/index/prices

{
    "current":{
        "11":"5.69455654",
        "13":"0.5698006",
        "14":"101.39774675",
        "16":"18.36484625",
        "17":"35.99251357",
        "18":"158.43509256",
        "19":"2.74257284",
        "1":"2542.09418524",
        "2":"42587.91750075",
        "101":"2.91830363",
        "3":"69.04478786",
        "103":"2.05785",
        "5":"311.43527",
        "6":"0.83293208",
        "7":"0.08037285",
        "20":"2.96296134",
        "10":"15.9303861"
    },
    "previousDay":{
        "11":"5.90402619",
        "13":"0.57615686",
        "14":"96.5283245",
        "16":"19.3462",
        "17":"35.68558684",
        "18":"121.85358556",
        "19":"2.757901",
        "1":"2537.87198993",
        "2":"42961.0925",
        "101":"2.95877308",
        "3":"69.71557851",
        "103":"2.11196245",
        "5":"317.14771965",
        "6":"0.85013963",
        "7":"0.08189559",
        "20":"2.89020835",
        "10":"15.054"
    }
}

```
