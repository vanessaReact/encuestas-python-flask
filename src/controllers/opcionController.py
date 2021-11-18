
#dto, modelo
from src.models.opcion import Opcion 
from src.dto.opcion import OpcionDTO 

class OpcionController():
    def create(self,opcionDto:OpcionDTO):
        Opcion().add_opcion(opcionDto)

    def list(self):
        return Opcion().findAll()

    def get(self, id_:int):
        return Opcion().get_opcion(id_)

    def findByPregunta(self, id_encuesta:int):
        return Opcion().finByPregunta(id_encuesta)

    def update(self, id_:int, nombre:str):
        Opcion().update_opcion(id_, nombre)

    def delete(self, id_:int):
        return Opcion().delete_opcion(id_)

