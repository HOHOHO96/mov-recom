import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask , render_template,request
app=Flask(__name__)

@app.route('/')
def index0():
    return render_template('index0.html')

@app.route('/moviename')
def moviename():
    return render_template('moviename.html')

@app.route('/moviegenre')
def moviegenre():
    return render_template('moviegenre.html')

@app.route('/director')
def director():
    return render_template('director.html')

@app.route('/name',methods=["GET","POST"])
def name():
    if request.method == "POST":
       movies_data = pd.read_csv(r"C:\Users\sujit\Downloads\movies.csv")
       selected_features = ['genres','keywords','tagline','cast','director']
       for feature in selected_features:
           movies_data[feature] = movies_data[feature].fillna('')
       combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
       vectorizer = TfidfVectorizer()
       feature_vectors = vectorizer.fit_transform(combined_features)
       similarity = cosine_similarity(feature_vectors)
       list_of_all_titles = movies_data['title'].tolist()
       # getting input with name = fname in HTML form
       movie_name = request.form.get("movie_name")
       # getting input with name = lname in HTML form
       suggestions = request.form.get("suggestions")
       j=int(suggestions)
       list_of_all_titles = movies_data['title'].tolist()
       find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
       close_match = find_close_match[0]
       index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
       similarity_score = list(enumerate(similarity[index_of_the_movie]))
       sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
       print('Movies suggested for you based on the movie name : \n')
       i = 1
       a=[]
       b="!!--- Movie Suggestions based on movie name ---!! "
       for movie in sorted_similar_movies:
         index = movie[0]
         title_from_index = movies_data[movies_data.index==index]['title'].values[0]
         if (i<=j):
           print(i, '.',title_from_index)
           b+="\n" + str(i) + "." + "  " + title_from_index + " ---- "
           a.append(title_from_index)
           print(b)
           i+=1
           
       return b
    return render_template("form.html")

@app.route('/genre',methods=["GET","POST"])
def genre():
    if request.method == "POST":
       movies_data = pd.read_csv(r"C:\Users\sujit\Downloads\movies.csv")
       selected_features = ['genres','keywords','tagline','cast','director']
       for feature in selected_features:
           movies_data[feature] = movies_data[feature].fillna('')
       combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
       vectorizer = TfidfVectorizer()
       feature_vectors = vectorizer.fit_transform(combined_features)
       similarity = cosine_similarity(feature_vectors)
       list_of_all_titles = movies_data['genres'].tolist()
       # getting input with name = fname in HTML form
       movie_genre = request.form.get("movie_genre")
       # getting input with name = lname in HTML form
       suggestions = request.form.get("suggestions")
       j=int(suggestions)
       list_of_all_titles = movies_data['genres'].tolist()
       find_close_match = difflib.get_close_matches(movie_genre, list_of_all_titles)
       close_match = find_close_match[0]
       index_of_the_movie = movies_data[movies_data.genres == close_match]['index'].values[0]
       similarity_score = list(enumerate(similarity[index_of_the_movie]))
       sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
       print('Movies suggested for you based on the movie genre : \n')
       i = 1
       a=[]
       b="!!--- Movie Suggestions based on movie genre ---!! "
       for movie in sorted_similar_movies:
         index = movie[0]
         title_from_index = movies_data[movies_data.index==index]['title'].values[0]
         if (i<=j):
           print(i, '.',title_from_index)
           b+="\n" + str(i) + "." + "  " + title_from_index + " ---- "
           a.append(title_from_index)
           print(b)
           i+=1
           
       return b
    return render_template("form.html")

@app.route('/dir',methods=["GET","POST"])
def dir():
    if request.method == "POST":
       movies_data = pd.read_csv(r"C:\Users\sujit\Downloads\movies.csv")
       selected_features = ['genres','keywords','tagline','cast','director']
       for feature in selected_features:
           movies_data[feature] = movies_data[feature].fillna('')
       combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
       vectorizer = TfidfVectorizer()
       feature_vectors = vectorizer.fit_transform(combined_features)
       similarity = cosine_similarity(feature_vectors)
       list_of_all_titles = movies_data['director'].tolist()
       # getting input with name = fname in HTML form
       movie_name = request.form.get("director")
       # getting input with name = lname in HTML form
       suggestions = request.form.get("suggestions")
       j=int(suggestions)
       list_of_all_titles = movies_data['director'].tolist()
       find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
       close_match = find_close_match[0]
       index_of_the_movie = movies_data[movies_data.director == close_match]['index'].values[0]
       similarity_score = list(enumerate(similarity[index_of_the_movie]))
       sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
       print('Movies suggested for you based on the director of movie : \n')
       i = 1
       a=[]
       b="!!--- Movie Suggestions based on movie name ---!! "
       for movie in sorted_similar_movies:
         index = movie[0]
         title_from_index = movies_data[movies_data.index==index]['title'].values[0]
         if (i<=j):
           print(i, '.',title_from_index)
           b+="\n" + str(i) + "." + "  " + title_from_index + " ---- "
           a.append(title_from_index)
           print(b)
           i+=1
           
       return b
    return render_template("form.html")

if __name__=='__main__':
    app.run()