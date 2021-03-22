import pandas as pd
from sqlalchemy import create_engine

# read from SQL

# db connect
engine = create_engine("mysql://root:admin@localhost:3307/shop")

# load data by native query
df = pd.read_sql_query("SELECT * FROM member", engine)

print(df)
