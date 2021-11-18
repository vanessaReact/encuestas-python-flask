from src.controllers.tipoPreguntaController import TipoPreguntaController
from src import app
from flask import json, request, session, Response, jsonify
from src.models.tipo_pregunta import TipoPregunta 
from src.dto.tipo_pregunta import TipoPreguntaDTO 

tipoPreguntaController = TipoPreguntaController()

@app.route('/tipo_pregunta', methods=['POST'])
def crear_tipopregunta():
    if request.method=='POST':
        nombre=request.form["nombre"]

        tipopreguntaDto=TipoPreguntaDTO(
            nombre=nombre,
        )
        crearTipoPregunta=tipoPreguntaController.create(tipopreguntaDto)
    
        return Response('tipopregunta base creada correctamente', 201, mimetype='application/json')

@app.route('/tipo_pregunta')
def obtener_tipopregunta():
    id_=request.args.get('id_')
    tipopregunta=tipoPreguntaController.get(int(id_))
    if(tipopregunta):
        return jsonify(TipoPregunta.json(tipopregunta))
    else:
        return Response('No existe la tipopregunta', 400, mimetype='application/json')
    
@app.route('/tipo_preguntas')
def obtener_todos_tipos_preguntas():
    tipopreguntas=tipoPreguntaController.list()
    return jsonify([TipoPregunta.json(tp) for tp in tipopreguntas])

@app.route('/tipo_pregunta',methods=['PUT'])
def actualizar_tipopregunta():
    if request.method=='PUT':
        id_=request.form['id']
        nombre=request.form['nombre']
        tipoPreguntaController.update(int(id_),nombre)
        response = Response("tipopregunta Actualizada", 201, mimetype='application/json')
        return response       

@app.route('/tipo_pregunta',methods=['DELETE'])
def eliminar_tipopregunta():
    if request.method=='DELETE':
        id_=request.form["id"]
        tipoPreguntaController.delete(int(id_))
        response = Response("tipopregunta eliminada", 201, mimetype='application/json')
        return response  




