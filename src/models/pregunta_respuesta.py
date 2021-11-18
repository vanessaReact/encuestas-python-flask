from src.config.settings import db
from src.dto.pregunta_respuesta import PreguntaRespuestaDTO 

class PreguntaRespuesta(db.Model):
    __tablename__ = 'pregunta_respuesta'
    id=db.Column(db.Integer, primary_key=True)
    respuesta=db.Column(db.String(255), nullable=False)
    id_pregunta=db.Column(db.Integer, db.ForeignKey('pregunta.id'))
    parentPregunta=db.relationship("Pregunta", back_populates="childrenPregunta")

    def json(self):
        return {
            'id':self.id,
            'respuesta':self.respuesta,
            'id_pregunta':self.id_pregunta, 
        }
    def add_pregunta_respuesta(self, preguntarespuesta:PreguntaRespuestaDTO):
        new_preguntarespuesta=PreguntaRespuesta(respuesta=preguntarespuesta.respuesta, id_pregunta=preguntarespuesta.id_pregunta)
        db.session.add(new_preguntarespuesta)
        db.session.commit()

    def get_pregunta_respuesta(self, id_:int):
        query_result=PreguntaRespuesta.query.filter_by(id=id_).first()
        return query_result

    def findAll(self):
        query_result=PreguntaRespuesta.query.all()
        return query_result

    def finByPregunta(self,id_pregunta:int):
        query_result = PreguntaRespuesta.query.filter_by(id_pregunta=id_pregunta).all()
        return query_result

    def update_pregunta_respuesta(self, id_, respuesta):
        preguntarespuesta_update= PreguntaRespuesta.query.filter_by(id=id_).first()
        preguntarespuesta_update.respuesta=respuesta
        db.session.commit()
    
    def delete_pregunta_respuesta(self, id_):
        d = PreguntaRespuesta.query.filter_by(id=id_).delete()
        db.session.commit()
        return d

db.create_all()
db.session.commit()