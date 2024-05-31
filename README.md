# kilo-python-sdk



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

### opBNB Network
```
"pendingRewardAddr": "0xb31c987b7c919d4021b928849CdB5A464BaBf56F",
"kiloStorageManagerAddr": "0x1EbEd4024308afcb05E6938eF8Ebd1ec5d6E8C46",
"productManagerAddr": "0x22c40b883b5976F13c78eE45eAd6b0CDc192daE5",
"kiloPriceFeedAddr": "0x7BC8D56cC78cF467C7230B77De0fcBDea9ac44cE",
"marginFeeManagerAddr": "0x19653dc8D30E39442B9cc96cb60d755E49A2717c",
"kusdAddr": "0x9e5aac1ba1a2e6aed6b32689dfcf62a509ca96f3",
"perpTradeAddr": "0x1a7b3F8890Da3cC6968c182fA528CE9C9C62f981",
"vaultStakeRewardAddr": "0xA2E2F3726DF754C1848C8fd1CbeA6aAFF84FC5B2",
"orderBookAddr": "0x43E3E6FFb2E363E64cD480Cbb7cd0CF47bc6b477",
"positionRouterAddr": "0xa02d433868C7Ad58C8A2A820d6C3FF8a15536ACc",
"kiloPerpViewAddr": "0x796f1793599D7b6acA6A87516546DdF8E5F3aA9d",
"liquidationPriceReaderAddr": "0x4fbC5c4732AF582d826dd30F442918cA56A2c53E",
"referralStorageManagerAddr": "0xac9BB99939bA91660ab3E1a28d63Cb4e0D17f5De",
"protocolRewardAddr": "0x298e94D5494E7c461a05903DcF41910e0125D019",
"tradeRewardDistributorAddr": "0xB1d06544B5c34f5b85AaD37cdFFd58610D7a8fBc"
```

### Bnb mainnet
```
"pendingRewardAddr": "0x8fd9e2457C7Df433D06BC45Dd1B134AF19a0a246",
"kiloStorageManagerAddr": "0xfE03be1b0504031e92eDA810374222c944351356",
"productManagerAddr": "0x8995edcfB225FfEa58Bf4C0E24272eEb89bC9533",
"kiloPriceFeedAddr": "0x1b64Eb04F9E62e1f3D1599D65FcFA8CC2dc44024",
"marginFeeManagerAddr": "0xC23b49051257fa3D5AAbA16a2CE2aF8A04973C48",
"kusdAddr": "0x55d398326f99059fF775485246999027B3197955",
"perpTradeAddr": "0x7C09a8df940cF1D14d4C24f90aCa39EE619f0864",
"vaultStakeRewardAddr": "0x1c3f35F7883fc4Ea8C4BCA1507144DC6087ad0fb",
"orderBookAddr": "0x746c180268825B52FC5ea8057ecf3768037692E2",
"positionRouterAddr": "0x298e94D5494E7c461a05903DcF41910e0125D019",
"kiloPerpViewAddr": "0x92A381C496eeE6C4686A4169aFf4aF94eAfeAFCc",
"liquidationPriceReaderAddr": "0x6152493B9E2ac4f89896af4F10B3cACdC9cf4BB0",
"referralStorageManagerAddr": "0x61E1200f18302C7B140E8398187cC2254250fFd5",
"protocolRewardAddr": "0xd62d82cE1D403d8a9d9fAcE699Cde9064e54b95c",
"tradeRewardDistributorAddr": "0x0811e132fA5802d136C34e5B3cfbD800eA98B451"
```

###  Manta mainnet
```
"pendingRewardAddr": "0xb31c987b7c919d4021b928849CdB5A464BaBf56F",
"kiloStorageManagerAddr": "0x1EbEd4024308afcb05E6938eF8Ebd1ec5d6E8C46",
"productManagerAddr": "0x22c40b883b5976F13c78eE45eAd6b0CDc192daE5",
"kiloPriceFeedAddr": "0x7BC8D56cC78cF467C7230B77De0fcBDea9ac44cE",
"marginFeeManagerAddr": "0x19653dc8D30E39442B9cc96cb60d755E49A2717c",
"kusdAddr": "0xf417F5A458eC102B90352F697D6e2Ac3A3d2851f",
"perpTradeAddr": "0x1a7b3F8890Da3cC6968c182fA528CE9C9C62f981",
"vaultStakeRewardAddr": "0xA2E2F3726DF754C1848C8fd1CbeA6aAFF84FC5B2",
"orderBookAddr": "0x43E3E6FFb2E363E64cD480Cbb7cd0CF47bc6b477",
"positionRouterAddr": "0xa02d433868C7Ad58C8A2A820d6C3FF8a15536ACc",
"kiloPerpViewAddr": "0x796f1793599D7b6acA6A87516546DdF8E5F3aA9d",
"liquidationPriceReaderAddr": "0x4fbC5c4732AF582d826dd30F442918cA56A2c53E",
"referralStorageManagerAddr": "0xac9BB99939bA91660ab3E1a28d63Cb4e0D17f5De",
"protocolRewardAddr": "0x298e94D5494E7c461a05903DcF41910e0125D019",
"tradeRewardDistributorAddr": "0xB1d06544B5c34f5b85AaD37cdFFd58610D7a8fBc",
```

### Bnbtest testnet
```
"pendingRewardAddr": "0x4dE3273F7fCFf1C1517Cd0e94819AC38FD8A4722",
"kiloStorageManagerAddr": "0x9d444b07cf87BA9186DbB62A662d726Ce7775155",
"productManagerAddr": "0xe7b4DBdeCe3B32aD1AFB6041623BD32F5a137985",
"kiloPriceFeedAddr": "0x3E5C07FC3E31718D1E464CDb5B6e1DA16067ae27",
"marginFeeManagerAddr": "0xd73d32c57C576f3bCC7ACa4870Fd662793dE0C75",
"kusdAddr": "0x7ce794304CBc54c3DeeA8Afa175F5B2458dDE460",
"perpTradeAddr": "0x6180C080A6daDe02cAb58ABDaed21796cE4a2a82",
"vaultStakeRewardAddr": "0xEBF0ea0aE187cD3520E52a069101fA21f1cc51Eb",
"orderBookAddr": "0x764b8A92015aBabc112B42D289BB672Bfb02779e",
"positionRouterAddr": "0x9cDaC1e06994aBfba5d6D8DC3683552c7b2E023D",
"kiloPerpViewAddr": "0xC5732F22D71286Dd25A663A21550Df0d5144d7DA",
"liquidationPriceReaderAddr": "0xDE5C6cAfef10515f4c23c932497191aDCb51a86e",
"referralStorageManagerAddr": "0x752C553D466C4268E6E0300e91B769137b62496a",
"protocolRewardAddr": "0x127628592bf6e386A98d69BDBe8f5DD3c3763794",
"tradeRewardDistributorAddr": "0x690461cBf0d2D213028C810D94299dB7D9E6368E",
"kiloPassCardAddr": "0x819f675875349DD4f52d31d5902F07b4b5471cE7"
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


Get symbol details
https://api.kiloex.io/common/queryProducts
https://opapi.kiloex.io/common/queryProducts
https://mantaapi.kiloex.io/common/queryProducts


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
