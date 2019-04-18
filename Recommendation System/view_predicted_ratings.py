import pandas as pd
import numpy as np
import os
import webbrowser

predicted_ratings=pd.read_csv("predicted_ratings.csv")
html=predicted_ratings.to_html(na_rep="")

with open("predicted_ratings.html","w") as f:
    f.write(html)
full_filename=os.path.abspath("predicted_ratings.html")
webbrowser.open("file://{}".format(full_filename))
