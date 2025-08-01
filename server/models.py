from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Article(db.Model, SerializerMixin):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    preview = db.Column(db.String)
    minutes_to_read = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # 🔑 Prevent recursion by excluding the user field when serializing
    serialize_rules = ('-user',)

    def __repr__(self):
        return f'Article {self.id} by {self.author}'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

    # Relationships
    articles = db.relationship('Article', backref='user', lazy=True)

    # 🔑 Prevent recursion: exclude nested user inside articles
    serialize_rules = ('-articles.user',)

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'
