
#dto, modelo
from re import L
from src.models.user import User
from src.dto.user import UserDTO 


class UserController():
    def create(self,userDto:UserDTO):
        User().add_user(userDto)

    def userFound(self, nombre):
        user_valid=User().user_exits_by_name(str(nombre))
        if(user_valid):
            return True
        return False
    
    def authUser(self, userDto:UserDTO):
        resolve_user=User().user_exits(userDto)
        return resolve_user
    
    def getUser(self, id):
        user = User().get_user_by_id(id)
        return user