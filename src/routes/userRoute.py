#controlador, #app, flask, response,dto, 
from src.controllers.auth.userController import UserController
from src import app
from flask import json, request, session, Response, jsonify, make_response
from src.models.user import User
from src.dto.user import UserDTO
import hashlib
userController = UserController()

from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity



@app.route('/api/register', methods=['POST'])
def registrar_usuario():
    validation=''
    if request.method=='POST':
        user=request.json['user']

        nombre=user["nombre"]
        email=user["email"]
        contrasenia=user["contrasenia"]

    if(userController.userFound(nombre)):
            validation="El nombre de usuario ya existe en la base de datos, elige otro porfavor"
            return Response(validation, 401, mimetype='application/json')
    else:
        validation="Usuario creado, Puedes Iniciar Sesion"
        #contrasenia encryptada
        h=hashlib.new("sha1",str(contrasenia).encode('utf-8'))
        password=h.hexdigest()
        #agregamos el nuevo usuario a la base de datos
        userDto=UserDTO(
            nombre=str(nombre),
            email=str(email),
            contrasenia=str(password)
        )
        crearUsuario=userController.create(userDto)
        return Response(validation, 201, mimetype='application/json')

@app.route('/api/login', methods=['POST'])
def iniciar_sesion():
    validation=""
    if(request.method=="POST"):
        user=request.json['user']

        nombre=user['nombre']
        contrasenia=user['contrasenia']

        #filtrar por nombre y contrasenia en la db
        h=hashlib.new("sha1",str(contrasenia).encode('utf-8'))
        password=h.hexdigest()
        userdto=UserDTO(str(nombre),"",str(password))
        resolve_user=userController.authUser(userdto)
        if(resolve_user):
            session.permanent=True
            session["user"]=resolve_user.nombre
            session["id"]=resolve_user.id
            token=create_access_token(identity=resolve_user.id)

            #Agregamos proteccion mediante JWT
            return make_response(jsonify({
                "token":token
            }
            ),200)
            #return jsonify(User.json(resolve_user))

        else:
            validation="Nombre de usuario o contraseña incorrectos"
            return Response(validation, 401, mimetype='application/json')

@app.route('/api/logout')
def logout():
    session.pop("user",None)
    session.pop("id",None)
    return Response('sesion cerrada correctamente', 201, mimetype='application/json')

@app.route('/auth')
def auth():
    if "user" in session:
        user=session["user"]
        return Response(user, 201, mimetype='application/json')
    return Response("No hay un usuario en la sesion", 400, mimetype='application/json')


@app.route('/api/user/<int:userId>', methods=['GET'])
def get_user(userId):
    user = userController.getUser(userId)
    if(user):
        return make_response(jsonify(User.json(user)),200)
    else:
        return make_response(jsonify({
            "message":"Error al traer el usuario"
        }), 400)
    