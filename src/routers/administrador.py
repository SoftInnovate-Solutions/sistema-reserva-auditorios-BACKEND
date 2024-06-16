from flask import Blueprint,jsonify,request
from models.administradorModel import AdministradorModel

main = Blueprint('administrador_blueprint', __name__)

@main.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    try:
        nombre_usu = request.json['nombre_usu']
        contrasenia_usu = request.json['contrasenia_usu']
        usuario_final = AdministradorModel.iniciar_sesion(nombre_usu,contrasenia_usu)
        return jsonify(usuario_final)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

