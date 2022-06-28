from app.dao.model.movie import Movie


class MovieDAO:
    """Прокси между БД и сервисами"""
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        """Получить инфу об одном фильме"""
        return self.session.query(Movie).get(movie_id)

    def get_all(self):
        """Получить инфу о всех фильмах"""
        return self.session.query(Movie).all()

    def create(self, data):
        """Добавить инфу о фильме"""
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie_id):
        """Обновить инфу о фильме"""
        movie = self.get_one(movie_id)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie_id):
        """Удалить инфу о фильме"""
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()
