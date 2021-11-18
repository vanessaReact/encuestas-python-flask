#controlador, #app, flask, response,dto, 
from src.controllers import encuestaController
from src.controllers.encuestaController import EncuestaController 
from src import app
from flask import json, request, session, Response, jsonify, redirect, url_for
from src.models.encuesta import Encuesta 
from src.dto.encuesta import EncuestaDTO 
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath

UPLOAD_FOLDER='static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

encuestaController = EncuestaController()

@app.route('/encuesta', methods=['POST'])
def crear_encuesta():
    if request.method=='POST':
        nombre=request.form["nombre"]
        descripcion=request.form["descripcion"]
        user_id=request.form["user_id"]

        file=request.files["img"]

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.root_path, "static/uploads/", filename))
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img_url='http://127.0.0.1:5000/static/uploads/'+filename 

        encuestaDto=EncuestaDTO(
            nombre=str(nombre),
            descripcion=str(descripcion),
            img=str(img_url),
	        user_id=int(user_id)
        )
        crearEncuesta=encuestaController.create(encuestaDto)
    
        return Response('Encuesta base creada correctamente', 201, mimetype='application/json')

@app.route('/encuesta')
def obtener_encuesta():
    id_=request.args.get('id_')
    encuesta=encuestaController.get(int(id_))
    if(encuesta):
        return jsonify(Encuesta.json(encuesta))
    else:
        return Response('No existe la encuesta', 400, mimetype='application/json')
    
@app.route('/encuestas_usuario')
def obtener_por_usuario():
    id_=request.args.get('id')
    encuestas=encuestaController.findByUser(int(id_))
    return jsonify([Encuesta.json(enc) for enc in encuestas])


@app.route('/encuestas')
def obtener_todo():
    encuestas=encuestaController.list()
    return jsonify([Encuesta.json(enc) for enc in encuestas])

@app.route('/encuesta',methods=['PUT'])
def actualizar_encuesta():
    if request.method=='PUT':
        id_=request.form['id']
        nombre=request.form['nombre']
        descripcion=request.form['descripcion']
        file=request.files['img']

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.root_path, "static/uploads/", filename))

        img_url='http://127.0.0.1:5000/static/uploads/'+filename 
        encuestaDto=EncuestaDTO(
            nombre=nombre,
            descripcion=descripcion,
            img=img_url,
            user_id=None
        )

        encuestaController.update(int(id_),encuestaDto)

        response = Response("Encuesta Actualizada", 201, mimetype='application/json')
        return response       

@app.route('/encuesta',methods=['DELETE'])
def eliminar_encuesta():
    if request.method=='DELETE':
        #id_=request.form['id']
        id_=request.args.get('id')
        encuestaController.delete(int(id_))
        response = Response("Encuesta eliminada", 201, mimetype='application/json')
        return response  




