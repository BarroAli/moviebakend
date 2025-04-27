###test des fonctions dans query_helpers.py ###########
from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# movies = get_movies(db=db, limit=5)
# for film in movies:
#     print(f"id: {film.movieId}, titre: {film.title}, genre: {film.genres}")

# rating = get_rating(db=db, movie_id=1,user_id=1)
# print(f"id: {rating.userId}, movie id: {rating.movieId}, rating: {rating.rating}, timestamp: {rating.timestamp}")

# ratings = get_ratings(db=db, min_rating=3.5, limit=10)
# for film in ratings:
#     print(f"id: {film.movieId}, note: {film.rating}")

# tag = get_tag(db=db, user_id=2,movie_id=60756, tag_text='funny')
# print(tag)
# print(f"userid: {tag.userId}, movieid: {tag.movieId}, tag: {tag.tag}")

n_link = get_tag_count(db=db)
print(f"le nombre de films: {n_link}")
db.close()