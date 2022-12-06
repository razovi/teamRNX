
class Status:
    USD = 0
    BTC = 0
    curp = 0  # current price of btc
    CT = 0.003

    def __init__(self, exchange):
        self.exchange = exchange
        # balance = self.exchange.ex.fetch_balance()
        balance = self.exchange.get_acc_balance()
        self.BTC = float(balance['info'][0]['amount'])
        self.USD = float(balance['info'][1]['amount'])

    def buy(self):
        cBTC = self.BTC * self.curp  # btc cost=
        print(f"cBTC = self.BTC * self.curp: {cBTC}={self.BTC}x{self.curp}")
        TOT = cBTC + self.USD  #
        print(f"TOT = cBTC + self.USD: {TOT}={cBTC}+{self.USD}")
        cBTC /= TOT  #
        print(f"cBTC /= TOT: {cBTC}={cBTC}/{TOT}")
        amount = self.CT * (1 - cBTC)
        print(f"amount = self.CT * (1 - cBTC): {amount}={self.CT}/(1-{cBTC})")
        # exchange.createMarketBuyOrder("TESTBTC/TESTUSD", amount)
        # self.exchange.ex.createOrder("TESTBTC/TESTUSD", "market", "buy", amount)
        self.exchange.create_market_buy_order(amount, tp_pct=1, sl_pct=1)

    def sell(self):
        """
        Reduntant function
        :return:
        """
        cBTC = self.BTC * self.curp
        TOT = cBTC + self.USD
        cBTC /= TOT
        amount = self.CT * cBTC
        # exchange.createMarketSellOrder("TESTBTC/TESTUSD", amount)
        self.exchange.ex.createOrder("TESTBTC/TESTUSD", "market", "sell", amount)

    def exchange(self, x):
        if self.BTC + x < 0 or self.USD < x * self.curp:
            return
        self.USD -= x * self.curp
        self.BTC += x

    def wealth(self):
        return self.BTC * self.curp + self.USD

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.row < self.rows:
            self.row = self.row + 1
            return self.Data.iloc[self.row - 1]
        raise StopIteration()




