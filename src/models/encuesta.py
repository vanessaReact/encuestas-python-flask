from src.config.settings import db
from src.dto.encuesta import EncuestaDTO 
import base64

class Encuesta(db.Model):
    __tablename__ = 'encuesta'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    descripcion=db.Column(db.String(255), nullable=False)
    img=db.Column(db.String(255), nullable=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    parent=db.relationship("User", back_populates="children")
    children=db.relationship("Seccion",back_populates="parent")
    def json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'descripcion':self.descripcion,
	        'img':self.img, 
            'user_id':self.user_id, 
        }
    def add_encuesta(self, encuesta:EncuestaDTO):
        new_encuesta=Encuesta(nombre=encuesta.nombre,descripcion=encuesta.descripcion,
		img=encuesta.img, user_id=encuesta.user_id)
        db.session.add(new_encuesta)
        db.session.commit()

    def get_encuesta(self, id_:int):
        query_result=Encuesta.query.filter_by(id=id_).first()
        return query_result

    def findAll(self):
        query_result=Encuesta.query.all()
        return query_result

    def find_by_user(self,_id):
        query_resolve = Encuesta.query.filter(
            Encuesta.user_id.like(_id),
        )
        return query_resolve

    def update_encuesta(self, id_, encuesta:EncuestaDTO):
        encuesta_update= Encuesta.query.filter_by(id=id_).first()
        encuesta_update.nombre=encuesta.nombre
        encuesta_update.descripcion=encuesta.descripcion
        encuesta_update.img=encuesta.img
        db.session.commit()
    
    def delete_encuesta(self, id_):
        d = Encuesta.query.filter_by(id=id_).delete()
        db.session.commit()
        return d

db.create_all()
db.session.commit()