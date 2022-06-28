from flask_restx import Resource, Namespace
from app.container import director_service
from app.dao.model.director import director_schema, directors_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_direct = director_service.get_all()
        return directors_schema.dump(all_direct)


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        direct = director_service.get_one(director_id)
        return director_schema.dump(direct), 200
