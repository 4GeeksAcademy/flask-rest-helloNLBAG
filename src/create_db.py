from app import app
from models import db, Usuario, Planeta, Personaje, Favorito, Post, Comentario, Follower

with app.app_context():
    db.drop_all()
    db.create_all()

    # Usuarios
    luke = Usuario(username='lukesky', email='luke@jedi.com', password='force123', nombre='Luke', apellido='Skywalker')
    leia = Usuario(username='leiaorgana', email='leia@rebels.com', password='alderaan', nombre='Leia', apellido='Organa')

    # Personajes y Planetas
    yoda = Personaje(nombre='Yoda', altura='66', peso='17', genero='masculino')
    tatooine = Planeta(nombre='Tatooine', clima='árido', terreno='desértico', poblacion='200000')

    # Favoritos
    fav1 = Favorito(usuario=luke, personaje=yoda)
    fav2 = Favorito(usuario=luke, planeta=tatooine)

    # Post y comentario
    post = Post(contenido='Yoda es el más sabio.', user_id=1)
    com = Comentario(texto='De acuerdo!', author_id=2, post_id=1)

    # Follows
    follow = Follower(user_from_id=2, user_to_id=1)

    db.session.add_all([luke, leia, yoda, tatooine, fav1, fav2, post, com, follow])
    db.session.commit()

    print("✅ Base de datos creada y poblada.")
