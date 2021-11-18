
#dto, modelo
from src.models.seccion import Seccion 
from src.dto.seccion import SeccionDTO 


class SeccionController():
    def create(self,seccionDto:SeccionDTO):
        Seccion().add_seccion(seccionDto)

    def list(self):
        return Seccion().findAll()

    def get(self, id_:int):
        return Seccion().get_seccion(id_)

    def findByEncuesta(self, id_encuesta:int):
        return Seccion().finByEncuesta(id_encuesta)

    def update(self, id_:int, nombre:str):
        Seccion().update_seccion(id_, nombre)

    def delete(self, id_:int):
        return Seccion().delete_seccion(id_)

