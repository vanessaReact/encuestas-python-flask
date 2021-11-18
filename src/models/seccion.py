from src.config.settings import db
from src.dto.seccion import SeccionDTO 

class Seccion(db.Model):
    __tablename__ = 'seccion'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    id_encuesta=db.Column(db.Integer, db.ForeignKey('encuesta.id'))
    parent=db.relationship("Encuesta", back_populates="children")
    children2=db.relationship("Pregunta",back_populates="parent2")

    def json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'id_encuesta':self.id_encuesta, 
        }
    def add_seccion(self, seccion:SeccionDTO):
        new_seccion=Seccion(nombre=seccion.nombre, id_encuesta=seccion.encuesta_id)
        db.session.add(new_seccion)
        db.session.commit()

    def get_seccion(self, id_:int):
        query_result=Seccion.query.filter_by(id=id_).first()
        return query_result

    def findAll(self):
        query_result=Seccion.query.all()
        return query_result
    def finByEncuesta(self,id_encuesta:int):
        query_result = Seccion.query.filter_by(id_encuesta=id_encuesta).all()
        return query_result

    def update_seccion(self, id_, nombre):
        seccion_update= Seccion.query.filter_by(id=id_).first()
        seccion_update.nombre=nombre
        db.session.commit()
    
    def delete_seccion(self, id_):
        d = Seccion.query.filter_by(id=id_).delete()
        db.session.commit()
        return d

db.create_all()
db.session.commit()