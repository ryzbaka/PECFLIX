import pandas as pd
import sqlite3
import numpy as np
from . import matrix_factorization_utilities

conn=sqlite3.connect("db.sqlite3")
#load user ratings
raw_dataset_df=pd.read_sql("select * from reviews;",conn)
#convert user ratings into a matrix
ratings_df=pd.pivot_table(raw_dataset_df,index='userid',columns='movieid',aggfunc=np.max)
#load movie titles
movies_df=pd.read_sql("select * from blog_movie;",conn,index_col="id")

#Apply Matrix factorization to find the latent features
U,M=matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.as_matrix(),num_features=15,regularization_amount=0.1)
#find al predicted ratings
predicted_ratings=np.matmul(U,M)

print("Enter a user id to get recommendations")
user_id_to_search=int(input())
print(f"Movies previously reviewed by user {user_id_to_search}")
reviewed_movies_df=raw_dataset_df[raw_dataset_df['userid']==user_id_to_search]
reviewed_movies_df=reviewed_movies_df.join(movies_df,on="movieid")

print(reviewed_movies_df[['title','rating']])

input("Press enter to continue")

print("Movies we will recommend:")
#It's working till here, fix the user ids.
#update:I added 33-36 line
'''
if user_id_to_search==1:
    user_ratings=predicted_ratings[0]
else:
    user_ratings=predicted_ratings[user_id_to_search-6]
movies_df['rating']=user_ratings

already_reviewed=reviewed_movies_df['movieid']
recommended_df=movies_df[movies_df.index.isin(already_reviewed) == False]
recommended_df=recommended_df.sort_values(by=['rating'],ascending=False)

print(recommended_df[['title','rating']].head(5))
'''
print("Movies:")
print(movies_df)
print("Already Viewed:")
print(reviewed_movies_df)
already_reviewed=reviewed_movies_df['movieid']
#recommended_df=movies_df[movies_df.movieid.isin(already_reviewed) == False]
#print("Reviewed movies ids:")
#print(list(already_reviewed))
#recommended_df=movies_df[movies_df['id'] not in list(already_reviewed)]
#print("Recommended Movies:")
#print(recommended_df)
'''
if user_id_to_search==1:
    user_ratings=predicted_ratings[0]
else:
    user_rating=predicted_ratings[user_id_to_search-1]
'''
#Dude just run the dataframes in a jupyter notebook to fix the indexing issues in the database
# make the program work to a point where we can see predicted ratings for a user along with the title of the movie

#after that figure out a way to get the actual user id as an input into the program and make a separate app for this