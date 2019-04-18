import pandas as pd
import os
import webbrowser

data_table=pd.read_csv("movie_ratings_data_set.csv")
#converting the pandas dataframe to an html file
#for easy viewing
html=data_table[0:100].to_html()
#writing data into a file named "MOVDATA.html"
with open("MOVDATA.html","w") as f:
    f.write(html)
#opening using web browser
full_filename=os.path.abspath("MOVDATA.html")
webbrowser.open("file://{}".format(full_filename))
#webbrowser.open("https://www.google.com")