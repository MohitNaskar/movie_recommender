# Movie Recommendation System
This is a movie recommendation system based on Machine Learning, Deep learning and Natural Language Processing.

At first we do the sentiment analysis of the users to extract the sentiment of the users per movie using NLP(natural language processing) and we check the accuracy of the sentiment analysis using Logistic Regression, Random Forest Classifier and Decision Tree. Then we proceed to develop the recommender system.

There are 5 different types of Recommendation Systems each having different roles.

Type 1: Property Based Recommendation System - which focuses on recommending movies based on the overview and genre of the movie. The genre and overview are vectorized and merged to apply the cosine_similarity algorithm to determine how similar the vectors are for the different movies. Then based on the similarity score we recommend the movies to the users.

Type 2: Popularity Based Recommendation System(Ratings) - which focuses on recommending movies based on the ratings provided by the users. First we create a pivot table for the users and ratings provided by them for each movie.
Then we find the correlation of each movie on the basis of the ratings provided by all the users and recommend it to the users based on the score.

Type 3: Popularity Based Recommendation System(Sentiment) - this system is same as the previous recommender system but in this system we replace the "ratings" provided by the users to "sentiment" of the users for each movie and take out the correlation between the movies based on the sentiments of the users and then recommend the movies to the users.

Type 4: User Collaborative Recommender System(Ratings) : this system focuses on the likeness of every user. Once the users have seen a few movies, we have the data of the users of what they like. Then we compute the User's(1) likeness on movies with the other users using Pearson's Correlations Algorithm. Pearson's Correlation helps us in finding how much two users are correlated on the basis of the data they provided. If the Pearson Correlation Score is above 0.75 we consider the "users" to be related. There we extract the movies seen by the users who are having correlation above 0.75 with user(1). We crosscheck if the User(1) has seen the movies extracted, if not seen we recommend the movie else skip. Here we take ratings provided by the users per movie into consideration.

Type 5: User Collaborative Recommender System(Ratings) : This system is almost the same as the previous system, just we take sentiment of users per movie into consideration.

The data used here is extracted by web scrappings using beautiful soup.

The application part and the deployement is done using Streamlit.
