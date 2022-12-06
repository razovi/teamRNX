from technical_indicators import rsi_mini
import pandas as pd



class RSIBot:

    def __init__(self, portfolio_init_val=50000, order_size_pct_wrt_portfolio=2, rsi_time_period=14):
        self.portfolio_val = portfolio_init_val
        self.order_size_pct_wrt_portfolio = order_size_pct_wrt_portfolio
        self.rsi_time_period = rsi_time_period
        self.ticks = []
        self.open_order = None
        self.orders_cnt = 0


    def run_tick(self, tick):
        self.ticks.append(tick)
        if len(self.ticks) <= self.rsi_time_period:
            pass
        else:
            past_rsi_time_period_data = pd.DataFrame(self.ticks[-14:])
            # print(past_rsi_time_period_data)
            rsi = rsi_mini.get_rsi_values(past_rsi_time_period_data["Close"], time_period=self.rsi_time_period)
            rsi_sig = rsi_mini.get_rsi_int_labels_ts(rsi)
            # tick_rsi_sig = rsi_sig.dropna()
            tick_rsi_sig = rsi_sig
            print(rsi)
            # print(tick_rsi_sig)
            if tick_rsi_sig.values[-1] == 1:
                if self.open_order is None:
                    self.orders_cnt += 1
                    amount = past_rsi_time_period_data.iloc[-1]["Close"] * (self.portfolio_val * (self.order_size_pct_wrt_portfolio/100))
                    self.order = {"price":past_rsi_time_period_data.iloc[-1]["Close"], "amount":amount}
            elif tick_rsi_sig.values[-1] == -1:
                if self.open_order is not None:
                    self.portfolio_val = self.portfolio_val
                print("sell")
            else:
                print("hold")
            # tick_rsi_sig = rsi_sig








