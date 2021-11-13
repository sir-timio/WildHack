import pandas as pd
from itertools import combinations
import seaborn as sns
import matplotlib.pyplot as plt


path_to_data = '../data/preprocess.csv'
data = pd.read_csv(path_to_data)
data.utc_event_time = pd.to_datetime(data.utc_event_time)
data.utc_event_date = pd.to_datetime(data.utc_event_date)

def get_dict_conversions(df):

    def func(df):
        series = df.event_action.value_counts()
        return pd.Series(
            {f'{i}/{j}': series.loc[i] / series.loc[j] 
             for i, j in combinations(series.index.unique(), 2)},
            name='count')

    actions_count = df.groupby('utc_event_date').apply(func)
    actions_count = actions_count.reset_index().rename(columns={'level_1': 'conversion'}).set_index('utc_event_date')
    for i, df in actions_count.groupby('conversion'):
        yield (i, df['count'].to_dict())

actions_count = list(get_dict_conversions(data))

plt.figure(figsize=(14, 5))
g = sns.lineplot(data=pd.Series(actions_count[0][1]))
g.tick_params(rotation=90)
plt.tight_layout()
plt.show()
