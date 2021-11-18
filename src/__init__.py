from flask import Flask
from datetime import timedelta
from flask_cors import CORS
from flask_jwt_extended import JWTManager 

app = Flask(__name__, static_url_path = "/static", static_folder = "static")
#CORS(app, resources={r"/api/*":{'origins':'http://localhost:3000'}})
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_mapping(
        SECRET_KEY='dev',
)
app.permanent_session_lifetime=timedelta(minutes=30)

app.config["JWT_SECRET_KEY"]="MY_PROJECT_VANESSA"
jwt=JWTManager(app)


from src.routes import userRoute
from src.routes import encuestaRoute 
from src.routes import seccionRoute
from src.routes import tipoPreguntaRoute
from src.routes import preguntaRoute
from src.routes import opcionRoute
from src.routes import preguntaRespuestaRoute
def create_app():
    app.run(debug=True, port=5000)
