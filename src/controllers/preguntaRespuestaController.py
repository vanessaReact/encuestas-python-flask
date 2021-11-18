#dto, modelo
from src.models.pregunta_respuesta import PreguntaRespuesta 
from src.dto.pregunta_respuesta import PreguntaRespuestaDTO 


class PreguntaRespuestaController():
    def create(self,preguntarespuestaDto:PreguntaRespuestaDTO):
        PreguntaRespuesta().add_pregunta_respuesta(preguntarespuestaDto)

    def list(self):
        return PreguntaRespuesta().findAll()

    def get(self, id_:int):
        return PreguntaRespuesta().get_pregunta_respuesta(id_)

    def findByPregunta(self, id_encuesta:int):
        return PreguntaRespuesta().finByPregunta(id_encuesta)

    def update(self, id_:int, respuesta:str):
        PreguntaRespuesta().update_pregunta_respuesta(id_, respuesta)

    def delete(self, id_:int):
        return PreguntaRespuesta().delete_pregunta_respuesta(id_)

