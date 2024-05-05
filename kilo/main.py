
import market_trade
import config
import asyncio

def open_position(amount, leverage, market_price) :
    market_trade.open_market_increase_position(int(config.btc_product_id), int(amount * config.precision),
                                                    int(leverage * config.precision), True,
                                                    int((market_price * 0.002 + market_price) * config.precision),
                                                    int(config.execution_fee),
                                                    bytearray(32))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #market_price = asyncio.run(market_trade.get_price())
    market_price = 64000;
    print(market_price)
    open_position(10, 2, market_price)