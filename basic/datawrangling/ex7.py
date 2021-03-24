import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)

# check values by each columns
for name in df['Name'][:2]:
    print(name)

# apply => custom function
def test(x):
    return len(x)

print(df['Name'].apply(test))
df['Name'] = df['Name'].apply(test)
print(df.head())
print(df['Age'].apply(lambda x: x < 50))

# map
print(df['Survived'].map({1: 'Live', 0: 'Dead'}))

# apply to group => groupby should be used with statistic functions ex) sum, var, std
print(df.groupby('Sex').count())
print(df.groupby('Sex').apply(lambda x: x.count()))