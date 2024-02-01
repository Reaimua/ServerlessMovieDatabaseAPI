import boto3

aws_access_key_id = 'AKIARHNZ4AF3AJUQP645'
aws_secret_access_key = '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'
region_name = 'us-east-1'
table_name = 'MovieList'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)
table = dynamodb.Table(table_name)

movies =[
    {
        "MovieID": "1001",
        "title": "Inception",
        "releaseYear": "2010",
        "genre": "Science Fiction, Action",
    },
    {
        "MovieID": "1002",
        "title": "The Social Network",
        "releaseYear": "2010",
        "genre": "Biography, Drama"
    },
    {
        "MovieID": "1003",
        "title": "Toy Story 3",
        "releaseYear": "2010",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1004",
        "title": "Black Swan",
        "releaseYear": "2010",
        "genre": "Drama, Thriller"
    },
    {
        "MovieID": "1005",
        "title": "The King's Speech",
        "releaseYear": "2010",
        "genre": "Biography, Drama, History"
    },
    {
        "MovieID": "1006",
        "title": "True Grit",
        "releaseYear": "2010",
        "genre": "Adventure, Drama, Western"
    },
    {
        "MovieID": "1007",
        "title": "127 Hours",
        "releaseYear": "2010",
        "genre": "Adventure, Biography, Drama"
    },
    {
        "MovieID": "1008",
        "title": "The Fighter",
        "releaseYear": "2010",
        "genre": "Biography, Drama, Sport"
    },
    {
        "MovieID": "1009",
        "title": "The Town",
        "releaseYear": "2010",
        "genre": "Crime, Drama, Thriller"
    },
    {
        "MovieID": "1010",
        "title": "Shutter Island",
        "releaseYear": "2010",
        "genre": "Mystery, Thriller"
    },
    {
        "MovieID": "1011",
        "title": "Avatar",
        "releaseYear": "2009",
        "genre": "Action, Adventure, Fantasy"
    },
    {
        "MovieID": "1012",
        "title": "Up",
        "releaseYear": "2009",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1013",
        "title": "The Blind Side",
        "releaseYear": "2009",
        "genre": "Biography, Drama, Sport"
    },
    {
        "MovieID": "1014",
        "title": "Inglourious Basterds",
        "releaseYear": "2009",
        "genre": "Adventure, Drama, War"
    },
    {
        "MovieID": "1015",
        "title": "District 9",
        "releaseYear": "2009",
        "genre": "Action, Sci-Fi, Thriller"
    },
    {
        "MovieID": "1016",
        "title": "Up in the Air",
        "releaseYear": "2009",
        "genre": "Drama, Romance"
    },
    {
        "MovieID": "1017",
        "title": "A Serious Man",
        "releaseYear": "2009",
        "genre": "Comedy, Drama"
    },
    {
        "MovieID": "1018",
        "title": "Star Trek",
        "releaseYear": "2009",
        "genre": "Action, Adventure, Sci-Fi"
    },
    {
        "MovieID": "1019",
        "title": "The Hangover",
        "releaseYear": "2009",
        "genre": "Comedy"
    },
    {
        "MovieID": "1020",
        "title": "The Hurt Locker",
        "releaseYear": "2009",
        "genre": "Drama, Thriller, War"
    },
]
for movie in movies:
    table.put_item(Item=movie)

print("Entries added to DynamoDB table successfully.")


