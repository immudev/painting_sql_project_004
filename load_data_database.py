# import pandas and sqlalchemy for load dataset in portgresql
import pandas as pd
from sqlalchemy import create_engine



# creating SQL Alchemy engine object to connect severs
conn_string = 'postgresql://postgres:Admin@localhost/painting_p004'
db = create_engine(conn_string)


# Initializing connection to the databse
conn = db.connect()

# list the csv file to load in the database
files = ['canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

# create a for lop to rreperate porcess untile the files end 
for file in files:

    # load the dataframe as df into the database 
    df = pd.read_csv(f"C:\\Users\\smohe\\OneDrive\\Desktop\\SQL\\projects\\project_004\\dataset\\{file}.csv")
    # the 'if_exists' can be 'fail' 'replace' or 'append' if exists is check the talble already exists or not if exists this step replace a table
    df.to_sql(file, con=conn, if_exists='replace', index=False)


# after click run button its take few sec to load dataset in database 
# after conplete the process you go to the databse refresh and check your databse 
