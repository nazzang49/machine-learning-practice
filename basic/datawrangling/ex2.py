import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)

# iloc => index by number
print(df.iloc[0])
# loc => index by string
print(df.loc[0])

# slice => select the range
print(df.iloc[:4])
print(df[:4])

# custom index
df = df.set_index(df['Name'])
print(df.head())

# choose specific columns and others deleted
df = df[['Name', 'Survived']]
print(df.head())
