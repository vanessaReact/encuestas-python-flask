from src.controllers.preguntaController import PreguntaController
from src import app
from flask import json, request, session, Response, jsonify
from src.models.pregunta import Pregunta 
from src.dto.pregunta import PreguntaDTO 

preguntaController = PreguntaController()

@app.route('/pregunta', methods=['POST'])
def crear_pregunta():
    if request.method=='POST':
        pregunta=request.form["pregunta"]
        id_seccion=request.form["id_seccion"]
        id_tipo_pregunta=request.form["id_tipo_pregunta"]

        preguntaDto=PreguntaDTO(
            pregunta=pregunta,
            id_seccion=int(id_seccion),
	        id_tipo_pregunta=int(id_tipo_pregunta)
        )
        crearPregunta=preguntaController.create(preguntaDto)
    
        return Response('pregunta base creada correctamente', 201, mimetype='application/json')

@app.route('/pregunta')
def obtener_pregunta():
    id_=request.args.get('id_')
    pregunta=preguntaController.get(int(id_))
    if(pregunta):
        return jsonify(Pregunta.json(pregunta))
    else:
        return Response('No existe la pregunta', 400, mimetype='application/json')
    
@app.route('/preguntas_seccion')
def obtener_por_seccion():
        id_seccion=request.args.get("id")
        preguntas=preguntaController.findBySeccion(int(id_seccion))
        return jsonify([Pregunta.json(prg) for prg in preguntas])


@app.route('/preguntas')
def obtener_todas_las_preguntas():
    preguntas=preguntaController.list()
    return jsonify([Pregunta.json(prg) for prg in preguntas])

@app.route('/pregunta',methods=['PUT'])
def actualizar_pregunta():
    if request.method=='PUT':
        id_=request.form['id']
        pregunta=request.form['pregunta']
        id_tipo_pregunta=request.form['id_tipo_pregunta']

        preguntaDto=PreguntaDTO(
            pregunta=pregunta,
            id_seccion=None,
            id_tipo_pregunta=id_tipo_pregunta
        )

        preguntaController.update(int(id_),preguntaDto)
        response = Response("pregunta Actualizada", 201, mimetype='application/json')
        return response       

@app.route('/pregunta',methods=['DELETE'])
def eliminar_pregunta():
    if request.method=='DELETE':
        id_=request.args.get("id")
        preguntaController.delete(int(id_))
        response = Response("pregunta eliminada", 201, mimetype='application/json')
        return response  




