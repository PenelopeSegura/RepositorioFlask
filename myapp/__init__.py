from flask import Flask #sirve para crear aplicaciones web con lenguaje de Python
from myapp.config import DevConfig  #configutar el servidor 
from myapp.task.controllers import taskRoute

app = Flask(__name__)  #Crea el objeto global de la aplicación
app.register_blueprint(taskRoute)   #Registra el taskRoute
#app.debug = True

app.config.from_object(DevConfig)  

@app.route('/')         #Ruta más global (raíz) del proyecto 
def hello_world() -> str:
    return ' Hello world'