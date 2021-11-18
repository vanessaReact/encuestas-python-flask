class PreguntaRespuestaDTO():
    respuesta:str
    id_pregunta:int
    def __init__(self,respuesta,id_pregunta):
        self.respuesta=respuesta
        self.id_pregunta=id_pregunta