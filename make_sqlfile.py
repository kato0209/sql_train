import sqlite3
import pandas as pd

con = sqlite3.connect("./10_test_database_02.db")
df = pd.read_sql(sql="select * from test_table", con=con)
df.to_csv("./test_table.csv", index=False, encoding="utf-8")

