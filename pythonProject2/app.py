import pickle
import requests
import pandas as pd
import streamlit as st
import pickle as pkl
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommend_movies =[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from Api
        recommend_movies.append(movies.iloc[i[0]].title)
        return recommend_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity= pickle.load(open('similarity.pkl','rb'))
option= st.title ('Movie recommender System')
selected_movie_name = st.selectbox('How would you like to be connected',
movies['title'].values)
if st.button('Recommend'):
   recommendations= recommend(selected_movie_name)
   for i in recommendations:
    st.write(i)