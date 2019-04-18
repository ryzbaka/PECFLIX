import numpy as np
import pandas as pd
import matrix_factorization_utilities

#load user ratings
df=pd.read_csv("movie_ratings_data_set.csv")

#load movie titles set movie_id as the index
movies_df=pd.read_csv("movies.csv",index_col="movie_id")

#convery yhe running list of user ratings into a matrix
ratings_df=pd.pivot_table(df,index="user_id",columns="movie_id")

#apply matrix factorization to find the latent features
U,M=matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.as_matrix(),num_features=15,regularization_amount=1.0)
# swap the rows and columns fo product_features just so that it's easier to work with
M=np.transpose(M)
#choose a movie to find similar movies to movie #5
movie_id=5
#get movie #1's name and genre
movie_information=movies_df.loc[5]
print("We are finding movies similar to this movie:")
print("movie title: {}".format(movie_information.title))
print("genre:{}".format(movie_information.genre))

#get movie #1's attributes
current_movie_features=M[movie_id-1]# -1 because of different index values
print("The attributes for this movie are:")
print(current_movie_features)

#main logic for finding similar products

#1. SUbtract the current movie's features from evey other movie's features
difference=M-current_movie_features
#2. Take the absolute value of the difference to get rid of any negative values
absolute_difference=np.abs(difference)
#3. Each movie has 15 different features.Sum those 15 features to get a feaure difference score for each movie
total_difference=np.sum(absolute_difference,axis=1)
#4. Create a new column in the movielist with the difference score with each movie
movies_df['difference_score']=total_difference
#5. Sort the movie list by difference score, from least difference from most different
sorted_movie_list=movies_df.sort_values('difference_score')
#6. Display 5 most similar movies
print("The 5 most similar movies are:")
print(sorted_movie_list[['title','difference_score']][0:5])