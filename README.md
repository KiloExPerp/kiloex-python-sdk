![image](https://github.com/user-attachments/assets/30623a6a-45fa-4b26-9452-dae4ccff6a3d)# kilo-python-sdk



## Getting started

### File Description

```
# Basic Configuration Data Including Chain ID, RPC, etc.
config_kiloex.ini

# Load corresponding configuration based on environment setup, such as BNBTEST BNB.
config_kiloex.py

# Here is an example of market order API, including opening long and short positions with multiple orders, and closing long and short positions.
market_trade_kiloex.py

# This is an example file of limit orders, which includes limit buy orders, limit sell orders, and limit orders with take profit and stop loss.
limit_trade_kiloex.py

# This is an example file for a vault, which includes examples of how to deposit, check shares, and redeem.
vault_kiloex.py

# This file mainly contains the logic of automatically authorizing the USDT quota. The logic and amount here can be configured according to actual needs.
usdt_kiloex.py

# from this file you can calc spread, get product funding fee, max open position, current oi.
perp_kiloex.py
```

### Key configuration.
```
# This file is a template data for .env.ini. First, you need to rename this file to .env.ini and change the wallet and private key inside to your own configuration.
env-example

[BNBTEST]
wallet = 0xBdC1248427332eCD8e08B2a3b2a1292CE37daB1b
private_key = 0xab57804aaacd2ba0a24a6657fcafb27bc126f3b5ba262b82218ad14722f6621e

```

### Environment Switching
```
# This file can configure the environment parameter, currently there are 2 sets of environments that can be switched, including BNBTEST and BNB environment. You just need to specify the corresponding environment to complete the environment switching.
kilo/config.py

environment = 'BNBTEST'  # or ...
```

## Contract Address

wallet = 7cRnmWXhaM3NbrcMP3EJ8DArioZpSraQxgPUFbRtZv7E

### opBNB Network
```
"kiloStorageManagerAddr": "0x1EbEd4024308afcb05E6938eF8Ebd1ec5d6E8C46",
"kusdAddr": "0x9e5aac1ba1a2e6aed6b32689dfcf62a509ca96f3",
"perpTradeAddr": "0x1a7b3F8890Da3cC6968c182fA528CE9C9C62f981",
"orderBookAddr": "0x43E3E6FFb2E363E64cD480Cbb7cd0CF47bc6b477",
"positionRouterAddr": "0xa02d433868C7Ad58C8A2A820d6C3FF8a15536ACc",
"tradeRewardDistributorAddr": "0xB1d06544B5c34f5b85AaD37cdFFd58610D7a8fBc"
"marketOrderWithTriggerOrderAddr": "0xe0eE1Cb99843c6dCdeb701707DaaDf9Ea8b752f7",
"hybridVaultAddr": "0x1Bc6F42D6D1680115A52F82DFA29265085E91d93",
"perpTradeReaderAddr": "0x2f179F55a780C44e319241031cD596eB6f1266bC",
```

### Bnb mainnet
```
"kiloStorageManagerAddr": "0xfE03be1b0504031e92eDA810374222c944351356",
"kusdAddr": "0x55d398326f99059fF775485246999027B3197955",
"perpTradeAddr": "0x7C09a8df940cF1D14d4C24f90aCa39EE619f0864",
"orderBookAddr": "0x746c180268825B52FC5ea8057ecf3768037692E2",
"positionRouterAddr": "0x298e94D5494E7c461a05903DcF41910e0125D019",
"tradeRewardDistributorAddr": "0x0811e132fA5802d136C34e5B3cfbD800eA98B451"
"marketOrderWithTriggerOrderAddr": "0x256035E9099C266F2a9bd3BDebC4c3f5a623EaeB",
"hybridVaultAddr": "0xef7aF0804AAB3885da59a8236fabfA19DDc6Cf48",
"perpTradeReaderAddr": "0x078E31821C94e5a99a64Fdc60cCae97E807ffCda",
```

###  Manta mainnet
```
"kiloStorageManagerAddr": "0x1EbEd4024308afcb05E6938eF8Ebd1ec5d6E8C46",
"kusdAddr": "0xf417F5A458eC102B90352F697D6e2Ac3A3d2851f",
"perpTradeAddr": "0x1a7b3F8890Da3cC6968c182fA528CE9C9C62f981",
"orderBookAddr": "0x43E3E6FFb2E363E64cD480Cbb7cd0CF47bc6b477",
"positionRouterAddr": "0xa02d433868C7Ad58C8A2A820d6C3FF8a15536ACc",
"tradeRewardDistributorAddr": "0xB1d06544B5c34f5b85AaD37cdFFd58610D7a8fBc",
"marketOrderWithTriggerOrderAddr": "0xF1fd3C545ED6eC401E50A8AeEeFE00E9A2BEC648",
"hybridVaultAddr": "0xa10f74374b8bE9E9C8Fb62c1Dc17B8D4247E332A",
"perpTradeReaderAddr": "0xE47262628F70981177AF961c75d1aA0d29aAd4d0",
```

###  Base mainnet
```
"kiloStorageManagerAddr": "0x7BC8D56cC78cF467C7230B77De0fcBDea9ac44cE",
"kusdAddr": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
"perpTradeAddr": "0xA2E2F3726DF754C1848C8fd1CbeA6aAFF84FC5B2",
"orderBookAddr": "0xa02d433868C7Ad58C8A2A820d6C3FF8a15536ACc",
"positionRouterAddr": "0x796f1793599D7b6acA6A87516546DdF8E5F3aA9d",
"perpTradeReaderAddr": "0xE47262628F70981177AF961c75d1aA0d29aAd4d0",
"tradeRewardDistributorAddr": "0x61E1200f18302C7B140E8398187cC2254250fFd5",
"marketOrderWithTriggerOrderAddr": "0x9438b892e292EbF8eCB6ceeB3Ecbb2B0D46AE107",
"hybridVaultAddr": "0xdf5ACC616cD3ea9556EC340a11B54859a393ebBB",
```

### Bnbtest testnet
```
"kiloStorageManagerAddr": "0x9d444b07cf87BA9186DbB62A662d726Ce7775155",
"kusdAddr": "0x7ce794304CBc54c3DeeA8Afa175F5B2458dDE460",
"perpTradeAddr": "0x6180C080A6daDe02cAb58ABDaed21796cE4a2a82",
"orderBookAddr": "0x764b8A92015aBabc112B42D289BB672Bfb02779e",
"positionRouterAddr": "0x9cDaC1e06994aBfba5d6D8DC3683552c7b2E023D",
"tradeRewardDistributorAddr": "0x690461cBf0d2D213028C810D94299dB7D9E6368E",
"perpTradeReaderAddr": "0x4D2B14724536B27811DD0f8dAd83253aA5e2bbA7"
```

## Quote and Candlestick

We using pyth network as our Oracle, So you can get price and candlestick history  from the pyth network, we use this too

https://benchmarks.pyth.network/docs#/TradingView/tradingview_streaming_route_v1_shims_tradingview_streaming_get

## Basic Information

from the following interface you can get the symbol information in manta/opbnb/bnb/base

https://mantaapi.kiloex.io/index/symbols?types=all

https://opapi.kiloex.io/index/symbols?types=all

https://api.kiloex.io/index/symbols?types=all

https://baseapi.kiloex.io/index/symbols?types=all


### REST API
```


Get symbol details
https://api.kiloex.io/common/queryProducts?types=all
https://opapi.kiloex.io/common/queryProducts?types=all
https://mantaapi.kiloex.io/common/queryProducts?types=all
https://baseapi.kiloex.io/common/queryProducts?types=all

{
    "status":true,
    "time":1705564929024,
    "productList":[
        {
            "productId":1,
            "productToken":"0x9ef1b8c0e4f7dc8bf5719ea496883dc6401d5b2e",
            "maxLeverage":10000000000,//Maximum leverage
            "minLeverage":200000000,//Minimum leverage
            "productFee":10,//fee 10 / 1e4
            "isActive":true,// true tradable
            "openInterestLong":6959079090084,//open interest long
            "openInterestShort":264055003556,//open interest short
            "weight":200,
            "reserve":250000000000000000,
            "maxExposure":75241618260109,//max exposure
            "minPriceChange":20,//
            "maxPositionSize":50000000000000,//User's maximum position limit
            "maxShift":0
        }
    ]
}


Get information such as funding rates

https://api.kiloex.io/common/queryKiloCache
https://opapi.kiloex.io/common/queryKiloCache
https://mantaapi.kiloex.io/common/queryKiloCache
https://baseapi.kiloex.io/common/queryKiloCache

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
https://baseapi.kiloex.io/index/prices

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
