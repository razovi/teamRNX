import cctx
import ccxt as ccxt


class BitfinexExchangeAcc:

    def __init__(self, account_type):
        self.account_type = account_type
        self.symbol = "TESTBTC/TESTUSD"
        self.exchange_id = "bitfinex"
        self.test_api_key = "Knv1zLXwUpBF9vdQVgvpYyua9oUqvNtpGIZolRufQ8l"
        self.test_secret_key = "Mpan2vh8N0Hp9Xa1TcMyahMsvuDW2A27IMEYtWAzzdc"
        self.real_api_key = "XfUXDuWVUYSizHOVdOMEX29uswhoOonC7hklTnKmvSQ"
        self.real_secret_key = "e7uwxwFMdJkdykaFH4MK863NkypClOAiC2kRqteW3Mj"
        self.ex_cls = getattr(ccxt, self.exchange_id)
        if self.account_type == "test":
            self.ex = self.ex_cls({'apiKey': self.test_api_key, 'secret': self.test_secret_key, })
        elif self.account_type == "real":
            self.ex = self.ex_cls({'apiKey': self.real_api_key, 'secret': self.real_secret_key, })
        else:
            self.ex = self.ex_cls({'apiKey': self.test_api_key, 'secret': self.test_secret_key, })

        self.buy_orders = []
        self.sell_orders = []

    def get_acc_balance(self):
        balance = self.ex.fetch_balance()
        return balance

    # def get_open_orders(self):
    #     open_orders = self.ex.fetch_open_orders(symbol=self.symbol)
    #     return open_orders
    #
    # def get_closed_orders(self):
    #     closed_orders = self.ex.fetch_closed_orders(symbol=self.symbol)
    #     return closed_orders

    # def get_all_orders(self):
    #     orders = self.ex.fetch_orders(symbol=self.symbol)
    #     return orders

    def create_market_buy_order(self, amount, tp=None, sl=None):
        """
        Give USD to get BTC
        # Place Market BTC Buy Order for amount (vol) = 2.15
        # ftx.create_order('SOL/USD', 'market', 'buy', 2.15)
        :param amount: How much BTC to buy with USD, e.g. amount=1 (BTC)
        :param type:
        :return:
        """
        params = {}
        if tp is not None:
            params["takeProfitPrice"] = tp
        if sl is not None:
            params["stopLossPrice"] = sl
        buy_order = self.ex.create_order(self.symbol, "market", "buy", amount)
        self.buy_orders.append(buy_order)
        return buy_order

    def create_market_sell_order(self, amount, tp=None, sl=None):
        """
        Give BTC to get USD
        buy side: buy give quote currency and receive base currency;
        for example, buying BTC/USD means that you will receive bitcoins for your dollars.
        # Place Market Sell Order, Selling volume = 2.15 for $300
        # ftx.create_order('SOL/USD', 'market', 'sell', 2.15)
        :param amount: How much USD to buy, e.g. amount=15000
        :param type:
        :return:
        """
        params = {}
        if tp is not None:
            params["takeProfitPrice"] = tp
        if sl is not None:
            params["stopLossPrice"] = sl
        sell_order = self.ex.create_order(self.symbol, "market", "sell", amount)
        self.sell_orders.append(sell_order)
        return sell_order

    # def create_limit_buy_order(self, amount, price, ):
    #     self.ex.create_limit_buy_order(self.symbol, amount, price, params)





if __name__ == "__main__":
    ex = BitfinexExchangeAcc("real")
    # ex.ex.verbose = True
    # print(ex.get_acc_balance())
    # print(ex.sell_orders)
    # test_sell_order_usd_amount = 100
    # # test_buy_order_btc_amount = 0.0001
    # ex.create_market_sell_order(test_sell_order_usd_amount)
    # # ex.create_market_buy_order(test_buy_order_btc_amount)
    # print("\nSELL ORDER OF AMOUNT 100 CREATED\n")
    # # print("\nBUY ORDER OF AMOUNT 0.0001 CREATED\n")
    # print(ex.get_acc_balance())
    # print(ex.sell_orders)
    # # print(f"balance: {balance}")