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
    {
        "MovieID": "1091",
        "title": "The Dark Knight",
        "releaseYear": "2008",
        "genre": "Action, Crime, Drama"
    },
    {
        "MovieID": "1022",
        "title": "Wall-E",
        "releaseYear": "2008",
        "genre": "Animation, Adventure, Family"
    },
    {
        "MovieID": "1023",
        "title": "Slumdog Millionaire",
        "releaseYear": "2008",
        "genre": "Drama, Romance"
    },
    {
        "MovieID": "1024",
        "title": "Iron Man",
        "releaseYear": "2008",
        "genre": "Action, Adventure, Sci-Fi"
    },
    {
        "MovieID": "1025",
        "title": "The Curious Case of Benjamin Button",
        "releaseYear": "2008",
        "genre": "Drama, Fantasy, Romance"
    },
    {
        "MovieID": "1026",
        "title": "Mamma Mia!",
        "releaseYear": "2008",
        "genre": "Comedy, Musical, Romance"
    },
    {
        "MovieID": "1027",
        "title": "Gran Torino",
        "releaseYear": "2008",
        "genre": "Drama"
    },
    {
        "MovieID": "1028",
        "title": "Quantum of Solace",
        "releaseYear": "2008",
        "genre": "Action, Adventure, Thriller"
    },
    {
        "MovieID": "1029",
        "title": "Twilight",
        "releaseYear": "2008",
        "genre": "Drama, Fantasy, Romance"
    },
    {
        "MovieID": "1030",
        "title": "The Reader",
        "releaseYear": "2008",
        "genre": "Drama, Romance"
    },
        {
        "MovieID": "1031",
        "title": "No Country for Old Men",
        "releaseYear": "2007",
        "genre": "Crime, Drama, Thriller"
    },
    {
        "MovieID": "1032",
        "title": "There Will Be Blood",
        "releaseYear": "2007",
        "genre": "Drama"
    },
    {
        "MovieID": "1033",
        "title": "Juno",
        "releaseYear": "2007",
        "genre": "Comedy, Drama"
    },
    {
        "MovieID": "1034",
        "title": "Ratatouille",
        "releaseYear": "2007",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1035",
        "title": "The Bourne Ultimatum",
        "releaseYear": "2007",
        "genre": "Action, Mystery, Thriller"
    },
    {
        "MovieID": "1036",
        "title": "Zodiac",
        "releaseYear": "2007",
        "genre": "Crime, Drama, Mystery"
    },
    {
        "MovieID": "1037",
        "title": "The Assassination of Jesse James by the Coward Robert Ford",
        "releaseYear": "2007",
        "genre": "Biography, Crime, Drama"
    },
    {
        "MovieID": "1038",
        "title": "Superbad",
        "releaseYear": "2007",
        "genre": "Comedy"
    },
    {
        "MovieID": "1039",
        "title": "Atonement",
        "releaseYear": "2007",
        "genre": "Drama, Mystery, Romance"
    },
    {
        "MovieID": "1040",
        "title": "Transformers",
        "releaseYear": "2007",
        "genre": "Action, Adventure, Sci-Fi"
    },
      {
        "MovieID": "1041",
        "title": "The Departed",
        "releaseYear": "2006",
        "genre": "Crime, Drama, Thriller"
    },
    {
        "MovieID": "1042",
        "title": "The Prestige",
        "releaseYear": "2006",
        "genre": "Drama, Mystery, Sci-Fi"
    },
    {
        "MovieID": "1043",
        "title": "Little Miss Sunshine",
        "releaseYear": "2006",
        "genre": "Comedy, Drama"
    },
    {
        "MovieID": "1044",
        "title": "Pan's Labyrinth",
        "releaseYear": "2006",
        "genre": "Drama, Fantasy, War"
    },
    {
        "MovieID": "1045",
        "title": "The Devil Wears Prada",
        "releaseYear": "2006",
        "genre": "Comedy, Drama"
    },
    {
        "MovieID": "1046",
        "title": "Casino Royale",
        "releaseYear": "2006",
        "genre": "Action, Adventure, Thriller"
    },
    {
        "MovieID": "1047",
        "title": "Children of Men",
        "releaseYear": "2006",
        "genre": "Drama, Sci-Fi, Thriller"
    },
    {
        "MovieID": "1048",
        "title": "V for Vendetta",
        "releaseYear": "2006",
        "genre": "Action, Drama, Sci-Fi"
    },
    {
        "MovieID": "1049",
        "title": "The Pursuit of Happyness",
        "releaseYear": "2006",
        "genre": "Biography, Drama"
    },
    {
        "MovieID": "1050",
        "title": "Cars",
        "releaseYear": "2006",
        "genre": "Animation, Comedy, Family"
    },
        {
        "MovieID": "1051",
        "title": "Brokeback Mountain",
        "releaseYear": "2005",
        "genre": "Drama, Romance"
    },
    {
        "MovieID": "1052",
        "title": "Capote",
        "releaseYear": "2005",
        "genre": "Biography, Crime, Drama"
    },
    {
        "MovieID": "1053",
        "title": "Crash",
        "releaseYear": "2005",
        "genre": "Crime, Drama, Thriller"
    },
    {
        "MovieID": "1054",
        "title": "Good Night, and Good Luck",
        "releaseYear": "2005",
        "genre": "Biography, Drama, History"
    },
    {
        "MovieID": "1055",
        "title": "King Kong",
        "releaseYear": "2005",
        "genre": "Action, Adventure, Drama"
    },
    {
        "MovieID": "1056",
        "title": "Munich",
        "releaseYear": "2005",
        "genre": "Action, Biography, Crime"
    },
    {
        "MovieID": "1057",
        "title": "Walk the Line",
        "releaseYear": "2005",
        "genre": "Biography, Drama, Music"
    },
    {
        "MovieID": "1058",
        "title": "Batman Begins",
        "releaseYear": "2005",
        "genre": "Action, Adventure"
    },
    {
        "MovieID": "1059",
        "title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
        "releaseYear": "2005",
        "genre": "Adventure, Family, Fantasy"
    },
    {
        "MovieID": "1060",
        "title": "Star Wars: Episode III - Revenge of the Sith",
        "releaseYear": "2005",
        "genre": "Action, Adventure, Fantasy"
    },
        {
        "MovieID": "1061",
        "title": "Million Dollar Baby",
        "releaseYear": "2004",
        "genre": "Drama, Sport"
    },
    {
        "MovieID": "1062",
        "title": "The Aviator",
        "releaseYear": "2004",
        "genre": "Biography, Drama"
    },
    {
        "MovieID": "1063",
        "title": "Sideways",
        "releaseYear": "2004",
        "genre": "Comedy, Drama, Romance"
    },
    {
        "MovieID": "1064",
        "title": "Eternal Sunshine of the Spotless Mind",
        "releaseYear": "2004",
        "genre": "Drama, Romance, Sci-Fi"
    },
    {
        "MovieID": "1065",
        "title": "Finding Neverland",
        "releaseYear": "2004",
        "genre": "Biography, Drama, Family"
    },
    {
        "MovieID": "1066",
        "title": "Ray",
        "releaseYear": "2004",
        "genre": "Biography, Drama, Music"
    },
    {
        "MovieID": "1067",
        "title": "The Incredibles",
        "releaseYear": "2004",
        "genre": "Animation, Action, Adventure"
    },
    {
        "MovieID": "1068",
        "title": "Hotel Rwanda",
        "releaseYear": "2004",
        "genre": "Biography, Drama, History"
    },
    {
        "MovieID": "1069",
        "title": "The Passion of the Christ",
        "releaseYear": "2004",
        "genre": "Drama"
    },
    {
        "MovieID": "1070",
        "title": "Spider-Man 2",
        "releaseYear": "2004",
        "genre": "Action, Adventure, Sci-Fi"
    },
    {
        "MovieID": "1071",
        "title": "The Lord of the Rings: The Return of the King",
        "releaseYear": "2003",
        "genre": "Action, Adventure, Drama"
    },
    {
        "MovieID": "1072",
        "title": "Pirates of the Caribbean: The Curse of the Black Pearl",
        "releaseYear": "2003",
        "genre": "Action, Adventure, Fantasy"
    },
    {
        "MovieID": "1073",
        "title": "Finding Nemo",
        "releaseYear": "2003",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1074",
        "title": "The Last Samurai",
        "releaseYear": "2003",
        "genre": "Action, Drama, War"
    },
    {
        "MovieID": "1075",
        "title": "The Matrix Reloaded",
        "releaseYear": "2003",
        "genre": "Action, Sci-Fi"
    },
    {
        "MovieID": "1076",
        "title": "Bruce Almighty",
        "releaseYear": "2003",
        "genre": "Comedy, Drama, Fantasy"
    },
    {
        "MovieID": "1077",
        "title": "The Italian Job",
        "releaseYear": "2003",
        "genre": "Action, Crime, Thriller"
    },
    {
        "MovieID": "1078",
        "title": "Kill Bill: Vol. 1",
        "releaseYear": "2003",
        "genre": "Action, Crime"
    },
    {
        "MovieID": "1079",
        "title": "Mystic River",
        "releaseYear": "2003",
        "genre": "Crime, Drama, Mystery"
    },
    {
        "MovieID": "1080",
        "title": "Elf",
        "releaseYear": "2003",
        "genre": "Comedy, Family, Fantasy"
    },
       {
        "MovieID": "1081",
        "title": "The Lord of the Rings: The Two Towers",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Drama"
    },
    {
        "MovieID": "1082",
        "title": "Spider-Man",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Sci-Fi"
    },
    {
        "MovieID": "1083",
        "title": "Star Wars: Episode II - Attack of the Clones",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Fantasy"
    },
    {
        "MovieID": "1084",
        "title": "The Pianist",
        "releaseYear": "2002",
        "genre": "Biography, Drama, Music"
    },
    {
        "MovieID": "1085",
        "title": "Men in Black II",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Comedy"
    },
    {
        "MovieID": "1086",
        "title": "Catch Me If You Can",
        "releaseYear": "2002",
        "genre": "Biography, Crime, Drama"
    },
    {
        "MovieID": "1087",
        "title": "The Bourne Identity",
        "releaseYear": "2002",
        "genre": "Action, Mystery, Thriller"
    },
    {
        "MovieID": "1088",
        "title": "Ice Age",
        "releaseYear": "2002",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1089",
        "title": "My Big Fat Greek Wedding",
        "releaseYear": "2002",
        "genre": "Comedy, Drama, Romance"
    },
    {
        "MovieID": "1090",
        "title": "Minority Report",
        "releaseYear": "2002",
        "genre": "Action, Crime, Mystery"
    },
    {
        "MovieID": "1101",
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "releaseYear": "2001",
        "genre": "Action, Adventure, Drama"
    },
    {
        "MovieID": "1102",
        "title": "Harry Potter and the Sorcerer's Stone",
        "releaseYear": "2001",
        "genre": "Adventure, Family, Fantasy"
    },
    {
        "MovieID": "1103",
        "title": "Shrek",
        "releaseYear": "2001",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1104",
        "title": "A Beautiful Mind",
        "releaseYear": "2001",
        "genre": "Biography, Drama"
    },
    {
        "MovieID": "1105",
        "title": "Monsters, Inc.",
        "releaseYear": "2001",
        "genre": "Animation, Adventure, Comedy"
    },
    {
        "MovieID": "1106",
        "title": "Ocean's Eleven",
        "releaseYear": "2001",
        "genre": "Crime, Thriller"
    },
    {
        "MovieID": "1107",
        "title": "The Mummy Returns",
        "releaseYear": "2001",
        "genre": "Action, Adventure, Fantasy"
    },
    {
        "MovieID": "1108",
        "title": "Jurassic Park III",
        "releaseYear": "2001",
        "genre": "Action, Adventure, Sci-Fi"
    },
    {
        "MovieID": "1109",
        "title": "Pearl Harbor",
        "releaseYear": "2001",
        "genre": "Action, Drama, History"
    },
    {
        "MovieID": "1110",
        "title": "The Fast and the Furious",
        "releaseYear": "2001",
        "genre": "Action, Crime, Thriller"
    },
    {
        "MovieID": "1111",
        "title": "Gladiator",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Drama"
    },
    {
        "MovieID": "1112",
        "title": "Cast Away",
        "releaseYear": "2000",
        "genre": "Adventure, Drama, Romance"
    },
    {
        "MovieID": "1113",
        "title": "Mission: Impossible 2",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Thriller"
    },
    {
        "MovieID": "1114",
        "title": "X-Men",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Sci-Fi"
    },
    {
        "MovieID": "1115",
        "title": "How the Grinch Stole Christmas",
        "releaseYear": "2000",
        "genre": "Comedy, Family, Fantasy"
    },
    {
        "MovieID": "1116",
        "title": "Meet the Parents",
        "releaseYear": "2000",
        "genre": "Comedy, Romance"
    },
    {
        "MovieID": "1117",
        "title": "Dinosaur",
        "releaseYear": "2000",
        "genre": "Animation, Adventure, Family"
    },
    {
        "MovieID": "1118",
        "title": "What Women Want",
        "releaseYear": "2000",
        "genre": "Comedy, Fantasy, Romance"
    },
    {
        "MovieID": "1119",
        "title": "The Perfect Storm",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Drama"
    },
    {
        "MovieID": "1120",
        "title": "Remember the Titans",
        "releaseYear": "2000",
        "genre": "Biography, Drama, Sport"
    },
]
for movie in movies:
    table.put_item(Item=movie)

print("Entries added to DynamoDB table successfully.")


