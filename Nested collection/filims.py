movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

# total number of movies

total=len(movies)
# print(total)

# movies with genre drama

drama_movies=[m.get("title") for m in movies if "Drama" in m.get("genres")]
# print(drama_movies)

# latest movie

latest_movie_year=max([m.get("year") for m in movies])
latest_movie=[m.get("title")for m in movies if m.get("year")==latest_movie_year]
# print(latest_movie)

# movies with language malayalam

malayalam_movies=[m.get("title") for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movies)

# movies released after year 2016

movies_aftr_2016=[m.get("title") for m in movies if m.get("year")>2016]
# print(movies_aftr_2016)

# movie with lowest rating

cheap_rating=min([m.get("rating") for m in movies])
cheap_rated_movie=[m.get("title")for m in movies if m.get("rating")==cheap_rating]
# print(cheap_rated_movie)

# malayalam movies with genere Action

action_movie=[m.get("title") for m in movies if m.get("language")=="Malayalam" and m.get("genre")=="Action"]
# print(action_movie)

# movies releasd in same years

movie_dictionary={}
for m in movies:
    release_year=m.get("year")
    if release_year in movie_dictionary:
        movie_dictionary[release_year]+=1
    else:
        movie_dictionary[release_year]=1
# print(movie_dictionary)

# oldest movie

oldest_movie_yr=min([m.get("year")for m in movies])
oldest_movie=[m.get("title") for m in movies if m.get("year")==oldest_movie_yr]
# print(oldest_movie)

# movie name with generes either Drama or Comedy

new_movie=[m.get("title") for m in movies if "Comedy" or "Drama" in m.get("genre")]
# print(new_movie)

# number of movies released in each year

years=[m.get("year")for m in movies]
year_count={y:years.count(y)for y in years}
# print(year_count)

# print all genres

# genre=set()
# for m in movies:
#     for g in m.get("genres"):
#         genre.add(g)

genre={g for m in movies for g in m.get("genres")}
# print(genre)

# genre:count(genre)

genre_count={m.get("genres"):m.count("genres") for m in movies}
print(genre_count)