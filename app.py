import streamlit as st
import pandas as pd
import pickle
import requests

movie_list=pickle.load(open("movie_dict.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies=pd.DataFrame(movie_list)



def poster_fetch(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5266fe5150c60b2f17c9a4053cef800a&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']




def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:7]

    recommend_movies=[]
    recommend_movies_poster=[]

    for i in movie_list:
        movie_id=movies.iloc[i[0]].id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetching poster with API
        recommend_movies_poster.append(poster_fetch(movie_id))

    return recommend_movies,recommend_movies_poster

    


st.title("Movie Recommender System")

movie_selected = st.selectbox(
    "Select Movie Name",
    movies['title'].values )

if st.button("Recommend"):
    names,posters=recommend(movie_selected)



col1, col2, col3, col4, col5, col6 = st.columns(6, gap="medium")
with col1:
   st.text(names[0])
   st.image(posters[0])

with col2:
   st.text(names[1])
   st.image(posters[1])

with col3:
   st.text(names[2])
   st.image(posters[2])

with col4:
   st.text(names[3])
   st.image(posters[3])

with col5:
   st.text(names[4])
   st.image(posters[4])

with col6:
   st.text(names[5])
   st.image(posters[5])
