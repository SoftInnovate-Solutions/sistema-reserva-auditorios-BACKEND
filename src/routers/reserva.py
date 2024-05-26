from flask import Blueprint,jsonify,request
from models.reservaModel import ReservaModel

main = Blueprint('reserva_blueprint', __name__)

@main.route('/all/<id>')
def get_reservas(id):
    try:
        reservas = ReservaModel.get_reservas(id)
        return jsonify(reservas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
