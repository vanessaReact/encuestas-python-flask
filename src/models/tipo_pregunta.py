from src.config.settings import db
from src.dto.tipo_pregunta import TipoPreguntaDTO 

class TipoPregunta(db.Model):
    __tablename__ = 'tipo_pregunta'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    #parent=db.relationship("Encuesta", back_populates="children")
    children1=db.relationship("Pregunta",back_populates="parent1")

    def json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
        }
    def add_tipo_pregunta(self, tipopregunta:TipoPreguntaDTO):
        new_tipopregunta=TipoPregunta(nombre=tipopregunta.nombre)
        db.session.add(new_tipopregunta)
        db.session.commit()

    def get_tipo_pregunta(self, id_:int):
        query_result=TipoPregunta.query.filter_by(id=id_).first()
        return query_result

    def findAll(self):
        query_result=TipoPregunta.query.all()
        return query_result

    def update_tipo_pregunta(self, id_, nombre):
        tipopregunta_update= TipoPregunta.query.filter_by(id=id_).first()
        tipopregunta_update.nombre=nombre
        db.session.commit()
    
    def delete_tipo_pregunta(self, id_):
        d = TipoPregunta.query.filter_by(id=id_).delete()
        db.session.commit()
        return d

db.create_all()
db.session.commit()