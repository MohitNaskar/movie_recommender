import streamlit as st
import pickle
import pandas as pd

#functions
def recommend_property(movie):
    movie_index = movie_list_propertyBased[movie_list_propertyBased['MovieName'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:9]

    recommend_movies = []
    for i in movies_list:
        movie_name = movie_list_propertyBased.iloc[i[0]].MovieName
        recommend_movies.append(movie_list_propertyBased.iloc[i[0]].MovieName)
    return recommend_movies

def calculate_pearson_correlation(dfset1,dfset2):
        # Number of elements not checked margined to 3 for all
        #pearson correlation is only calculated between the set of items rated by both the users x and y 
        import math
        # mean of ratings of x and y
        mean_x = dfset1['AverageSentiment'].iloc[0] 
        mean_y = dfset2['AverageSentiment'].iloc[0]
      
        
        # substract mean of each element of both pair 
        diff_x = []
        # for loop to iterate through the column and return the ratings for user 1
        for i in range(dfset1.shape[0]):
                result = dfset1['sentiment'].iloc[i]-dfset1['AverageSentiment'].iloc[0]
                diff_x.append(result)
        diff_y =[]
        # for loop to iterate through the column and return the satings o
        for i in range(dfset2.shape[0]):
                result = dfset2['sentiment'].iloc[i]-dfset2['AverageSentiment'].iloc[0]
                diff_y.append(result)

        
        # sum of the product of each pair of element from the two array
        sum_product_diff = sum([diff_x[i] * diff_y[i] for i in range(2)])

        
        #calculating the dinominator 
        sumationuser1 = sum([diff_x[i]*diff_x[i] for i in range(2)])
        squarerootUser1 = math.sqrt(sumationuser1)


        sumationuser2 = sum([diff_y[i]*diff_y[i] for i in range(2)])
        squarerootUser2 = math.sqrt(sumationuser2)

        dino = squarerootUser1*squarerootUser2

        return sum_product_diff/dino

def calculate_pearson_correlationRatings(dfset1,dfset2):
        # Number of elements not checked margined to 3 for all
        #pearson correlation is only calculated between the set of items rated by both the users x and y 
        import math
        # mean of ratings of x and y
        mean_x = dfset1['AverageRatings'].iloc[0] 
        mean_y = dfset2['AverageRatings'].iloc[0]
      
        
        # substract mean of each element of both pair 
        diff_x = []
        # for loop to iterate through the column and return the ratings for user 1
        for i in range(dfset1.shape[0]):
                result = dfset1['Ratings'].iloc[i]-dfset1['AverageRatings'].iloc[0]
                diff_x.append(result)
        diff_y =[]
        # for loop to iterate through the column and return the satings o
        for i in range(dfset2.shape[0]):
                result = dfset2['Ratings'].iloc[i]-dfset2['AverageRatings'].iloc[0]
                diff_y.append(result)

        
        # sum of the product of each pair of element from the two array
        sum_product_diff = sum([diff_x[i] * diff_y[i] for i in range(2)])

        
        #calculating the dinominator 
        sumationuser1 = sum([diff_x[i]*diff_x[i] for i in range(2)])
        squarerootUser1 = math.sqrt(sumationuser1)


        sumationuser2 = sum([diff_y[i]*diff_y[i] for i in range(2)])
        squarerootUser2 = math.sqrt(sumationuser2)

        dino = squarerootUser1*squarerootUser2

        return sum_product_diff/dino


#loading the pkl files
movie_list_propertyBased = pickle.load(open('Movies.pkl','rb'))
movie_list_propertyBased = pd.DataFrame(movie_list_propertyBased)
similarity = pickle.load(open('similarity.pkl','rb'))
popularityRating = pickle.load(open('PopularityRatings.pkl','rb'))
PopularitySentiment = pickle.load(open('PopularitySentiment.pkl','rb'))


#changing the background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://plus.unsplash.com/premium_photo-1710500925162-93486c5a7abe?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
opacity: 1.0;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
#changing the title color
title_color = """
<style>
[data-testid="stText"] {
    font-size: 18px; /* Change the size as needed */
    font-weight: 550; /* Options: normal, bold, bolder, lighter, or numerical value (100-900) */
    color: black;
}

</style>"""
st.markdown(title_color,unsafe_allow_html=True)

#changing the subheading color to black
# selectboxColor = """
# <style>
# [data-testid="stMarkdownContainer"]{
#     font-size: 15px;
#     color:;
# }
# </style>
# """
# st.markdown(selectboxColor,unsafe_allow_html=True)
def remove_duplicates(strings):
    seen = set()
    result = []
    for string in strings:
        if string not in seen:
            seen.add(string)
            result.append(string)
    return result



#recommendation drop down menu
st.title("Movie Recommender System")
select_recommendation_type = st.selectbox(
    'Select Recommendation Type',
    ('Property Based','Popularity Based','User Based Collaborative'),
)
if (select_recommendation_type == 'Property Based'): 
    st.header("1. Property Based Recommendation",divider= 'rainbow')
    # Add a selectbox to the sidebar:
    select_movieName = st.selectbox(
        'Select Movie Name',
        movie_list_propertyBased['MovieName'].values
    )
    if st.button('Confirm Selection'):
    
        recommendations = recommend_property(select_movieName)
        unique_strings = remove_duplicates(recommendations)
        for i in unique_strings:
            st.text(i)
            
            

#for popularity based filering
if(select_recommendation_type == 'Popularity Based'):
    st.header("2. Popularity Based Recommendation",divider= 'rainbow')
    select_Popularity_Recommendation_Type= st.selectbox(
        'Select The type of Filtering',
        ('Popularity based Filtering (Rating)','Popularity based Filtering (Sentiment)')
    )
    # filtering using Ratings of users
    if(select_Popularity_Recommendation_Type== 'Popularity based Filtering (Rating)'):
        recommend_movies_PopularityRatings = []
        for col in popularityRating.columns:
            recommend_movies_PopularityRatings.append(col)

        select_movieName= st.selectbox(
            'select the movie name',
            recommend_movies_PopularityRatings
        )
        if st.button('Confirm Selection'):
            movie_watched = popularityRating[select_movieName]
            similarity_with_other_movies = popularityRating.corrwith(movie_watched)  # find correlation between "selected movie" and other movies
            similarity_with_other_movies = similarity_with_other_movies.sort_values(ascending=False)
            similarity_with_other_movies = similarity_with_other_movies.reset_index()
            similarity_with_other_movies = similarity_with_other_movies.iloc[0:5]
            similarity_with_other_movies = similarity_with_other_movies['MovieName'].tolist()
            for i in similarity_with_other_movies:
                st.text(i)
        
    
    #filtering using Sentiment of users
    if(select_Popularity_Recommendation_Type =='Popularity based Filtering (Sentiment)'):
        recommend_movies_PopularitySentiment = []
        for col in PopularitySentiment.columns:
            recommend_movies_PopularitySentiment.append(col)

        select_movieName = st.selectbox(
            'select a movie name',
            recommend_movies_PopularitySentiment
        )                
        if st.button('Confirm Selection'):
            movie_watched = PopularitySentiment[select_movieName]
            similarity_with_other_movies = PopularitySentiment.corrwith(movie_watched)  # find correlation between "selected movie" and other movies
            similarity_with_other_movies = similarity_with_other_movies.sort_values(ascending=False)
            similarity_with_other_movies = similarity_with_other_movies.reset_index()
            similarity_with_other_movies = similarity_with_other_movies.iloc[0:5]
            similarity_with_other_movies = similarity_with_other_movies['MovieName'].tolist()
            for i in similarity_with_other_movies:
                st.text(i)


df_averageSentiment = pickle.load(open('df_averageSentiment.pkl','rb'))
result1 = pickle.load(open('resultSentiment.pkl','rb'))
df_averageRatings = pickle.load(open('df_averageRatings.pkl','rb'))
resultRatings = pickle.load(open('resultRatings.pkl','rb'))

userlist = pickle.load(open('UserList.pkl','rb'))
userlist = userlist.sort_values(ascending = True)
#for user based collaborative filtering
if(select_recommendation_type == 'User Based Collaborative'):
    st.header("3. User Based Collaborative Recommendation",divider= 'rainbow')
    select_Collab_Recommendation_Type= st.selectbox(
        'Select The type of User Based Collaborative Filtering',
        ('Collaborative Filtering based on User Rating','Collaborative Filtering based on User Sentiment')
    )

    #collaborative filtering using User Ratings
    if(select_Collab_Recommendation_Type== 'Collaborative Filtering based on User Rating'):
        selectedUserID = st.selectbox(
            'Select the User ID',
            userlist
        )
        if st.button('Confirm Selection'):
            for i in range(len(df_averageRatings)):
                dfset1 = df_averageRatings[df_averageRatings['User_ID'] == selectedUserID]
                dfsetcheck = df_averageRatings.loc[df_averageRatings['User_ID'] == df_averageRatings['User_ID'].iloc[i],['MovieName','User_ID','Movie_ID','Ratings','AverageRatings']]
                resultRatings.loc[(i)] = [df_averageRatings['User_ID'].iloc[i],df_averageRatings['MovieName'].iloc[i],calculate_pearson_correlationRatings(dfset1,dfsetcheck)]
    
            resultSentiment = resultRatings.sort_values(by=['Coefficient'],ascending=False)
            #keeping the thresshold to be 0.75
            resultSentiment = resultSentiment[resultSentiment.Coefficient >=0.75]
            resultSentiment = resultSentiment.reset_index()
            movie_list = pd.DataFrame(resultSentiment['MovieName2']).reset_index()
            movie_seenU1 = pd.DataFrame(df_averageRatings[df_averageRatings['User_ID'] == selectedUserID]).reset_index()
            movie_seenU1 = pd.DataFrame(movie_seenU1['MovieName']).reset_index()
            movie_list = movie_list.drop_duplicates(ignore_index= True)
            movie_list = movie_list.drop(columns = 'index')
            movie_list = movie_list.reset_index()
            movie_list = movie_list.drop(columns = 'index')
            movie_list= movie_list.drop_duplicates()
            movie_seenU1 = movie_seenU1.drop(columns ='index')
            movie_seenU1 = movie_seenU1.drop_duplicates()
            series_A = movie_list['MovieName2']
            series_B = movie_seenU1['MovieName']

            # Find names in A but not in B
            names_in_A_not_in_B = series_A[~series_A.isin(series_B)]
            names_in_A_not_in_B = pd.DataFrame(names_in_A_not_in_B).reset_index()
            names_in_A_not_in_B = names_in_A_not_in_B.iloc[0:6]
            names_in_A_not_in_B = names_in_A_not_in_B.drop(columns='index')
            names_in_A_not_in_B = names_in_A_not_in_B['MovieName2'].to_list()
            for i in names_in_A_not_in_B:
                 st.text(i)


    #collaborative filtering using User Sentiment    
    if(select_Collab_Recommendation_Type== 'Collaborative Filtering based on User Sentiment'):
        selectedUserID = st.selectbox(
            'Select the User ID',
            userlist
        )
        if st.button('Confirm Selecion'):
            for i in range(len(df_averageSentiment)):
                dfset1 = df_averageSentiment[df_averageSentiment['User_ID'] == selectedUserID]
                dfsetcheck = df_averageSentiment.loc[df_averageSentiment['User_ID'] == df_averageSentiment['User_ID'].iloc[i],['MovieName','User_ID','Movie_ID','sentiment','AverageSentiment']]
                result1.loc[(i)] = [df_averageSentiment['User_ID'].iloc[i],df_averageSentiment['MovieName'].iloc[i],calculate_pearson_correlation(dfset1,dfsetcheck)]
                #remove the user set1 tomm
            result1 = result1.sort_values(by=['Coefficient'],ascending=False)
            #keeping the thresshold to be 0.75
            result1 = result1[result1.Coefficient >=0.75]
            result1 = result1.reset_index()
            movie_list = pd.DataFrame(result1['MovieName2']).reset_index()
            movie_seenU1 = pd.DataFrame(df_averageSentiment[df_averageSentiment['User_ID'] == selectedUserID]).reset_index()
            movie_seenU1 = pd.DataFrame(movie_seenU1['MovieName']).reset_index()
            movie_list = movie_list.drop_duplicates(ignore_index= True)
            movie_list = movie_list.drop(columns = 'index')
            movie_list = movie_list.reset_index()
            movie_list = movie_list.drop(columns = 'index')
            movie_list= movie_list.drop_duplicates()
            movie_seenU1 = movie_seenU1.drop(columns ='index')
            movie_seenU1 = movie_seenU1.drop_duplicates()
            series_A = movie_list['MovieName2']
            series_B = movie_seenU1['MovieName']

            # Find names in A but not in B
            names_in_A_not_in_B = series_A[~series_A.isin(series_B)]
            names_in_A_not_in_B = pd.DataFrame(names_in_A_not_in_B).reset_index()
            names_in_A_not_in_B = names_in_A_not_in_B.iloc[0:6]
            names_in_A_not_in_B = names_in_A_not_in_B.drop(columns='index')
            names_in_A_not_in_B = names_in_A_not_in_B['MovieName2'].to_list()
            for i in names_in_A_not_in_B:
                 st.text(i)





