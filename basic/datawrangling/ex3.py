import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)

# specific condition => if
print(df[df['Sex'] == 'female'].head(2))
# and
print(df[(df['Sex'] == 'female') & (df['Age'] >= 60)].head(2))
# or
print(df[(df['Sex'] == 'female') | (df['Age'] >= 60)].head(2))

# replace => left -> right (multiple possible)
df['Sex'] = df['Sex'].replace(['female', 'male'], ['Woman', 'Man'])
print(df['Sex'].head())
print(df.replace(r'1st', 'First', regex=True).head(2))
print(df.replace({'Woman': 0, 'Man': 1}).head())

# rename columns
print(df.rename(columns={'Sex': 'Gender', 'PClass': 'Level'}).head())
# to lower case
print(df.rename(str.lower, axis='columns').head())