from src.controllers.opcionController import OpcionController
from src import app
from flask import json, request, session, Response, jsonify
from src.models.opcion import Opcion 
from src.dto.opcion import OpcionDTO 

opcionController = OpcionController()

@app.route('/opcion', methods=['POST'])
def crear_opcion():
    if request.method=='POST':
        descripcion=request.form["descripcion"]
        id_pregunta=request.form["id_pregunta"]

        opcionDto=OpcionDTO(
            descripcion=descripcion,
	        id_pregunta=id_pregunta
        )
        crearOpcion=opcionController.create(opcionDto)
    
        return Response('opcion base creada correctamente', 201, mimetype='application/json')

@app.route('/opcion')
def obtener_opcion():
    id_=request.args.get('id_')
    opcion=opcionController.get(int(id_))
    if(opcion):
        return jsonify(Opcion.json(opcion))
    else:
        return Response('No existe la opcion', 400, mimetype='application/json')
    
@app.route('/opciones_pregunta', )
def obtener_por_pregunta():
    id_pregunta=request.args.get("id")
    opcions=opcionController.findByPregunta(int(id_pregunta))
    return jsonify([Opcion.json(opc) for opc in opcions])


@app.route('/opciones')
def obtener_todas_las_opciones():
    opcions=opcionController.list()
    return jsonify([Opcion.json(opc) for opc in opcions])

@app.route('/opcion',methods=['PUT'])
def actualizar_opcion():
    if request.method=='PUT':
        id_=request.form['id']
        descripcion=request.form['descripcion']
        opcionController.update(int(id_),descripcion)
        response = Response("opcion Actualizada", 201, mimetype='application/json')
        return response       

@app.route('/opcion',methods=['DELETE'])
def eliminar_opcion():
    if request.method=='DELETE':
        id_=request.args.get("id")
        opcionController.delete(int(id_))
        response = Response("opcion eliminada", 201, mimetype='application/json')
        return response  




