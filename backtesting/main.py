# from technical_indicators import rsi
# from technical_indicators import rsi_mini
from data_downloader import BTCUSDData
from trade_sim import TradeSim
from bots.rsi_bot import RSIBot


data_src = BTCUSDData()
bot = RSIBot()
trade_sim = TradeSim(data_src)

bot.run_tick(trade_sim.get_tick())


# btcusd_data = btcusd._data
# close = btcusd_data["Close"]







# rsi = rsi.RSI(close, time_period=14, overbought_level=70, oversold_level=30)
# rsi = rsi_mini.get_rsi_values(close)
# rsi_sig = rsi_mini.get_rsi_int_labels_ts(rsi)
# print(rsi_sig)
# rsi_values = rsi.get_rsi_values()
# rsi.get_rsi_int_labels_ts()