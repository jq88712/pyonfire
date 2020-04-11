import sqlite3
import pandas as pd

conn = sqlite3.connect('database_pyfire.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

#Reading data into memory
features = pd.read_csv('retaildataset/features.csv')
sales = pd.read_csv('retaildataset/sales.csv')
stores = pd.read_csv('retaildataset/stores.csv')

#Loading data into database
features.to_sql('Features', conn, if_exists='fail', index = True)
sales.to_sql('Sales', conn, if_exists='fail', index = True)
stores.to_sql('Stores', conn, if_exists='fail', index = True)

