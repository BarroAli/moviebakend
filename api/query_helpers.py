"""SQLAlchemy query functions for Noveless API"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional
import models

########### FILMS ###############
def get_movie(db:Session, movie_id: int):
    """récuperation d'un film à travers son Id"""
    return db.query(models.Movie).filter(models.Movie.movieId==movie_id).first()

def get_movies(db: Session, skip: int=0, limit: int=100, title: str=None, genre: str=None):
    """récuperation d'une liste de films avec filtres optionnels"""
    query = db.query(models.Movie)
    
    if title:
        query = query.filter(models.Movie.title.ilike(f"%{title}%")) 
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%{genre}%"))
    
    return query.offset(skip).limit(limit).all()


################ EVALUATIONS ##############
def get_rating(db: Session, user_id: int, movie_id: int):
    """recuperation d'une évaluation  en fonction du couple (userId, movieId)"""
    return db.query(models.Rating).filter(
        models.Rating.userId == user_id,
        models.Rating.movieId == movie_id
    ).first()

def get_ratings(db: Session, skip: int=0, limit: int=100, movie_id: int=None, user_id: int=None, min_rating: float=None):
    """récupération d'une liste d'évaluations avec filtres optionnels"""
    query = db.query(models.Rating)

    if movie_id:
        query = query.filter(models.Rating.movieId == movie_id)
    if user_id:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)
    
    return query.offset(skip).limit(limit).all()


############## TAGS ################
def get_tag(db:Session, user_id: int, movie_id:int, tag_text:str):
    """recupère un tag par userId, movieId et le texte du tag"""
    return (
        db.query(models.Tag)
        .filter(
            models.Tag.userId == user_id,
            models.Tag.movieId == movie_id,
            models.Tag.tag == tag_text
        )
        .first()
    )

def get_tags(
        db: Session,
        skip: int = 0,
        limit : int = 100,
        movie_id : Optional[int]=None,
        user_id : Optional[int]=None
):
    """recuperation d'une liste de tags avec filtres optionels"""
    query = db.query(models.Tag)
    if movie_id is not None:
        query = query.filter(models.Tag.movieId == movie_id)
    if user_id is not None:
        query = query.filter(models.Tag.userId == user_id)
    
    return query.offset(skip).limit(limit).all()


################# LIENS ###############
def get_link(db:Session, movie_id : int):
    """recupère le lien IMDB et TMDB associé à un film"""
    return db.query(models.Link).filter(models.Link.movieId == movie_id).first()

def get_links (db:Session, skip: int = 0, limit: int = 100):
    """recupère une liste paginée de lien IMDB et TMDB de films"""
    return db.query(models.Link).offset(skip).limit(limit).all()


########## réquêtes analytiques #########
def get_movie_count(db: Session):
    """Retourne le nombre total de films."""
    return db.query(models.Movie).count()

def get_rating_count(db: Session):
    """Retourne le nombre total d'évaluations."""
    return db.query(models.Rating).count()

def get_tag_count(db: Session):
    """Retourne le nombre total de tags."""
    return db.query(models.Tag).count()

def get_link_count(db: Session):
    """Retourne le nombre total de liens."""
    return db.query(models.Link).count()