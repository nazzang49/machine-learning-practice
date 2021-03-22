import pandas as pd

# sample csv file Titanic Survive
url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
# error_bad_lines False => skip bad lines
df = pd.read_csv(url, error_bad_lines=False)

print(df.head())
print(df.tail())
print(df.info())
print(df.columns)

# check NaN on each columns => Age 557
print(df.isnull().sum())
print(df.isna().sum())

# check survived count => 450
print(df[df['Survived'] == 1].count())

# check value ratio on each columns
print(df['PClass'].value_counts())



