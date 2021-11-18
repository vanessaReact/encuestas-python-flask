
#dto, modelo
from src.models.tipo_pregunta import TipoPregunta 
from src.dto.tipo_pregunta import TipoPreguntaDTO 


class TipoPreguntaController():
    def create(self,tipopreguntaDto:TipoPreguntaDTO):
        TipoPregunta().add_tipo_pregunta(tipopreguntaDto)

    def list(self):
        return TipoPregunta().findAll()

    def get(self, id_:int):
        return TipoPregunta().get_tipo_pregunta(id_)

    def update(self, id_:int, nombre:str):
        TipoPregunta().update_tipo_pregunta(id_, nombre)

    def delete(self, id_:int):
        return TipoPregunta().delete_tipo_pregunta(id_)

