from take_profit_stop_loss_labeller import PositionSideLabeler
from data_downloader import BTCUSDData
from technical_indicators import sma_crossover


data_cls = BTCUSDData("1d")
data = data_cls.data



expiration_days_limit = None
take_profit_pct = 10
stop_loss_pct = 10
position_labels = PositionSideLabeler(data["Close"],
                                      take_profit_pct=take_profit_pct,
                                      stop_loss_pct=stop_loss_pct,
                                      expiration_days_limit=expiration_days_limit)


position_labels.start_labeller()
label_results_df = position_labels.get_results_df()
sides = position_labels.get_side_labels_series()
# sides = sides.shift(-1)
sides = sides.dropna()
days_elapsed_average = int(label_results_df["DaysElapsed"].describe()[1])
days_elapsed_top_25_pct_q_avg = int(label_results_df["DaysElapsed"].describe()[4])
days_elapsed_top_50_pct_q_avg = int(label_results_df["DaysElapsed"].describe()[5])
days_elapsed_top_75_pct_q_avg = int(label_results_df["DaysElapsed"].describe()[6])
days_elapsed_max = int(label_results_df["DaysElapsed"].describe()[7])



sma_crossover_parameters = {"short_term_period":days_elapsed_top_25_pct_q_avg,
                           "long_term_period":days_elapsed_top_75_pct_q_avg,
                           "threshold":1}

sma_crossover_signal = sma_crossover.SMACrossOver(data["Close"],
                                                 sma_crossover_parameters["short_term_period"],
                                                 sma_crossover_parameters["long_term_period"],
                                                 sma_crossover_parameters["threshold"])

sma_crossover_int_labels = sma_crossover_signal.get_sma_crossover_int_labels()

print(sma_crossover_int_labels)
