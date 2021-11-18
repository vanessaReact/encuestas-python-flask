from src.controllers.preguntaRespuestaController import PreguntaRespuestaController
from src import app
from flask import json, request, session, Response, jsonify
from src.models.pregunta_respuesta import PreguntaRespuesta 
from src.dto.pregunta_respuesta import PreguntaRespuestaDTO 

preguntarespuestaController = PreguntaRespuestaController()

@app.route('/pregunta_respuesta', methods=['POST'])
def crear_preguntarespuesta():
    if request.method=='POST':
        respuesta=request.form["respuesta"]
        id_pregunta=request.form["id_pregunta"]

        preguntarespuestaDto=PreguntaRespuestaDTO(
            respuesta=respuesta,
	        id_pregunta=id_pregunta
        )
        crearPreguntaRespuesta=preguntarespuestaController.create(preguntarespuestaDto)
    
        return Response('preguntarespuesta base creada correctamente', 201, mimetype='application/json')

@app.route('/pregunta_respuesta')
def obtener_preguntarespuesta():
    id_=request.args.get('id_')
    preguntarespuesta=preguntarespuestaController.get(int(id_))
    if(preguntarespuesta):
        return jsonify(PreguntaRespuesta.json(preguntarespuesta))
    else:
        return Response('No existe la preguntarespuesta', 400, mimetype='application/json')
    
@app.route('/pregunta_respuestas', methods=['POST'])
def obtener_respuestas_por_pregunta():
    if request.method=='POST':
        id_pregunta=request.form["id_pregunta"]
        preguntarespuestas=preguntarespuestaController.findByPregunta(int(id_pregunta))
        return jsonify([PreguntaRespuesta.json(prs) for prs in preguntarespuestas])


@app.route('/pregunta_respuestas')
def obtener_todas_las_respuestas():
    preguntarespuestas=preguntarespuestaController.list()
    return jsonify([PreguntaRespuesta.json(prs) for prs in preguntarespuestas])

@app.route('/pregunta_respuesta',methods=['PUT'])
def actualizar_preguntarespuesta():
    if request.method=='PUT':
        id_=request.form['id']
        respuesta=request.form['respuesta']
        preguntarespuestaController.update(int(id_),respuesta)
        response = Response("preguntarespuesta Actualizada", 201, mimetype='application/json')
        return response       

@app.route('/pregunta_respuesta',methods=['DELETE'])
def eliminar_preguntarespuesta():
    if request.method=='DELETE':
        id_=request.form["id"]
        preguntarespuestaController.delete(int(id_))
        response = Response("preguntarespuesta eliminada", 201, mimetype='application/json')
        return response  




