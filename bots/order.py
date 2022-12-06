
class Order:

    def __init__(self, open_date, open_price, tp_pct, sl_pct, amount):
        self.open_date = open_date  # D_i
        self.open_price = open_price  # P_i
        self.tp_pct = tp_pct  # %TP
        self.sl_pct = sl_pct if sl_pct > 0 else abs(sl_pct)  # %SL
        self.amount = amount
        self.take_profit_price = (1 + self.tp_pct / 100) * self.open_price  # P_tp
        self.stop_loss_price = (1 - self.sl_pct / 100) * self.open_price  # P_sl
        self.return_pct = None
        self.current_return = None
        self.closed = False
        self.closed_date = None  # D_f
        self.closed_price = None  # P_f
        self.closed_return = None
        self.return_outcome = None
        self.current_value = None

    def __str__(self):
        msg = "\nOpen price [$]: {0}\n" \
              "Open date [yyyy-mm-dd]: {1}\n" \
              "Take-profit limit: {2}\n" \
              "Stop-loss limit: {3}\n" \
              "Number of shares: {4}\n" \
              "Current return [$]: {5}\n" \
              "Current return [%]: {6}\n" \
              "Close?: {7}\n" \
              "Current value [$]: {8}".format(self.open_price, self.open_date,
                                              self.tp_pct, self.stop_loss_price,
                                              self.amountself.num_shares, self.current_return,
                                              self.return_pct, self.closed, self.current_value)
        return msg

    def update_order(self, current_date, current_price):  # 1.2.1 and 1.4.1
        self.return_pct = ((current_price - self.open_price) / self.open_price) * 100
        self.current_return = (self.open_price * ((self.return_pct / 100) + 1)) * self.amount
        self.current_value = self.current_return + (self.open_price * self.amount)
        if current_price >= self.take_profit_price or current_price <= self.stop_loss_price:
            self.closed_date = current_date
            self.closed_price = current_price
            self.closed_return = current_price - self.open_price
            self.closed = True
            if current_price >= self.take_profit_price:
                self.return_outcome = 1
            elif current_price <= self.stop_loss_price:
                self.return_outcome = -1