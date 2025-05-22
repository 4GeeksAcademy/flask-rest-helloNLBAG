import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Usuario, Planeta, Personaje, Favorito, Post, Comentario, Follower

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Star Wars Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(Usuario, db.session))
    admin.add_view(ModelView(Planeta, db.session))
    admin.add_view(ModelView(Personaje, db.session))
    admin.add_view(ModelView(Favorito, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Comentario, db.session))
    admin.add_view(ModelView(Follower, db.session))
