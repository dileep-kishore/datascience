import pandas as pd

DATAPATH = '../data/stack-overflow-2018-developer-survey/survey_results_public.csv'

data = pd.read_csv(DATAPATH, index_col=0)

dev_who_open_source = data[data['OpenSource'] == 'Yes']['DevType'].unique()

print(dev_who_open_source)
