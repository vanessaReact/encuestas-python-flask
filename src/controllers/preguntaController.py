
#dto, modelo
from src.models.pregunta import Pregunta 
from src.dto.pregunta import PreguntaDTO 


class PreguntaController():
    def create(self,preguntaDto:PreguntaDTO):
        Pregunta().add_pregunta(preguntaDto)

    def list(self):
        return Pregunta().findAll()

    def get(self, id_:int):
        return Pregunta().get_pregunta(id_)

    def findBySeccion(self,id_seccion:int):
        return Pregunta().finBySeccion(id_seccion)

    def update(self, id_:int, pregunta:PreguntaDTO):
        Pregunta().update_pregunta(id_, pregunta)

    def delete(self, id_:int):
        return Pregunta().delete_pregunta(id_)

