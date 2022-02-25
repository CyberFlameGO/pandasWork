# -*- coding: utf-8 -*-
"""
petri's dish of pandas
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./transcript_dates.txt', header = None)
df.columns = ['date']
df.date = df.date.astype('datetime64[ns]')
df['date2'] = pd.to_datetime(df['date'])
plt.plot(df['date2'], df['date'])
plt.show()
