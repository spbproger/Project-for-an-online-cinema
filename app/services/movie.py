from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        movie_id = data.get('id')
        movie = self.get_one(movie_id)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.genre = data.get('genre')
        movie.director_id = data.get('director_id')
        movie.director = data.get('director')

        self.dao.update(movie_id)
        return movie

    def update_partial(self, data):
        movie_id = data.get('id')
        movie = self.get_one(movie_id)

        if 'title' in data:
            movie.title = data['title']
        if 'description' in data:
            movie.description = data['description']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'year' in data:
            movie.year = data['year']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'genre' in data:
            movie.genre = data['genre']
        if 'director_id' in data:
            movie.director_id = data['director_id']
        if 'director' in data:
            movie.director = data['director']

        self.dao.update(movie_id)
        return movie

    def delete(self, movie_id):
        self.dao.delete(movie_id)
