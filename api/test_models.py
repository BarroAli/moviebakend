"""SQLAlchemy model test"""
# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link
db = SessionLocal()

# %%
#tester la récupuration des données de la base
movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"ID: {movie.movieId}, Title : {movie.title}, Gender: {movie.genres}")

#recuperer les 5 films du genre action(1ère méthode)
# %%
movies_action = db.query(Movie).filter(Movie.genres.contains('Action')).limit(5).all()
for movie in movies_action:
    print(f"ID: {movie.movieId}, Title : {movie.title}, Gender: {movie.genres}")

# %%
#recuperer les 5 films du genre action(2ème méthode)
movies_action = db.query(Movie).filter(Movie.genres.like('%Action%')).limit(5).all()
for movie in movies_action:
    print(f"ID: {movie.movieId}, Title : {movie.title}, Gender: {movie.genres}")

#recuperer quelques évaluation des films (ratings)
# %%
ratings= db.query(Rating).limit(5).all()
for rating in ratings:
    print(f"userId: {rating.userId}, movieId: {rating.movieId}, rating: {rating.rating}, timestamp: {rating.timestamp}")


#filtrer les films avec une note supérieure à 4.0
# %%
high_rated_movie = db.query(Movie.title, Rating.rating).join(Rating).filter(Rating.rating >= 4).limit(5).all()
for title, rating in high_rated_movie:
    print(title, rating)

#filtrer les films avec une note supérieure à 4.0(2è méthode)
# %%
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
)
print(high_rated_movies)

#recupération des tags associés aux films
# %%
tags = db.query(Tag).limit(5).all()
for tag in tags:
    print(f"userId: {tag.userId}, movie Id: {tag.movieId}, tag: {tag.tag}, timestamp: {tag.timestamp}")

#tester les links des film
# %%
links = db.query(Link).limit(5).all()
for link in links:
    print(f"movieId: {link.movieId}, imdbId: {link.imdbId}, tmdbId: {link.tmdbId}")

#fermer la session
# %%
db.close()
# %%
