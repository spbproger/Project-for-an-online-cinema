from app.dao.model.director import Director


class DirectorDAO:
    """Прокси между БД и сервисами"""
    def __init__(self, session):
        self.session = session

    def get_one(self, dir_id):
        """Получить инфу об одном режиссере"""
        return self.session.query(Director).get(dir_id)

    def get_all(self):
        """Получить инфу о всех режиссерах"""
        return self.session.query(Director).all()
