from flask import Flask, render_template, jsonify, request
from transformers import pipeline
import requests
import boto3
import urllib.parse


app = Flask(__name__)

aws_access_key_id = 'AKIARHNZ4AF3AJUQP645'
aws_secret_access_key = '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'
region_name = 'us-east-1'
table_name = 'MovieList'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)
table = dynamodb.Table(table_name)

summarizer = pipeline("summarization")

#this is the homepage of everything else
@app.route('/')
def index():
    return render_template ('index.html')

def fetch_and_format_movies():
    formatted_movies = []  # Initialize the list to store formatted movies

    # Fetch movie data from DynamoDB
    response = requests.get('https://tibsep5k93.execute-api.us-east-1.amazonaws.com/default/GetMoviesLambda')
    
    # Check if the request was successful
    if response.status_code == 200:
        dynamodb_movies = response.json()

        # Construct formatted_movies list based on DynamoDB data
        for dynamodb_movie in dynamodb_movies:
            movie = {
                'MovieID': int(dynamodb_movie['MovieID']['S']),
                'title': dynamodb_movie['title']['S'],
                'releaseYear': int(dynamodb_movie['releaseYear']['S']),
                'genre': dynamodb_movie['genre']['S'],
                'coverimage' : dynamodb_movie['coverimage']['S']
            }
            formatted_movies.append(movie)
        # Sort the movies by MovieID
        formatted_movies = sorted(formatted_movies, key=lambda x: x['MovieID'])
        
    return formatted_movies

#this is the getting movies page332
@app.route('/getmovies')
def get_movies_json():
    formatted_movies = fetch_and_format_movies()
    return jsonify(formatted_movies) 

@app.route('/getmoviesbyyear')
def get_movies_by_year():
    formatted_movies = fetch_and_format_movies()
    user_provided_year = request.args.get('year', type=int)

    # Return a response based on the filtered movies
    if user_provided_year is None:
        return "You need to choose a year!", 404
    elif user_provided_year < 2000 or user_provided_year > 2010:
        return "Please Choose a movie year between 2000 and 2010!", 404
    filtered_movies = [movie for movie in formatted_movies if movie["releaseYear"] == user_provided_year]
    return jsonify (filtered_movies)
        
import requests
from flask import request, jsonify

@app.route('/getMovieSummaries')
def get_movie_summaries():
    # Extract movie title from request parameters
    movie_title = request.args.get('title')
    API_key = "cceac696bb8b6f4b878ec456452151b7"
    
    if not movie_title:
        return "You need to provide a movie title!", 400
        
    # Make API request to TMDb
    encoded_title = urllib.parse.quote(movie_title)
    url = f"https://api.themoviedb.org/3/search/movie?query={encoded_title}&include_adult=false&language=en-US&page=1&api_key={API_key}"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse response and extract summary
        data = response.json()
        if data['results']:
            summary = data['results'][0].get('overview', 'Summary not available')
            return jsonify({"title": movie_title, "summary": summary})
        else:
            return f"No movie found with the title '{movie_title}'", 404
    else:
        return "Failed to fetch movie summary", response.status_code

if __name__ == '__main__':  
    app.run(debug=True)


