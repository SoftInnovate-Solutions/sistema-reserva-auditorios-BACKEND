from flask import Blueprint,jsonify,request
from models.reservaModel import ReservaModel
from models.entities.reserva import Reserva

main = Blueprint('reserva_blueprint', __name__)

@main.route('/all/<id>')
def get_reservas(id):
    try:
        reservas = ReservaModel.get_reservas(id)
        return jsonify(reservas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_reserva(id):
    try:
        reserva = Reserva(cod_reserva = id)
        affected_rows = ReservaModel.delete_reserva(reserva)
        if affected_rows == 1:
            return jsonify(reserva.cod_reserva)
        return jsonify({'message': "Ambiente no eliminado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/one/<id>')
def get_reserva(id):
    try:
        reserva = ReservaModel.get_reserva(id)
        return jsonify(reserva)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500