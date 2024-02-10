import boto3

aws_access_key_id = 'YOURAWSACCESSKEYID'
aws_secret_access_key = 'YOURAWSSECRETACCESSKEY'
region_name = 'YOUR_REGION'
table_name = 'YOUR_DYNAMODB_TABLE_NAME'

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
        "coverimage": "https://movielistimages.s3.amazonaws.com/p7825626_p_v8_af.jpg"
    },
    {
        "MovieID": "1002",
        "title": "The Social Network",
        "releaseYear": "2010",
        "genre": "Biography, Drama",
        "coverimage": "https://movielistimages.s3.amazonaws.com/p8078163_p_v8_ad.jpg"
    },
    {
        "MovieID": "1003",
        "title": "Toy Story 3",
        "releaseYear": "2010",
        "genre": "Animation, Adventure, Comedy",
        "coverimage": "https://movielistimages.s3.amazonaws.com/thumb_F20120C7-E9F7-4C80-8D3F-5EED01DBEE1E.jpg"
    },
    {
        "MovieID": "1004",
        "title": "Black Swan",
        "releaseYear": "2010",
        "genre": "Drama, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p8236892_p_v8_ar.jpg"
    },
    {
        "MovieID": "1005",
        "title": "The King's Speech",
        "releaseYear": "2010",
        "genre": "Biography, Drama, History",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p8073374_v_v13_aq.jpg"
    },
    {
        "MovieID": "1006",
        "title": "True Grit",
        "releaseYear": "2010",
        "genre": "Adventure, Drama, Western",
        "coverimage":"https://movielistimages.s3.amazonaws.com/tCrB8pcjadZjsDk7rleGJaIv78k.jpg"
    },
    {
        "MovieID": "1007",
        "title": "127 Hours",
        "releaseYear": "2010",
        "genre": "Adventure, Biography, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p8236871_p_v10_ba.jpg"
    },
    {
        "MovieID": "1008",
        "title": "The Fighter",
        "releaseYear": "2010",
        "genre": "Biography, Drama, Sport",
        "coverimage":"https://movielistimages.s3.amazonaws.com/61cZrsayy2L._AC_UF894%2C1000_QL80_.jpg"
    },
    {
        "MovieID": "1009",
        "title": "The Town",
        "releaseYear": "2010",
        "genre": "Crime, Drama, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p8076702_p_v11_ak.jpg"
    },
    {
        "MovieID": "1010",
        "title": "Shutter Island",
        "releaseYear": "2010",
        "genre": "Mystery, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p3531967_v_v9_bf.jpg"
    },
    {
        "MovieID": "1011",
        "title": "Avatar",
        "releaseYear": "2009",
        "genre": "Action, Adventure, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p3542039_v_v13_ad.jpg"
    },
    {
        "MovieID": "1012",
        "title": "Up",
        "releaseYear": "2009",
        "genre": "Animation, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p190662_p_v12_ay.jpg"
    },
    {
        "MovieID": "1013",
        "title": "The Blind Side",
        "releaseYear": "2009",
        "genre": "Biography, Drama, Sport",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p3538632_v_h9_ao.jpg"
    },
    {
        "MovieID": "1014",
        "title": "Inglourious Basterds",
        "releaseYear": "2009",
        "genre": "Adventure, Drama, War",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p193875_p_v7_aq.jpg"
    },
    {
        "MovieID": "1015",
        "title": "District 9",
        "releaseYear": "2009",
        "genre": "Action, Sci-Fi, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p177953_v_h9_ae.jpg"
    },
    {
        "MovieID": "1016",
        "title": "Up in the Air",
        "releaseYear": "2009",
        "genre": "Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p3600392_p_v8_av.jpg"
    },
    {
        "MovieID": "1017",
        "title": "A Serious Man",
        "releaseYear": "2009",
        "genre": "Comedy, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p3531873_p_v8_as.jpg"
    },
    {
        "MovieID": "1018",
        "title": "Star Trek",
        "releaseYear": "2009",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/star-trek-09.jpg"
    },
    {
        "MovieID": "1019",
        "title": "The Hangover",
        "releaseYear": "2009",
        "genre": "Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p192248_p_v8_am.jpg"
    },
    {
        "MovieID": "1020",
        "title": "The Hurt Locker",
        "releaseYear": "2009",
        "genre": "Drama, Thriller, War",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p197175_v_h9_ba.jpg"
    },
    {
        "MovieID": "1091",
        "title": "The Dark Knight",
        "releaseYear": "2008",
        "genre": "Action, Crime, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/darkknight.jpg"
    },
    {
        "MovieID": "1022",
        "title": "Wall-E",
        "releaseYear": "2008",
        "genre": "Animation, Adventure, Family",
        "coverimage":"https://movielistimages.s3.amazonaws.com/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw%40%40._V1_.jpg"
    },
    {
        "MovieID": "1023",
        "title": "Slumdog Millionaire",
        "releaseYear": "2008",
        "genre": "Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p179969_p_v8_ak.jpg"
    },
    {
        "MovieID": "1024",
        "title": "Iron Man",
        "releaseYear": "2008",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p170620_p_v8_az.jpg"
    },
    {
        "MovieID": "1025",
        "title": "The Curious Case of Benjamin Button",
        "releaseYear": "2008",
        "genre": "Drama, Fantasy, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p170920_p_v8_am.jpg"
    },
    {
        "MovieID": "1026",
        "title": "Mamma Mia!",
        "releaseYear": "2008",
        "genre": "Comedy, Musical, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/65189_aa.jpg"
    },
    {
        "MovieID": "1027",
        "title": "Gran Torino",
        "releaseYear": "2008",
        "genre": "Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p183329_p_v8_ab.jpg"
    },
    {
        "MovieID": "1028",
        "title": "Quantum of Solace",
        "releaseYear": "2008",
        "genre": "Action, Adventure, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p170973_p_v8_ah.jpg"
    },
    {
        "MovieID": "1029",
        "title": "Twilight",
        "releaseYear": "2008",
        "genre": "Drama, Fantasy, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/large_nlvPMLCdum7bkHKmDSMnNLGztmW.jpg"
    },
    {
        "MovieID": "1030",
        "title": "The Reader",
        "releaseYear": "2008",
        "genre": "Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p188151_p_v11_ab.jpg"
    },
        {
        "MovieID": "1031",
        "title": "No Country for Old Men",
        "releaseYear": "2007",
        "genre": "Crime, Drama, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p170313_p_v13_ad.jpg"
    },
    {
        "MovieID": "1032",
        "title": "There Will Be Blood",
        "releaseYear": "2007",
        "genre": "Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/61939_ab.jpg"
    },
    {
        "MovieID": "1033",
        "title": "Juno",
        "releaseYear": "2007",
        "genre": "Comedy, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p172418_p_v10_aa.jpg"
    },
    {
        "MovieID": "1034",
        "title": "Ratatouille",
        "releaseYear": "2007",
        "genre": "Animation, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p20623444_p_v10_aa.jpg"
    },
    {
        "MovieID": "1035",
        "title": "The Bourne Ultimatum",
        "releaseYear": "2007",
        "genre": "Action, Mystery, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p162782_p_v8_au.jpg"
    },
    {
        "MovieID": "1036",
        "title": "Zodiac",
        "releaseYear": "2007",
        "genre": "Crime, Drama, Mystery",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p166270_p_v8_ai.jpg"
    },
    {
        "MovieID": "1037",
        "title": "The Assassination of Jesse James by the Coward Robert Ford",
        "releaseYear": "2007",
        "genre": "Biography, Crime, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/54706_aa.jpg"
    },
    {
        "MovieID": "1038",
        "title": "Superbad",
        "releaseYear": "2007",
        "genre": "Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p167014_v_h9_aj.jpg"
    },
    {
        "MovieID": "1039",
        "title": "Atonement",
        "releaseYear": "2007",
        "genre": "Drama, Mystery, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p167496_p_v8_am.jpg"
    },
    {
        "MovieID": "1040",
        "title": "Transformers",
        "releaseYear": "2007",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p159729_p_v8_ap.jpg"
    },
      {
        "MovieID": "1041",
        "title": "The Departed",
        "releaseYear": "2006",
        "genre": "Crime, Drama, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/images.jpeg"
    },
    {
        "MovieID": "1042",
        "title": "The Prestige",
        "releaseYear": "2006",
        "genre": "Drama, Mystery, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p161581_v_h9_ao.jpg"
    },
    {
        "MovieID": "1043",
        "title": "Little Miss Sunshine",
        "releaseYear": "2006",
        "genre": "Comedy, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p161258_v_v8_ac.jpg"
    },
    {
        "MovieID": "1044",
        "title": "Pan's Labyrinth",
        "releaseYear": "2006",
        "genre": "Drama, Fantasy, War",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p162074_p_v8_ab.jpg"
    },
    {
        "MovieID": "1045",
        "title": "The Devil Wears Prada",
        "releaseYear": "2006",
        "genre": "Comedy, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p159800_v_v9_be.jpg"
    },
    {
        "MovieID": "1046",
        "title": "Casino Royale",
        "releaseYear": "2006",
        "genre": "Action, Adventure, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p159167_p_v8_aw.jpg"
    },
    {
        "MovieID": "1047",
        "title": "Children of Men",
        "releaseYear": "2006",
        "genre": "Drama, Sci-Fi, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p159796_v_h9_ao.jpg"
    },
    {
        "MovieID": "1048",
        "title": "V for Vendetta",
        "releaseYear": "2006",
        "genre": "Action, Drama, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p159693_p_v8_bb.jpg"
    },
    {
        "MovieID": "1049",
        "title": "The Pursuit of Happyness",
        "releaseYear": "2006",
        "genre": "Biography, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p162523_p_v8_ad.jpg"
    },
    {
        "MovieID": "1050",
        "title": "Cars",
        "releaseYear": "2006",
        "genre": "Animation, Comedy, Family",
        "coverimage":"https://movielistimages.s3.amazonaws.com/1_RaSZ3YZS8N1Mi01LkbT6wg.jpg"
    },
        {
        "MovieID": "1051",
        "title": "Brokeback Mountain",
        "releaseYear": "2005",
        "genre": "Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/41914_ab.jpg"
    },
    {
        "MovieID": "1052",
        "title": "Capote",
        "releaseYear": "2005",
        "genre": "Biography, Crime, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p90443_p_v8_aa.jpg"
    },
    {
        "MovieID": "1053",
        "title": "Crash",
        "releaseYear": "2005",
        "genre": "Crime, Drama, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p35710_v_v8_aj.jpg"
    },
    {
        "MovieID": "1054",
        "title": "Good Night, and Good Luck",
        "releaseYear": "2005",
        "genre": "Biography, Drama, History",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p89817_p_v8_ac.jpg"
    },
    {
        "MovieID": "1055",
        "title": "King Kong",
        "releaseYear": "2005",
        "genre": "Action, Adventure, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/tileburnedin.jpeg"
    },
    {
        "MovieID": "1056",
        "title": "Munich",
        "releaseYear": "2005",
        "genre": "Action, Biography, Crime",
        "coverimage":"https://movielistimages.s3.amazonaws.com/download.jpeg"
    },
    {
        "MovieID": "1057",
        "title": "Walk the Line",
        "releaseYear": "2005",
        "genre": "Biography, Drama, Music",
        "coverimage":"https://movielistimages.s3.amazonaws.com/images+(1).jpeg"
    },
    {
        "MovieID": "1058",
        "title": "Batman Begins",
        "releaseYear": "2005",
        "genre": "Action, Adventure",
        "coverimage":"https://movielistimages.s3.amazonaws.com/616VGokMnsL.jpg"
    },
    {
        "MovieID": "1059",
        "title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
        "releaseYear": "2005",
        "genre": "Adventure, Family, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p90695_p_v8_aj.jpg"
    },
    {
        "MovieID": "1060",
        "title": "Star Wars: Episode III - Revenge of the Sith",
        "releaseYear": "2005",
        "genre": "Action, Adventure, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p35273_p_v8_av.jpg"
    },
        {
        "MovieID": "1061",
        "title": "Million Dollar Baby",
        "releaseYear": "2004",
        "genre": "Drama, Sport",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p35226_p_v8_ar.jpg"
    },
    {
        "MovieID": "1062",
        "title": "The Aviator",
        "releaseYear": "2004",
        "genre": "Biography, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p35190_p_v8_aj.jpg"
    },
    {
        "MovieID": "1063",
        "title": "Sideways",
        "releaseYear": "2004",
        "genre": "Comedy, Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p34948_p_v8_ae.jpg"
    },
    {
        "MovieID": "1064",
        "title": "Eternal Sunshine of the Spotless Mind",
        "releaseYear": "2004",
        "genre": "Drama, Romance, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p33409_v_v10_az.jpg"
    },
    {
        "MovieID": "1065",
        "title": "Finding Neverland",
        "releaseYear": "2004",
        "genre": "Biography, Drama, Family",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p34951_p_v8_ah.jpg"
    },
    {
        "MovieID": "1066",
        "title": "Ray",
        "releaseYear": "2004",
        "genre": "Biography, Drama, Music",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p35003_p_v8_ae.jpg"
    },
    {
        "MovieID": "1067",
        "title": "The Incredibles",
        "releaseYear": "2004",
        "genre": "Animation, Action, Adventure",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p35032_p_v8_at.jpg"
    },
    {
        "MovieID": "1068",
        "title": "Hotel Rwanda",
        "releaseYear": "2004",
        "genre": "Biography, Drama, History",
        "coverimage":"https://movielistimages.s3.amazonaws.com/00300855_10af8bf2a41bc468436a1881391aaace_arc614x376_w735_us1.jpg"
    },
    {
        "MovieID": "1069",
        "title": "The Passion of the Christ",
        "releaseYear": "2004",
        "genre": "Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p33660_p_v8_ah.jpg"
    },
    {
        "MovieID": "1070",
        "title": "Spider-Man 2",
        "releaseYear": "2004",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/unnamed.jpg"
    },
    {
        "MovieID": "1071",
        "title": "The Lord of the Rings: The Return of the King",
        "releaseYear": "2003",
        "genre": "Action, Adventure, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/1607111714_the-lord-of-the-rings-the-return-of-the-king-4k-2003-extended-poster.png"
    },
    {
        "MovieID": "1072",
        "title": "Pirates of the Caribbean: The Curse of the Black Pearl",
        "releaseYear": "2003",
        "genre": "Action, Adventure, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/images+(2).jpeg"
    },
    {
        "MovieID": "1073",
        "title": "Finding Nemo",
        "releaseYear": "2003",
        "genre": "Animation, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/download+(1).jpeg"
    },
    {
        "MovieID": "1074",
        "title": "The Last Samurai",
        "releaseYear": "2003",
        "genre": "Action, Drama, War",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p33171_v_h9_ao.jpg"
    },
    {
        "MovieID": "1075",
        "title": "The Matrix Reloaded",
        "releaseYear": "2003",
        "genre": "Action, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p31912_p_v8_bb.jpg"
    },
    {
        "MovieID": "1076",
        "title": "Bruce Almighty",
        "releaseYear": "2003",
        "genre": "Comedy, Drama, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p31817_v_v9_ae.jpg"
    },
    {
        "MovieID": "1077",
        "title": "The Italian Job",
        "releaseYear": "2003",
        "genre": "Action, Crime, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p470_v_h9_am.jpg"
    },
    {
        "MovieID": "1078",
        "title": "Kill Bill: Vol. 1",
        "releaseYear": "2003",
        "genre": "Action, Crime",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p32988_p_v8_aa.jpg"
    },
    {
        "MovieID": "1079",
        "title": "Mystic River",
        "releaseYear": "2003",
        "genre": "Crime, Drama, Mystery",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p32186_v_v8_al.jpg"
    },
    {
        "MovieID": "1080",
        "title": "Elf",
        "releaseYear": "2003",
        "genre": "Comedy, Family, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/large_2BCvh9w8YXP30Jst8PkMngEo619.jpg"
    },
       {
        "MovieID": "1081",
        "title": "The Lord of the Rings: The Two Towers",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p30793_k_v9_ac.jpg"
    },
    {
        "MovieID": "1082",
        "title": "Spider-Man",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p13222290_b_v9_ad.jpg"
    },
    {
        "MovieID": "1083",
        "title": "Star Wars: Episode II - Attack of the Clones",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p28914_v_v9_aa.jpg"
    },
    {
        "MovieID": "1084",
        "title": "The Pianist",
        "releaseYear": "2002",
        "genre": "Biography, Drama, Music",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p30193_v_h8_ag.jpg"
    },
    {
        "MovieID": "1085",
        "title": "Men in Black II",
        "releaseYear": "2002",
        "genre": "Action, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/81bYthNNZfL._AC_UF894%2C1000_QL80_.jpg"
    },
    {
        "MovieID": "1086",
        "title": "Catch Me If You Can",
        "releaseYear": "2002",
        "genre": "Biography, Crime, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/images+(3).jpeg"
    },
    {
        "MovieID": "1087",
        "title": "The Bourne Identity",
        "releaseYear": "2002",
        "genre": "Action, Mystery, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p28900_p_v8_ar.jpg"
    },
    {
        "MovieID": "1088",
        "title": "Ice Age",
        "releaseYear": "2002",
        "genre": "Animation, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/Ice-Age-2002.jpg"
    },
    {
        "MovieID": "1089",
        "title": "My Big Fat Greek Wedding",
        "releaseYear": "2002",
        "genre": "Comedy, Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p29868_v_v8_af.jpg"
    },
    {
        "MovieID": "1090",
        "title": "Minority Report",
        "releaseYear": "2002",
        "genre": "Action, Crime, Mystery",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p11908931_b_v9_aa.jpg"
    },
    {
        "MovieID": "1101",
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "releaseYear": "2001",
        "genre": "Action, Adventure, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p28828_p_v8_ao.jpg"
    },
    {
        "MovieID": "1102",
        "title": "Harry Potter and the Sorcerer's Stone",
        "releaseYear": "2001",
        "genre": "Adventure, Family, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/TITLE_ART_16_9.jpeg"
        
    },
    {
        "MovieID": "1103",
        "title": "Shrek",
        "releaseYear": "2001",
        "genre": "Animation, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p23961510_v_v8_aa.jpg"
    },
    {
        "MovieID": "1104",
        "title": "A Beautiful Mind",
        "releaseYear": "2001",
        "genre": "Biography, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p28869_v_v10_at.jpg"
    },
    {
        "MovieID": "1105",
        "title": "Monsters, Inc.",
        "releaseYear": "2001",
        "genre": "Animation, Adventure, Comedy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/download+(2).jpeg"
    },
    {
        "MovieID": "1106",
        "title": "Ocean's Eleven",
        "releaseYear": "2001",
        "genre": "Crime, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p28801_p_v10_am.jpg"
    },
    {
        "MovieID": "1107",
        "title": "The Mummy Returns",
        "releaseYear": "2001",
        "genre": "Action, Adventure, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p27207_p_v13_an.jpg"
    },
    {
        "MovieID": "1108",
        "title": "Jurassic Park III",
        "releaseYear": "2001",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/AAAABWw9eZmS90sYed7geguqtUa8z8jRZA1TayDFaJDD32KUNokSwwYD96px3MQN7tNPr9opkoCPJ8mu6buum7_ILbhAcoyS.jpg"
    },
    {
        "MovieID": "1109",
        "title": "Pearl Harbor",
        "releaseYear": "2001",
        "genre": "Action, Drama, History",
        "coverimage":"https://movielistimages.s3.amazonaws.com/MV5BOTMxOTUxNjQtZmRhNi00NWM5LTliNzEtYjk4OTNmZWE0YzllXkEyXkFqcGdeQXVyNTIzOTk5ODM%40._V1_.jpg"
    },
    {
        "MovieID": "1110",
        "title": "The Fast and the Furious",
        "releaseYear": "2001",
        "genre": "Action, Crime, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p27779_p_v8_aw.jpg"
    },
    {
        "MovieID": "1111",
        "title": "Gladiator",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p24674_p_v8_ae.jpg"
    },
    {
        "MovieID": "1112",
        "title": "Cast Away",
        "releaseYear": "2000",
        "genre": "Adventure, Drama, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/51WfhfdkGeL._AC_UF894%2C1000_QL80_.jpg"
    },
    {
        "MovieID": "1113",
        "title": "Mission: Impossible 2",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Thriller",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p25485_v_v10_aa.jpg"
    },
    {
        "MovieID": "1114",
        "title": "X-Men",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Sci-Fi",
        "coverimage":"https://movielistimages.s3.amazonaws.com/MV5BZmIyMDk5NGYtYjQ5NS00ZWQxLTg2YzQtZDk1ZmM4ZDBlN2E3XkEyXkFqcGdeQXVyMTQxNzMzNDI%40._V1_.jpg"
    },
    {
        "MovieID": "1115",
        "title": "How the Grinch Stole Christmas",
        "releaseYear": "2000",
        "genre": "Comedy, Family, Fantasy",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p26539_p_v11_ca.jpg"
    },
    {
        "MovieID": "1116",
        "title": "Meet the Parents",
        "releaseYear": "2000",
        "genre": "Comedy, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p26230_p_v8_av.jpg"
    },
    {
        "MovieID": "1117",
        "title": "Dinosaur",
        "releaseYear": "2000",
        "genre": "Animation, Adventure, Family",
        "coverimage":"https://movielistimages.s3.amazonaws.com/66f5a29fb66c143f993411d9292ade18.jpg"
    },
    {
        "MovieID": "1118",
        "title": "What Women Want",
        "releaseYear": "2000",
        "genre": "Comedy, Fantasy, Romance",
        "coverimage":"https://movielistimages.s3.amazonaws.com/images+(4).jpeg"
    },
    {
        "MovieID": "1119",
        "title": "The Perfect Storm",
        "releaseYear": "2000",
        "genre": "Action, Adventure, Drama",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p25744_p_v8_aq.jpg"
    },
    {
        "MovieID": "1120",
        "title": "Remember the Titans",
        "releaseYear": "2000",
        "genre": "Biography, Drama, Sport",
        "coverimage":"https://movielistimages.s3.amazonaws.com/p25848_p_v8_az.jpg"
    },
]
for movie in movies:
    table.put_item(Item=movie)

print("Entries added to DynamoDB table successfully.")


