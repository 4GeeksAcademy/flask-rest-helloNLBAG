from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from models import db, Usuario, Post, Comentario, Follower

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = Usuario.query.filter_by(email=email, password=password).first()
    if not user:
        return jsonify({"msg": "Credenciales inválidas"}), 401

    token = create_access_token(identity=user.id)
    return jsonify(access_token=token), 200

@api.route('/usuario/<int:target_id>/follow', methods=['POST'])
@jwt_required()
def follow_user(target_id):
    user_id = get_jwt_identity()
    if user_id == target_id:
        return jsonify({"msg": "No puedes seguirte a ti mismo"}), 400
    if Follower.query.filter_by(user_from_id=user_id, user_to_id=target_id).first():
        return jsonify({"msg": "Ya estás siguiendo a este usuario"}), 409
    follow = Follower(user_from_id=user_id, user_to_id=target_id)
    db.session.add(follow)
    db.session.commit()
    return jsonify({"msg": f"Siguiendo al usuario {target_id}"}), 201

@api.route('/usuario/<int:user_id>/post', methods=['POST'])
@jwt_required()
def create_post(user_id):
    contenido = request.json.get("contenido")
    post = Post(contenido=contenido, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify({"msg": "Post creado"}), 201

@api.route('/post/<int:post_id>/comentario', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    user_id = get_jwt_identity()
    texto = request.json.get("texto")
    comentario = Comentario(texto=texto, post_id=post_id, author_id=user_id)
    db.session.add(comentario)
    db.session.commit()
    return jsonify({"msg": "Comentario agregado"}), 201
