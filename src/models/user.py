from src.config.settings import db
from src.dto.user import UserDTO
#from src.models.short_path import ShortPath
#from src.models.encuesta import Encuesta 
class User(db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    contrasenia=db.Column(db.String(255), nullable=False)
    children=db.relationship("Encuesta",back_populates="parent")


    def json(self):
        return {
            'id':self.id, 'nombre':self.nombre,
            'email':self.email, 'contrasenia':self.contrasenia
        }
    def add_user(self, user:UserDTO):
        new_user=User(nombre=user.nombre,email=user.email,contrasenia=user.contrasenia)
        db.session.add(new_user)
        db.session.commit()

    def user_exits(self, user:UserDTO):
        query_resolve = User.query.filter(
        db.and_(
            User.nombre.like(user.nombre),
            User.contrasenia.like(user.contrasenia)
            )
        ).first()
        
        return query_resolve

        
    def user_exits_by_name(self, name_user):
        quuery_resolve = User.query.filter(User.nombre.like(name_user)).first()
        return quuery_resolve
    
    def get_user_by_id(self, id):
        user=User.query.filter_by(id=id).first()
        return user

db.create_all()
db.session.commit()
    