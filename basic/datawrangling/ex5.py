import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)

# unique
print(df['Sex'].unique())
print(df['Sex'].value_counts())

# delete specific col => use column name
print(df.drop(['Age', 'Sex'], axis=1).head())
print(df.drop(df.columns[0], axis=1).head())

# delete specific row => use boolean condition
print(df[df['Sex'] != 'male'].head())

# delete duplicate
print(df.drop_duplicates().head())
print(df.drop_duplicates(subset=['Sex']).head())
# last => leave last row
print(df.drop_duplicates(subset=['Sex'], keep='last').head())
