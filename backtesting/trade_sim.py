


class TradeSim:

    def __init__(self, data_cls):
        self.data_cls = data_cls
        self.data_src = self.data_cls.get_row()

    def get_tick(self):
        return next(self.data_src)




if __name__ == "__main__":
    from data_downloader import BTCUSDData
    data_src = BTCUSDData()
    trade_sim = TradeSim(data_src)




    # t1 = trade_sim.get_tick()
    # t2 = trade_sim.get_tick()
    # t3 = trade_sim.get_tick()


