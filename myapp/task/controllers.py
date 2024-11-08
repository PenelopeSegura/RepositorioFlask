from flask import Blueprint

taskRoute = Blueprint('task', __name__, url_prefix='/task')

#Creacion de rutas en el modulo rutas

@taskRoute.route('/')
def index():
    return 'Index'  #Devuelve una cadena de datos de texto en la ruta definida .../task/

@taskRoute.route('/<int:id>')  #Devuelve un registro específico de acuerdo al id (#)
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    return 'update '+str(id)