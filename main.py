from trading_module.trader import Status
from cctx_module.cctx_interface import BitfinexExchangeAcc
from technical_indicators.rolling_avg import RollingAvg
from cctx_module.cctx_interface import BitfinexExchangeAcc


exchange = BitfinexExchangeAcc("real")


status = Status(exchange)
WINDOW = 10
WINDOW2 = 50
dq = RollingAvg(WINDOW)
dq2 = RollingAvg(WINDOW2)
startWealth = -1


while True:
    # status.curp = exchange.get_tick()["close"]
    status.curp = exchange.ex.fetch_ticker("BTC/USDT")["close"]
    if startWealth < 0:
        startWealth = status.wealth()
    dq.add(status.curp)
    dq2.add(status.curp)
    if len(dq2.dq) == WINDOW2:
        mean = dq.avg / WINDOW
        meanLong = dq2.avg / WINDOW2
        if mean < meanLong:
            status.buy()

        if mean > meanLong:
            status.sell()


time.sleep(0.1)

#######################################


pd.DataFrame(exchange.fetch_my_trades(symbol="TESTBTC/TESTUSD", since=None, limit=None, params={}))


price = exchange.fetchTickers(["BTC/USDT"])
# price = exchange.get_tick()

price = pd.DataFrame.from_dict(price)

price= price.to_numpy()

last_price = int((price[11]))
entry_point = int((price[7]))
stop_loss = int(entry_point-(entry_point*0.05))
take_profit = int(entry_point+(entry_point*0.05))

trade_risk=((entry_point-stop_loss)/(take_profit-entry_point))


trade_risk=((entry_point-stop_loss)/(take_profit-entry_point))
print(trade_risk)

