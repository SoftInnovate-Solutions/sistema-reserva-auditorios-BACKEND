from flask import Blueprint,jsonify,request
from models.finalModel import FinalModel

main = Blueprint('final_blueprint', __name__)

@main.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    try:
        nombre_usu = request.json['nombre_usu']
        contrasenia_usu = request.json['contrasenia_usu']
        codigo_sis = request.json['codigo_sis_fin']
        usuario_final = FinalModel.iniciar_sesion(nombre_usu,contrasenia_usu,codigo_sis)
        return jsonify(usuario_final)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
