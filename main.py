import pandas as pd

df = pd.read_csv('./transcript_dates.txt', delimiter = "\n", header = None)
df.columns = ['date']
df.date = pd.to_datetime(df.date)
print(df)
