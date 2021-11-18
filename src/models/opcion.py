from src.config.settings import db
from src.dto.opcion import OpcionDTO 

class Opcion(db.Model):
    __tablename__ = 'opcion'
    id=db.Column(db.Integer, primary_key=True)
    descripcion=db.Column(db.String(255), nullable=False)
    id_pregunta=db.Column(db.Integer, db.ForeignKey('pregunta.id'))
    parentOpcion=db.relationship("Pregunta", back_populates="childrenOpcion")

    def json(self):
        return {
            'id':self.id,
            'descripcion':self.descripcion,
            'id_pregunta':self.id_pregunta, 
        }
    def add_opcion(self, opcion:OpcionDTO):
        new_opcion=Opcion(descripcion=opcion.descripcion, id_pregunta=opcion.id_pregunta)
        db.session.add(new_opcion)
        db.session.commit()

    def get_opcion(self, id_:int):
        query_result=Opcion.query.filter_by(id=id_).first()
        return query_result

    def findAll(self):
        query_result=Opcion.query.all()
        return query_result

    def finByPregunta(self,id_pregunta:int):
        query_result = Opcion.query.filter_by(id_pregunta=id_pregunta).all()
        return query_result

    def update_opcion(self, id_, descripcion):
        opcion_update= Opcion.query.filter_by(id=id_).first()
        opcion_update.descripcion=descripcion
        db.session.commit()
    
    def delete_opcion(self, id_):
        d = Opcion.query.filter_by(id=id_).delete()
        db.session.commit()
        return d

db.create_all()
db.session.commit()