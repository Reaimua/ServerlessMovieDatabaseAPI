# PythonServerlessAPI

## Overview 
This project focuses on developing a serverless movie API using Python within the context of the [6 Month Cloud Study Plan](https://www.madebygps.com/cloudcamp/). The goal is to gain practical experience in building cloud-native applications leveraging serverless architecture and AWS services. 

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

```python
{
    "title": "title of the movie",
    "releaseYear": "when the movie was released",
    "genre": "genre of the movie",
    "coverUrl": "url-to-image-in-cloud-storage"
}
```
### getmoviesbyyear
```json
  {
    "MovieID": 1011,
    "coverimage": "https://movielistimages.s3.amazonaws.com/p3542039_v_v13_ad.jpg",
    "genre": "Action, Adventure, Fantasy",
    "releaseYear": 2009,
    "title": "Avatar"
  },
  {
    "MovieID": 1012,
    "coverimage": "https://movielistimages.s3.amazonaws.com/p190662_p_v12_ay.jpg",
    "genre": "Animation, Adventure, Comedy",
    "releaseYear": 2009,
    "title": "Up"
  }
```
### getMovieSummaries
```json
{
  "summary": "Summary of the Movie inputted",
  "title": "title of the movie"
}
```
