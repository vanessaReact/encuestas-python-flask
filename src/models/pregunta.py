from src.config.settings import db
from src.dto.pregunta import PreguntaDTO 

class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    id=db.Column(db.Integer, primary_key=True)
    pregunta=db.Column(db.String(255), nullable=False)
    id_seccion=db.Column(db.Integer, db.ForeignKey('seccion.id'))
    id_tipo_pregunta=db.Column(db.Integer, db.ForeignKey('tipo_pregunta.id'))
    parent1=db.relationship("TipoPregunta", back_populates="children1")
    parent2=db.relationship("Seccion", back_populates="children2")
    childrenOpcion=db.relationship("Opcion",back_populates="parentOpcion")
    childrenPregunta=db.relationship("PreguntaRespuesta",back_populates="parentPregunta")

    def json(self):
        return {
            'id':self.id,
            'pregunta':self.pregunta,
            'id_seccion':self.id_seccion, 
            'id_tipo_pregunta':self.id_tipo_pregunta, 
        }
    def add_pregunta(self, preguntaDto:PreguntaDTO):
        new_pregunta=Pregunta(pregunta=preguntaDto.pregunta, id_seccion=preguntaDto.id_seccion, id_tipo_pregunta=preguntaDto.id_tipo_pregunta)
        db.session.add(new_pregunta)
        db.session.commit()

    def get_pregunta(self, id_:int):
        query_result=Pregunta.query.filter_by(id=id_).first()
        return query_result

    def findAll(self):
        query_result=Pregunta.query.all()
        return query_result

    def finBySeccion(self,id_seccion:int):
        query_result = Pregunta.query.filter_by(id_seccion=id_seccion).all()
        return query_result

    def update_pregunta(self, id_, pregunta:PreguntaDTO):
        pregunta_update= Pregunta.query.filter_by(id=id_).first()
        pregunta_update.pregunta=pregunta.pregunta
        pregunta_update.id_tipo_pregunta=pregunta.id_tipo_pregunta
        db.session.commit()
    
    def delete_pregunta(self, id_):
        d = Pregunta.query.filter_by(id=id_).delete()
        db.session.commit()
        return d

db.create_all()
db.session.commit()