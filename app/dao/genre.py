from app.dao.model.genre import Genre


class GenreDAO:
    """Прокси между БД и сервисами"""
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        """Получить инфу об одном жанре"""
        return self.session.query(Genre).get(genre_id)

    def get_all(self):
        """Получить инфу о всех жанрах"""
        return self.session.query(Genre).all()
