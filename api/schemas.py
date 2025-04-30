from pydantic import BaseModel
from typing import Optional, List

####### schémas sécondaires ######
class RatingBase(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int
    class Config:
        orm_mode = True

class TagBase(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int
    class Config:
        orm_mode = True

class LinkBase(BaseModel):
    imdbId: Optional[str]
    tmdbId: Optional[int]
    class Config:
        orm_mode = True


########## Schéma principal pour movie
class MovieBase(BaseModel):
    movieId : int
    title : str
    genres : Optional[str] = None
    class Config:
        orm_mode = True


class MovieDetailed(MovieBase):
    ratings : List[RatingBase]=[]
    tags: List[TagBase] = []
    link: Optional[LinkBase]=[]


############# Schéma pour lire les films (sans détails embriqués)
class MovieSimple(BaseModel):
    movieId: int
    title: str
    genres: Optional[str]
    class Config:
        orm_mode = True


######## pour les endpoints /ratings, /tags et /links si appelés seuls ---
class RatingSimple(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    class Config:
        orm_mode = True


class TagSimple(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int

    class Config:
        orm_mode = True


class LinkSimple(BaseModel):
    movieId: int
    imdbId: Optional[str]
    tmdbId: Optional[int]

    class Config:
        orm_mode = True

class AnalyticsResponse(BaseModel):
    movie_count: int
    rating_count: int
    tag_count: int
    link_count: int

    class Config:
        orm_mode = True