import ccxt
# Create instance for your exchange, here binance
bitfinex = ccxt.bitfinex()
# Quick test to verify data access
# Get the last 2 hours candelsticks from the pair 'BTC/USDT'
pair = 'TESTBTC/TESTUSD'
bitfinex.fetch_ohlcv(pair, limit=2)

import time
current_milli_time = lambda x: int(round((time.time()- 3600*x) * 1000))



# install pandas with pip install pandas, perfect library for manipulate our dataset
import pandas as pd
symbol = 'TESTBTC/TESTUSD'
print(symbol)
ohlcv_dataframe = pd.DataFrame()
for hours in range(4320,0,-600): # 6 month is around 24hours * 30days * 6 = 4320
    if bitfinex.has['fetchOHLCV']:
        time.sleep (bitfinex.rateLimit / 1000) # time.sleep wants seconds
        # the limit from binance is 1000 timesteps
        ohlcv = bitfinex.fetch_ohlcv(symbol, '1h', since=current_milli_time(hours),
                                    limit=1000)
        ohlcv_dataframe = ohlcv_dataframe.append(pd.DataFrame(ohlcv))
        print(hours)
# We are changing the name of the columns, important to use trading indicators later on
ohlcv_dataframe['date']   = ohlcv_dataframe[0]
ohlcv_dataframe['open']   = ohlcv_dataframe[1]
ohlcv_dataframe['high']   = ohlcv_dataframe[2]
ohlcv_dataframe['low']    = ohlcv_dataframe[3]
ohlcv_dataframe['close']  = ohlcv_dataframe[4]
ohlcv_dataframe['volume'] = ohlcv_dataframe[5]
ohlcv_dataframe = ohlcv_dataframe.set_index('date')
# Change the timstamp to date in UTC
ohlcv_dataframe = ohlcv_dataframe.set_index(
    pd.to_datetime(ohlcv_dataframe.index, unit='ms').tz_localize('UTC'))
ohlcv_dataframe.drop([0,1,2,3,4,5], axis=1, inplace=True)
# Create CSV file from our panda dataFrame
ohlcv_dataframe.to_csv('data_since6months_freq1h'+symbol.split('/')[0]+'.csv')