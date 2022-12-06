import cctx
import ccxt as ccxt
import time
import pandas as pd


class BitfinexExchangeAcc:

    def __init__(self, account_type):
        self.account_type = account_type
        self.symbol = "TESTBTC/TESTUSD"
        self.exchange_id = "bitfinex"
        self.test_api_key = "Knv1zLXwUpBF9vdQVgvpYyua9oUqvNtpGIZolRufQ8l"
        self.test_secret_key = "Mpan2vh8N0Hp9Xa1TcMyahMsvuDW2A27IMEYtWAzzdc"
        # self.real_api_key = "XfUXDuWVUYSizHOVdOMEX29uswhoOonC7hklTnKmvSQ"
        self.real_api_key = "yNN9StYqCEuVT30ktlIGtuFQxioA7iwzoNXiKKeKg1Y"
        # self.real_secret_key = "e7uwxwFMdJkdykaFH4MK863NkypClOAiC2kRqteW3Mj"
        self.real_secret_key = "tHyQx1Y6FdZQlsM7mOhE5sKJ0kLmav1yXrX76RuZn1T"
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

    def get_tot_acc_balance(self):
        tot_balance = self.ex.fetch_total_balance()
        return tot_balance

    # def get_tick(self):
    #     tick = self.ex.fetch_ticker(self.symbol)
    #     return tick

    def get_my_trades(self):
        my_trades = self.ex.fetch_my_trades(self.symbol)
        return my_trades

    # def create_market_buy_order(self, amount, tp_pct=None, sl_pct=None):
    def create_market_buy_order(self, amount, tp_pct=1, sl_pct=1):
        """
        Give USD to get BTC
        # Place Market BTC Buy Order for amount (vol) = 2.15
        # ftx.create_order('SOL/USD', 'market', 'buy', 2.15)
        :param amount: How much BTC to buy with USD, e.g. amount=1 (BTC)
        :param type:
        :return:
        """
        tp_sl_params = {}
        close_price = self.ex.fetch_ticker(self.symbol)["close"]
        if tp_pct is not None:
            tp_price = close_price * ((tp_pct/100)+1)
            tp_sl_params["takeProfitPrice"] = tp_price
        if sl_pct is not None:
            sl_price = close_price * ((sl_pct / 100) + 1)
            tp_sl_params["stopLossPrice"] = sl_price
        buy_order = self.ex.create_order(self.symbol, "market", "buy", amount, params=tp_sl_params)
        self.buy_orders.append(buy_order)
        # return buy_order

    def create_market_sell_order(self, amount, tp=None, sl=None):
        """
        DONT USE THIS METHOD! ONLY USE create_market_buy_order(..)
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

    def build_hist_ohlcv(self, save_csv_data=False):
        current_milli_time = lambda x: int(round((time.time() - 3600 * x) * 1000))
        ohlcv_dataframe = pd.DataFrame()
        for hours in range(4320, 0, -600):
            if self.ex.has['fetchOHLCV']:
                time.sleep(self.ex.rateLimit / 1000)  # time.sleep wants seconds
                ohlcv = self.ex.fetch_ohlcv(self.symbol, '1h',
                                            since=current_milli_time(hours),
                                            limit=1000)
        ohlcv_dataframe = ohlcv_dataframe.append(pd.DataFrame(ohlcv))
        ohlcv_dataframe['date'] = ohlcv_dataframe[0]
        ohlcv_dataframe['open'] = ohlcv_dataframe[1]
        ohlcv_dataframe['high'] = ohlcv_dataframe[2]
        ohlcv_dataframe['low'] = ohlcv_dataframe[3]
        ohlcv_dataframe['close'] = ohlcv_dataframe[4]
        ohlcv_dataframe['volume'] = ohlcv_dataframe[5]
        ohlcv_dataframe = ohlcv_dataframe.set_index('date')
        ohlcv_dataframe = ohlcv_dataframe.set_index(
            pd.to_datetime(ohlcv_dataframe.index, unit='ms').tz_localize('UTC'))
        ohlcv_dataframe.drop([0, 1, 2, 3, 4, 5], axis=1, inplace=True)
        if save_csv_data is True:
            ohlcv_dataframe.to_csv('data_since6months_freq1h' + self.symbol.split('/')[0] + '.csv')
            return ohlcv_dataframe
        else:
            return ohlcv_dataframe

if __name__ == "__main__":
    ex = BitfinexExchangeAcc("real")
    p = ex.ex.fetch_ticker("TESTBTC/TESTUSD")
    b = ex.ex.fetch_balance()
    # balance_pre_buy_order = ex.get_acc_balance()
    # print(f"balance_pre_buy_order: {balance_pre_buy_order}\n")
    # ex.create_market_buy_order(amount=0.001)
    # balance_post_buy_order = ex.get_acc_balance()
    # print(f"\nbalance_post_buy_order: {balance_post_buy_order}")

    #~~~~~~~~~

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