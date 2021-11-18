class PreguntaDTO():
    pregunta:str
    id_seccion:int
    id_tipo_pregunta:int
    def __init__(self,pregunta,id_seccion,id_tipo_pregunta):
        self.pregunta=pregunta
        self.id_seccion=id_seccion
        self.id_tipo_pregunta=id_tipo_pregunta