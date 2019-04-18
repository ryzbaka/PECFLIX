import pandas as pd
import os
import webbrowser
data_table=pd.read_csv("movies.csv",index_col="movie_id")
html=data_table.to_html()

with open("movie_data.html","w") as f:
    f.write(html)

full_filename=os.path.abspath("movie_data.html")
webbrowser.open("file://{}".format(full_filename))
