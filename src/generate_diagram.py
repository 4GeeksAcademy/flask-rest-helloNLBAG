from models import db
from app import app
from eralchemy2 import render_er

with app.app_context():
    render_er(db.metadata, 'diagram.png')
