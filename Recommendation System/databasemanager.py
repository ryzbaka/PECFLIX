import sqlite3
import sys
from genremapper import val_input
import pandas as pd
#remember to check dbname when connecting to database

def runsqlquery(database_name1,query):
    '''
    Docstring:
    '''
    print(f"sqlite3 query mode. Database:{database_name1} ('quit' to exit query mode)")
    try:
        check=query.find("SELECT")*query.find("Select")*query.find("select")
        if check==0:
            conn=sqlite3.connect(database_name1)
            cursor=conn.execute(query)
            for row in cursor:
                print(row)
        else:
            conn=sqlite3.connect(database_name1)
            conn.execute(query)
            conn.commit()
    except:
        print(sys.exc_info()," error.")
#1. Convert .CSV files to pandas dataframes
#2. Add respective genre code for a mapping
#3. Convert DataFrame into SQLite Database
reviews=pd.read_csv("movie_ratings_data_set.csv")
movies=pd.read_csv("movies.csv",index_col="movie_id")
conn=sqlite3.connect("maindb")
moviesdb=movies.to_sql("movies",conn)
reviewsdb=reviews.to_sql("reviews",conn)