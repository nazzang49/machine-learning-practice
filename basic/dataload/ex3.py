import pandas as pd

# read csv
url = "https://tinyurl.com/simulated-data"
df = pd.read_csv(url, sep=",")

print(df)
print("# HEAD")
print(df.head())
print("# TAIL")
print(df.tail())
print("# COLUMNS")
print(df.columns)
print("# INFO")
print(df.info())
print("# DESCRIBE")
print(df.describe())
print("# CHOOSE COLUMN")
print(df['integer'])
print(df.integer)
print("# INDEX")
print(df.index)

# read json
url = "https://tinyurl.com/simulated-json"
df = pd.read_json(url, orient="columns")

print(df)
print("# HEAD")
print(df.head())
print("# TAIL")
print(df.tail())
print("# COLUMNS")
print(df.columns)
print("# INFO")
print(df.info())
print("# DESCRIBE")
print(df.describe())
print("# CHOOSE COLUMN")
print(df['integer'])
print(df.integer)
print("# INDEX")
print(df.index)

# choose specific row
print(df.loc[50, ['integer', 'datetime']])
