#from app import app         # estamos importando la variable app del archivo app.py 
from flask import jsonify, request, Blueprint
from controllers.student_controller import StudentController

student_module = Blueprint('students',__name__)    #esta es la forma en como flask, nos indica a nosotros que podemos tener un submodulo
                                        # con el Blueprint se deja un poco mas limpio, ya puedo quitar los urls /estudiantes 
controller = StudentController()

@student_module.get('/')  #asi se hacen las rutas en flask 
def getStudents():
    return jsonify(controller.get())

@student_module.post('/')
def createStudent():
    result = controller.create(request.get_json())   # tenemos acceso al request
    return jsonify(result.__dict__), 201   # como es de creacion, retorno 201 

# se puede recibir el id del usuario con path parameters, para indicar un path parameter lo indico con <>
@student_module.get('/<string:id>')
def showStudent(id):    #el analiza la ruta y el ve que en la ruta tengo una variable que se llama id, entonces uso el mismo nombre (id va tener el mismo valor que se pase en la ruta)
    return jsonify(controller.getById(id).__dict__)

@student_module.put('/<string:id>')
def updateStudent(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@student_module.delete('/<string:id>')
def deleteStudent(id):
    controller.delete(id)
    return jsonify({}), 204

'''
@student_module.get('/')  #asi se hacen las rutas en flask 
def getStudents():
    return jsonify([
        {
            "id": 1,
            "name": "Andres",
            "lastname": "Gutierrez"
        },
        {
            "id": 2,
            "name": "santi",
            "lastname": "bedo"
        }
    ])
@student_module.post('/')
def createStudent():
    data = request.get_json()   # tenemos acceso al request
    return jsonify(data), 201   # como es de creacion, retorno 201 
# se puede recibir el id del usuario con path parameters, para indicar un path parameter lo indico con <>
@student_module.get('/<string:id>')
def showStudent(id):    #el analiza la ruta y el ve que en la ruta tengo una variable que se llama id, entonces uso el mismo nombre (id va tener el mismo valor que se pase en la ruta)
    return jsonify({
        "id": 1,
        "name": "Andres",
        "lastname": "Gutierrez"
    })
@student_module.put('/<string:id>')
def updateStudent(id):
    return jsonify({}), 204
@student_module.delete('/<string:id>')
def deleteStudent(id):
    return jsonify({}), 204

'''



