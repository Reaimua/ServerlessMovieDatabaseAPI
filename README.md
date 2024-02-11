# ServerlessMovieAPI

## Overview 
This project focuses on developing a serverless movie API using Python within the context of the 6 Month Cloud Study Plan. The goal is to gain practical experience in building cloud-native applications leveraging serverless architecture and AWS services. The project aims to simplify movie data access using serverless functions, with a setup including a NoSQL database, cloud storage, and serverless functions.

## Introduction
With this project, you can efficiently store and retrieve movie details using serverless functions. The API offers three functions: GetMovies, returning a JSON list of movies with cover image URLs; GetMoviesByYear, retrieving movies by year; and GetMovieSummary, fetching movie summaries from The Movie Database (TMDb). This approach simplifies movie data access and provides a seamless experience for users.

## Technologies Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Python 3

## Functions
### fetch_and_format_Movies
The function fetch_and_format_movies() gets movie data from DynamoDB and organizes it neatly. It starts by creating an empty list. Then, it fetches movie data from DynamoDB through an API link. If the data is successfully fetched, it processes it into a list of dictionaries, with each dictionary representing a movie. Finally, it sorts the movies by their IDs and returns the list. This function makes it easy to handle movie data from DynamoDB.

```python
formatted_movies = []  # Initialize the list to store formatted movies

    # Fetch movie data from DynamoDB
    response = requests.get('YOUR_GATEWAY_API_LINK')
    
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
```
###  getmovies
This snippet establishes a route '/getmovies' for a Flask web app. When accessed via a GET request, it calls get_movies_json(). This function fetches and formats movie data, then returns it as JSON. In short, '/getmovies' provides movie data in JSON format.
```python
def get_movies_json():
    formatted_movies = fetch_and_format_movies()
    return jsonify(formatted_movies) 
```
### getmoviesbyyear
This code, get_movies_by_year(), filters movie data based on the user's provided year. It fetches and formats the movie data, then extracts the user-provided year from the request parameters. If no year is provided or the year is not between 2000 and 2010, it returns an error message with a 404 status code. Otherwise, it filters the movies by the provided year and returns them in JSON format. In short, it helps users find movies released in a specific year between 2000 and 2010.
```python
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

```
### getMovieSummaries
The get_movie_summaries() function fetches movie summaries based on titles. It extracts the movie title from the request parameters, queries The Movie Database (TMDb) using an API key, and returns the summary of the first movie in JSON format. If no movie is found, it returns a 404 error; if no title is provided or the request fails, it returns a 400 error. This function simplifies the process of getting movie summaries from TMDb.

```python
def get_movie_summaries():
    # Extract movie title from request parameters
    movie_title = request.args.get('title')
    API_key = "YOUR_TMDB_API_KEY"
    
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
```
## Usage
To use this code effectively, you'll first need to create an index.html file, which functions as the main interface for this local web app. Within this page, you have the flexibility to select your preferred method for executing the GET requests.

```html
<body>
    <div class="container">
        <h1>Serverless Movie API</h1>
        <h4 style="text-align:center;"> This List is comprised of the top 10 movies of each year from 2000-2010</h4>

        <h2 style="text-align: center;">Functions</h2>
        <ol>
            <li><h3><a href="{{ url_for('get_movies_json')}}" target="_blank">Get Movies</a></h3></li>
        
            <li><h3>Get Movies by Year:</h3></li>
            <form action="/getmoviesbyyear" method="GET" target="_blank">
                <label for="year">Choose a year:</label>
                <input type="number" id="year" name="year" min="2000" max="2010" required>
                <button type="submit">Get Movies</button>
            </form>
            <li><h3>Movie Summary Generator:</h3></li>
            <form action="/getMovieSummaries" method="GET" target="_blank">
                <label for="movie_title">Enter Movie Title:</label>
                <input type="text" id="movie_title" name="title" required>
                <button type="submit">Generate Summary</button>
            </form>
        </ol>
    </div>
</body>
```

## Considerations
- make sure you have installed all the necessary packages to enable the code to run, this includes: Flask, Boto3, and Requests
- ensure the permissions on your application are adjusted appropriately to allow access    
- Another option is to create 3 different AWS functions within Lambda rather than 3 python functions for scalability and
- Verify the accuracy of your AWS account configurations; the code will not function correctly otherwise
