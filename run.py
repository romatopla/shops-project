from pgfb import PGDatabase
import pandas as pd 
import os 
import configparser
import shutil

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname,'config.ini'))

DATABASE_CREDS = config['Database']

database = PGDatabase(
    host=DATABASE_CREDS['HOST'],
    database=DATABASE_CREDS['DATABASE'],
    user=DATABASE_CREDS['USER'],
    password=DATABASE_CREDS['PASSWORD']
)

data_df = pd.DataFrame()
for file in os.listdir(os.path.join(dirname,'data')):
    file_path = os.path.join(dirname,'data',file)
    if os.path.exists(file_path):
        curr_df = pd.read_csv(file_path)
        data_df = pd.concat([data_df,curr_df],ignore_index=True)
        os.unlink(file_path)

for i,row in data_df.iterrows():
    query = f"insert into sales values ('{row['doc_id']}','{row['shop_num']}','{row['cash_num']}','{row['item']}','{row['category']}','{row['amount']}','{row['price']}','{row['discount']}')"
    database.post(query)
