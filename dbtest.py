'''
python3 function for running sqlite3 queries
'''
import sqlite3

#remember to check dbname when connecting to database

def runsqlquery(database_name1):
    '''
    Docstring:
    Enter query mode in sqlite3
    runsqlquery(database_name)
    >query
    '''
    query="placeholder"
    print(f"sqlite3 query mode. Database:{database_name1} ('quit' to exit query mode)")
    while query!="quit":
        query=input('>')
        if query=="QUIT" or query=="quit":
            print("Exiting query mode...")
            break
            #try getting rid of break
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


#<module> begins
db="db.sqlite3"
runsqlquery(db)
