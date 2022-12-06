
class Status:
    # USD = 0
    # BTC = 0
    # curp = 0  # current price of btc
    # CT = 0.003

    def __init__(self, exchange):
        self.exchange = exchange
        self.cur_market_tick = self.exchange.ex.fetch_ticker("TESTBTC/TESTUSD")
        self.cur_close_price = self.cur_market_tick["close"]
        # self.exchange = exchange
        # balance = self.exchange.ex.fetch_balance()
        self.balance = self.exchange.get_acc_balance()
        # self.btc_amount = float(self.balance['info'][0]['amount'])
        # self.usd_amount = float(self.balance['info'][1]['amount'])
        self.btc_amount_amount = self.balance["total"]["TESTBTC"]
        self.usd_amount_amount = self.balance["total"]["TESTUSD"]
        self.cur_portfolio_val = self.usd_amount_amount + self.cur_close_price * self.btc_amount_amount

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.row < self.rows:
            self.row = self.row + 1
            return self.Data.iloc[self.row - 1]
        raise StopIteration()

    # def update_current_btc_usd_price(self):
    def update_cur_market_tick(self):
        # self.cur_close_price = self.exchange.ex.fetch_ticker("TESTBTC/TESTUSD")["close"]
        self.cur_market_tick = self.exchange.ex.fetch_ticker("TESTBTC/TESTUSD")
        self.cur_close_price = self.cur_market_tick["close"]

    def update_acc_balance(self):
        self.balance = self.exchange.get_acc_balance()

    def update_btc_usd_amounts(self):
        self.btc_amount_amount = self.balance["total"]["TESTBTC"]
        self.usd_amount_amount = self.balance["total"]["TESTUSD"]

    def update_cur_portfolio_val(self):
        self.cur_portfolio_val = self.usd_amount_amount + self.cur_close_price * self.btc_amount_amount

    def update(self):
        # self.update_current_btc_usd_price()
        self.update_cur_market_tick()
        self.update_acc_balance()
        self.update_btc_usd_amounts()
        self.update_cur_portfolio_val()

    def buy(self, buy_amount_pct=2, tp_pct=1, sl_pct=1, verbose=1):
        cur_portfolio_btc_amount_usd_val = self.btc_amount * self.cur_close_price
        # print(f"cur_btc_amount_val = self.btc_amount * self.curp: {cur_btc_amount_val}={self.btc_amount}x{self.cur_close_price}")
        cur_tot_balance_val = cur_portfolio_btc_amount_usd_val + self.usd_amount  #
        # print(f"cur_tot_balance_val = cur_btc_amount_val + self.usd_amount: {cur_tot_balance_val}={cur_btc_amount_val}+{self.usd_amount}")
        # cur_btc_amount_val = cur_btc_amount_val / cur_tot_balance_val  #
        # print(f"cur_btc_amount_val /= cur_tot_balance_val: {cur_btc_amount_val}={cur_btc_amount_val}/{cur_tot_balance_val}")
        buy_amount_usd = (buy_amount_pct/100) * cur_tot_balance_val
        buy_amount_btc = buy_amount_usd / self.cur_close_price
        print(f"buy_amount_usd: {buy_amount_usd}")
        print(f"buy_amount_btc: {buy_amount_btc}")
        # amount = self.CT * (1 - cur_btc_amount_val)
        # print(f"amount = self.CT * (1 - cur_btc_amount_val): {amount}={self.CT}/(1-{cur_btc_amount_val})")
        # exchange.createMarketBuyOrder("TESTBTC/TESTUSD", amount)
        # self.exchange.ex.createOrder("TESTBTC/TESTUSD", "market", "buy", amount)
        # self.exchange.create_market_buy_order(amount, tp_pct=1, sl_pct=1)
        if verbose == 1:
            info = f"Buy order created @ {self.cur_close_price} for BTC {buy_amount_btc} (=${buy_amount_usd})"
            print(info)
        self.exchange.create_market_buy_order(amount=buy_amount_btc, tp_pct=tp_pct, sl_pct=sl_pct)

    def sell(self):
        """
        Reduntant function
        :return:
        """
        cBTC = self.btc_amount * self.cur_close_price
        TOT = cBTC + self.usd_amount
        cBTC /= TOT
        amount = self.CT * cBTC
        # exchange.createMarketSellOrder("TESTBTC/TESTUSD", amount)
        self.exchange.ex.createOrder("TESTBTC/TESTUSD", "market", "sell", amount)







