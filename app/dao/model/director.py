from marshmallow import Schema, fields
from app.setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __str__(self):  # Показывает имя режиссера во вьюшке /movies
        return self.name


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
