import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)
print(len(df))

# add column
array = np.random.randint(1, 10, 1313)
custom_df = pd.DataFrame(array, columns=['Number'])
print(len(custom_df))
print(custom_df.head())
df['Number'] = custom_df
print(df.head())

# concat
df1 = pd.DataFrame({'name': ['park', 'ahn', 'na'], 'age': ['20', '25', '30']})
df2 = pd.DataFrame({'name': ['kim', 'jo', 'moon'], 'age': ['24', '23', '33']})
# row
print(pd.concat([df1, df2], axis=0))
# col
print(pd.concat([df1, df2], axis=1))

# merge = join
df1 = pd.DataFrame({'name': ['park', 'ahn', 'na'], 'age': ['20', '25', '30']})
df2 = pd.DataFrame({'name': ['na', 'jo', 'moon'], 'sex': ['female', 'male', 'male']})
# inner join
print(pd.merge(df1, df2, on='name'))
# full outer join
print(pd.merge(df1, df2, on='name', how='outer'))
# left join
print(pd.merge(df1, df2, on='name', how='left'))
# right join
print(pd.merge(df1, df2, on='name', how='right'))
print(pd.merge(df1, df2, left_on='name', right_on='sex', how='outer'))