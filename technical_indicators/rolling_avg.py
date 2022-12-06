import collections



class RollingAvg:
    """
    DOESN'T ACTUALLY WORK PROPERLY OR IS A TERRIBLY POOR IMPLEMENTATION
    """
    def __init__(self, w):
        self.dq = collections.deque()
        self.avg = 0
        self.WINDOW = w

    def add(self, x):
        self.dq.append(x)
        self.avg += x
        if len(self.dq) > self.WINDOW:
            self.avg -= self.dq.popleft()



