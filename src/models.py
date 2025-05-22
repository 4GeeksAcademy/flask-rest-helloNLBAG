from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    nombre = db.Column(db.String(120))
    apellido = db.Column(db.String(120))
    fecha_subscripcion = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship('Post', backref='autor', lazy=True)
    comentarios = db.relationship('Comentario', backref='autor', lazy=True)
    seguidores = db.relationship('Follower', foreign_keys='Follower.user_to_id', backref='seguido', lazy=True)
    seguidos = db.relationship('Follower', foreign_keys='Follower.user_from_id', backref='seguidor', lazy=True)
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)

class Planeta(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    clima = db.Column(db.String(120))
    terreno = db.Column(db.String(120))
    poblacion = db.Column(db.String(120))
    favoritos = db.relationship('Favorito', backref='planeta', lazy=True)

class Personaje(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    altura = db.Column(db.String(50))
    peso = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    favoritos = db.relationship('Favorito', backref='personaje', lazy=True)

class Favorito(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    personaje_id = db.Column(db.Integer, db.ForeignKey('personajes.id'))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    comentarios = db.relationship('Comentario', backref='post', lazy=True)

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

class Follower(db.Model):
    __tablename__ = 'followers'
    user_from_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    user_to_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
