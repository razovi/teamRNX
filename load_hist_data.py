import pandas as pd
import os
import gzip
from natsort import natsorted

class csv2DataFrame:
    Datas = []
    Data = pd.DataFrame({'A' : []})
    row = 0
    rows = 0
    # def __init__(self, path = "D:\\Work\\hackathon\\data\\hackathon-data\\public-trades-bitfinex-btc-usd\\"):
    def __init__(self, path = "/Users/Ksavier/Downloads/hackathon-data/public-trades-bitfinex-btc-usd/"):
        self.path = path;
        directory = os.fsdecode(path);
        dir_contents = os.listdir(directory)
        sorted_dir_conents = natsorted(dir_contents)
        # for file in os.listdir(directory):
        for file in sorted_dir_conents:
            print(f"file: {file}")
            if(file.endswith(".gz")):
                f = open(path + file[:-3], 'w');
                f.write(gzip.open(path + file, 'rb').read().decode("utf-8"))
                os.remove(path + file)
        # for file in os.listdir(directory):
        for file in sorted_dir_conents:
            if(file.endswith(".csv")):
                self.Datas.append(pd.read_csv (path + file));
        self.Data = pd.concat(self.Datas);
        self.Data = self.Data.rename(columns = {'date': 'timestamp'})
        self.rows = self.Data.shape[0];
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        if self.row < self.rows:
            self.row = self.row + 1
            return self.Data.iloc[self.row - 1]
        raise StopIteration()

if __name__ == "__main__":
    path = "/Users/Ksavier/Downloads/hackathon-data/public-trades-bitfinex-btc-usd/"
    dir = os.listdir(path)
    data_cls = csv2DataFrame()

