import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)

# group by column
print(df.groupby('Sex').mean())
print(df.groupby('Sex').sum())
print(df.groupby('Sex').var())
print(df.groupby('Sex').std())
print(df.groupby('Sex').median())

print(df.groupby('Survived').count())
print(df.groupby('Survived')['Name'].count())
print(df.groupby('Survived')['Age'].count())

# group by Sex and Survived => Age count
print(df.groupby(['Sex', 'Survived'])['Age'].count())

# group by time track
import numpy as np

time_index = pd.date_range('06/07/2020', periods=100000, freq='30S')
df = pd.DataFrame(index=time_index)
print(df.head())

# range 1 ~ 10
df['Sales'] = np.random.randint(1, 10, 100000)

# sum group by 1week
print(df.resample('W').sum())
# sum group by 1hour
print(df.resample('H').sum())
print(df.resample('2W').mean())
print(df.resample('M', label='left').count())
# S => first day of the month
print(df.resample('MS').count())