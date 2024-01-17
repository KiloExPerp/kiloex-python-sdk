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

## Basic Information

from the following interface you can get the symbol information in manta/opbnb/bnb

https://app.kiloex.io/backendstatic/manta/symbols.json

https://app.kiloex.io/backendstatic/opbnb/symbols.json

https://app.kiloex.io/backendstatic/bnb/symbols.json
