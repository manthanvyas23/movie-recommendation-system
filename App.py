import streamlit as st
import pandas as pd
import pickle
import joblib

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = joblib.load('similarity.joblib')

st.title('_Movie Recommendation System_ 🎬')

selected_movie_name = st.selectbox(
    'Select a Movie',
    movies['title'].values,
    index = None,
    placeholder = 'Select a movie to get similar recommendations')

if st.button('Get Recommendations', type = 'primary', icon = '🔍', icon_position = 'right'):
    if selected_movie_name is None:
        st.warning('Please choose a movie to see recommendations', icon = '⚠️')
    else:
        recommendations = recommend(selected_movie_name)
        for i in recommendations:
            st.write(i)