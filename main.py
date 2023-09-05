import psycopg2
from sqlalchemy import create_engine
import pandas as pd

df = pd.DataFrame(
    {'氏名':['高橋','伊藤','鈴木','山本'],
     '出席番号':['a001','a002','a005','a006'],
     '国語':[5,6,7,8]
     }
).set_index('氏名')

connection_config = {
    'user': 'postgres',
    'password': 'password0209',
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'postgres'
}

engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**connection_config))

#df.to_sql('test_table01', con = engine, if_exists='replace')

"""
df = pd.read_csv("./test_table.csv")
df = df.set_index("ID")
df.to_sql('test_table_csv', con = engine, if_exists='replace')
"""

df = pd.read_sql(sql="select * from test_table_csv", con=engine)
print(df)
