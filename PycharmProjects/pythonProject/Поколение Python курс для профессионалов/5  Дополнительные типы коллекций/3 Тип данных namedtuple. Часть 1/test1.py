from collections import namedtuple
Movie = namedtuple('Movie', ['name', 'genres', 'director', 'imdb_rating'])
movie = Movie('La La Land', ['comedy', 'drama', 'musical'], 'Damien Chazelle', 8)
print(movie.name)
print(movie[0])
