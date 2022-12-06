import yfinance as yf


class BTCUSDData:

    def __init__(self, res="1d", data=None):
        self.res = res
        self.ticker = yf.Ticker("BTC-USD")
        # “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
        self._data = self.ticker.history(period="max", interval=self.res)

    @property
    def data(self):
        if self._data is None:
            self._data = self.ticker.history(period="max", interval=self.res)
            return self._data
        else:
            self._data

    def get_row(self):
        for idx_i in self._data.index.tolist():
            yield self._data.loc[idx_i]


if __name__ == "__main__":
    data_cls = BTCUSDData("1d")
    data = data_cls.data
    # data_cls = BTCUSDData("1m")
    data_src = data_cls.get_row()
    print(next(data_src))
    print(next(data_src))

