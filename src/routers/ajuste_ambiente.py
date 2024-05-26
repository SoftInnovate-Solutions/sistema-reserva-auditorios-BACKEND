from flask import Blueprint,jsonify,request
from models.ajuste_ambienteModel import Ajuste_ambienteModel
from models.entities.ajuste_ambiente import Ajuste_Ambiente

main = Blueprint('ajuste_ambiente_blueprint',__name__)

@main.route('/addUpdate', methods=['POST'])
def update_ajuste_ambiente():
    try:
        cod_ambiente = request.json['cod_ambiente']
        configuracion = request.json['configuracion']
        inicio = request.json['fecha_inicio_general_per']
        fin = request.json['fecha_fin_general_per']
        ajuste_ambiente = Ajuste_Ambiente(cod_ambiente=cod_ambiente)
        affected_rows = Ajuste_ambienteModel.update_ajustes_ambiente(ajuste_ambiente,configuracion,(inicio,fin))
        if affected_rows >= 1:
            return jsonify(affected_rows)
        return jsonify({'message': "Error al insertar"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/deleteAll', methods=['DELETE'])
def delete_ajuste_ambiente_all():
    try:
        affected_rows = Ajuste_ambienteModel.delete_ajuste_ambiente_all()
        if affected_rows >= 1:
            return jsonify(affected_rows)
        else:
            return jsonify({'message': "Ajustes no eliminados"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/get_ajuste_ambiente/<id>')
def get_one_setting(id):
    try:
        return jsonify(Ajuste_ambienteModel.get_ajuste_ambiente(id))
    except Exception as ex:
        return jsonify({'message':str(ex)}),500