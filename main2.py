# from trading_module.trader import Status
from trading_module.traderv2 import Status
# from cctx_module.cctx_interface import BitfinexExchangeAcc
# from technical_indicators.rolling_avg import RollingAvg
from technical_indicators.rolling_avgV2 import RollingAvgV2
from cctx_module.cctx_interface import BitfinexExchangeAcc


exchange = BitfinexExchangeAcc("real")

# exchange.ex

print("exchange created")
status = Status(exchange)
fast_wndw = 10
short_wndw = 50
fast_rolling_avg = RollingAvgV2(fast_wndw)
slow_rolling_avg = RollingAvgV2(short_wndw)
startWealth = -1


while True:
    # update the trader with the most current tick, i.e. cur btc close price, balance info etc
    print("updating status with market tick data")
    status.update()
    if startWealth < 0:
        startWealth = status.cur_portfolio_val
    # add the current btc close price to each rolling window collections.deque()
    fast_rolling_avg.add(status.cur_close_price)
    slow_rolling_avg.add(status.cur_close_price)
    # check to see if the slow rolling avg wndw
    if len(slow_rolling_avg.dq) == short_wndw:
        slow_rolling_avg_mean = slow_rolling_avg.cur_avg
        fast_rolling_avg_mean = fast_rolling_avg.cur_avg
        # mean = fast_rolling_avg.avg / fast_wndw
        # meanLong = slow_rolling_avg.avg / short_wndw
        if slow_rolling_avg_mean < fast_rolling_avg_mean:
            status.buy(buy_amount_pct=2, tp_pct=1, sl_pct=1, verbose=1)
        if slow_rolling_avg_mean > fast_rolling_avg_mean:
            status.sell()


# time.sleep(0.1)
#
# #######################################
#
#
# pd.DataFrame(exchange.fetch_my_trades(symbol="TESTBTC/TESTUSD", since=None, limit=None, params={}))
#
#
# price = exchange.fetchTickers(["BTC/USDT"])
# # price = exchange.get_tick()
#
# price = pd.DataFrame.from_dict(price)
#
# price= price.to_numpy()
#
# last_price = int((price[11]))
# entry_point = int((price[7]))
# stop_loss = int(entry_point-(entry_point*0.05))
# take_profit = int(entry_point+(entry_point*0.05))
#
# trade_risk=((entry_point-stop_loss)/(take_profit-entry_point))
#
#
# trade_risk=((entry_point-stop_loss)/(take_profit-entry_point))
# print(trade_risk)

