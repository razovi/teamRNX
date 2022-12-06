from technical_indicators import rolling_avgV2

# xs = [2,4,6,8,12,14,16,18,20]
# window_size = 6.4,8.8,11.2,13.6,16
moving_avgs = [6.4, 8.8, 11.2, 13.6, 16]

window_size = 5
xs = [2, 4, 6, 8, 12, 14, 16, 18, 20]

rolling_avg = rolling_avgV2.RollingAvg(window=window_size)

for x in xs:
    rolling_avg.add(x)

print(f"rolling_avg.dq: {rolling_avg.dq}")
print(f"rolling_avg.sum: {rolling_avg.sum}")
print(f"rolling_avg.avgs: {rolling_avg.avgs}")

# 2 + 0 = 2
# ...
# 4 + 2 = 6
# ...
# 6 + 6 = 12
# ...
# 8 + 12 = 20
# ...
# 12 + 20 = 32
# [2, 4, 6, 8, 12]
# self.tot = 32
# self.avg = self.tot/self.window = 6.4


# [4, 6, 8, 12]

# 14 + 32 = 32
# [4, 6, 8, 12, 14]
# .popleft() -> [4, 6, 8, 12, 14]
# self.tot = 32
# self.avg = self.tot/self.window = 6.4







