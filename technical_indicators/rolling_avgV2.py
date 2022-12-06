import collections

class RollingAvgV2:
    """
    !!!TO BE USE INSTEAD OF RollingAvg!!!
    Moving Avg. <=> Rolling/Moving Mean
    Creates a successive series of `window` sized subsets/arrays
    of averages from the full deque (self.dq) data set.
    https://goodcalculators.com/simple-moving-average-calculator/
    """
    def __init__(self, window):
        """
        :param window: int of the rolling avg window size
        E.g. (fast_wndw) w=10, (short_wndw_ w=50
        """
        self.window = window
        self.dq = collections.deque()
        self.sum = 0
        self.avgs = []
        self.cur_avg = None

    def add(self, x):
        """
        1) Compute
        2) Add new val, x, on the rhs of the deque, self.dq


        Given a seq of ints & a window size, compute the
        moving avg of all ints within the sliding window.
        :param x:
        :return:
        """
        self.sum = self.sum + x
        self.dq.append(x)
        # Check if deque len is >= than the window size
        if len(self.dq) >= self.window:
            self.cur_avg = self.sum/self.window
            # self.sum = self.sum - self.dq.popleft()
            self.avgs.append(self.cur_avg)
            lhs_popped_item = self.dq.popleft()
            self.sum = self.sum - lhs_popped_item
