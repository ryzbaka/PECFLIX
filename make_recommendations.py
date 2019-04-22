import numpy as np
import pandas as pd
import sqlite3
import matrix_factorization_utilities

def recommendations(user_id_to_search):
    

    newuser=[]
    conner=sqlite3.connect("db.sqlite3")
    cursor=conner.execute("select id from auth_user where id not in (select user_id_id as id from recommendation_system_reviews);")
    for row in cursor:
        newuser.append(row[0])
    
    if user_id_to_search in newuser:
        return 0,0



    conn=sqlite3.connect("db.sqlite3")
    #load user ratings
    raw_dataset_df=pd.read_sql("select user_id_id as userid,movie_id_id as movieid,rating from recommendation_system_reviews;",conn)
    #convert user ratings into a matrix
    ratings_df=pd.pivot_table(raw_dataset_df,index='userid',columns='movieid',aggfunc=np.max)
    #load movie titles
    movies_df=pd.read_sql("select * from blog_movie;",conn,index_col="id")

    #Apply Matrix factorization to find the latent features
    U,M=matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.as_matrix(),num_features=15,regularization_amount=0.1)
    #find all predicted ratings
    predicted_ratings=np.matmul(U,M)
    #print("Enter a user id to get recommendations")
    #user_id_to_search=int(input())
    #print(f"Movies previously reviewed by user {user_id_to_search}")
    reviewed_movies_df=raw_dataset_df[raw_dataset_df['userid']==user_id_to_search]
    reviewed_movies_df=reviewed_movies_df.join(movies_df,on="movieid")

    reviewed=list(reviewed_movies_df['movieid'])
    movielist=list(movies_df.index)

    #Movies that the user hasn't watched
    recommended_df=movies_df[movies_df.index.isin(reviewed) == False]

    #Finding Predicted Ratings for user
    if user_id_to_search==1:
        user_ratings=predicted_ratings[0]
    else:
        user_ratings=predicted_ratings[user_id_to_search-6]
    #add the user's rating to the movies dataframe and then sort the dataframe in descending order of predicted ratings
    movies_df['ratings']=user_ratings
    reviewed=list(reviewed_movies_df['movieid'])
    recommended_df=movies_df[movies_df.index.isin(reviewed) == False]
    recommended_df=recommended_df.sort_values(by=['ratings'],ascending=False)
    movierecommendation=list(recommended_df["content"].head(2))


    return list(reviewed_movies_df['title']),movierecommendation