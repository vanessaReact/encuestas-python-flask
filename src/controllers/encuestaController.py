
#dto, modelo
from src.models.encuesta import Encuesta 
from src.dto.encuesta import EncuestaDTO 


class EncuestaController():
    def create(self,encuestaDto:EncuestaDTO):
        Encuesta().add_encuesta(encuestaDto)

    def list(self):
        return Encuesta().findAll()

    def get(self, id_:int):
        return Encuesta().get_encuesta(id_)

    def findByUser(self, id_:int):
        return Encuesta().find_by_user(id_)

    def update(self, id_:int, encuesta:EncuestaDTO):
        Encuesta().update_encuesta(id_, encuesta)

    def delete(self, id_:int):
        return Encuesta().delete_encuesta(id_)

