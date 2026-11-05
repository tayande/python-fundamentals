"""
Mini-lab: write two small functions using the movies list above:

find_movie(movies, movie_id) returns the movie with that ID, or None if it doesn’t exist.
add_movie(movies, new_movie) adds the movie, but raises a ValueError if a movie with the same ID already exists.
"""
movies = [
    {"id": "MV001", "title": "Up",   "year": 2009},
    {"id": "MV002", "title": "Coco", "year": 2017},
    {"id": "MV003", "title": "Soul", "year": 2020},
]


# function 1
def find_movie(movies, movie_id):
    # result = {}
    for movie in movies:
        new = movie.get("id")
        if new == movie_id:
            return movie
    return None
movies = [
    {"id": "MV001", "title": "Up",   "year": 2009},
    {"id": "MV002", "title": "Coco", "year": 2017},
    {"id": "MV003", "title": "Soul", "year": 2020},
]
result = find_movie(movies, "MV002")
print(result)
result = find_movie(movies, "MV005")
print(result)

# Function 2


def add_movie(movies, new_movie):
    new_id = new_movie.get("id")
    for movie in movies:
        existing_id = movie.get("id")
        if new_id == existing_id:
            raise ValueError("movie already exist")
    movies.append(new_movie)
    return movies

movies = [
    {"id": "MV001", "title": "Up",   "year": 2009},
    {"id": "MV002", "title": "Coco", "year": 2017},
    {"id": "MV003", "title": "Soul", "year": 2020},
]
new = {"id": "MV004", "title": "Silicon valley", "year": 2025}
result = add_movie(movies, new)
print(result)
print(len(result))


# testing the second function
try:
    add_movie(movies, {"id": "MV002", "title": "Fake", "year": 2000})
except ValueError as e:
    print("Rejected:", e)
print(len(movies))   # should still be 4