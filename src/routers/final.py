from flask import Blueprint,jsonify,request
from models.finalModel import FinalModel

main = Blueprint('final_blueprint', __name__)

@main.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    try:
        contrasenia_usu = request.json['contrasenia_usu']
        codigo_sis = request.json['codigo_sis_fin']
        usuario_final = FinalModel.iniciar_sesion(contrasenia_usu,codigo_sis)
        return jsonify(usuario_final)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
