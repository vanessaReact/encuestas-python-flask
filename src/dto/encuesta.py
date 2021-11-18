class EncuestaDTO():
    nombre:str
    descripcion:str
    img:str
    user_id:int
    def __init__(self,nombre,descripcion,img,user_id):
        self.nombre=nombre
        self.descripcion=descripcion
        self.img=img
        self.user_id=user_id