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
        return jsonify({'message': "Reserva no eliminado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/one/<id>')
def get_reserva(id):
    try:
        reserva = ReservaModel.get_reserva(id)
        return jsonify(reserva)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/imparticiones/<id>')
def get_imparticiones(id):
    try:
        imparticiones = ReservaModel.get_imparticiones(id)
        return jsonify(imparticiones)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/ambientes_disponibles/<cantidad>')
def ambientes_disponibles(cantidad):
    try:
        ambientes = ReservaModel.get_ambientes_disponibles(cantidad)
        return jsonify(ambientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/get_calendario/<id>')
def get_calendario(id):
    try:
        fechas = ReservaModel.get_calendario(id)
        return jsonify(fechas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/get_bloque', methods=['POST'])
def get_bloque():
    try:
        cod_ambiente = request.json['cod_ambiente']
        fecha_aa = request.json['fecha_aa']
        return jsonify(ReservaModel.get_bloque(cod_ambiente,fecha_aa))
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add_reserva', methods=['POST'])
def add_reserva():
    try:
        cod_usuario = request.json['cod_usuario']
        cod_grupo = request.json['cod_grupo']
        cod_materia = request.json['cod_materia']
        cod_ambiente = request.json['cod_ambiente']
        cod_dia = request.json['cod_dia']
        cod_bloque = request.json['cod_bloque']
        fecha_res = request.json['fecha_res']
        cantidad_estudiantes_res = request.json['cantidad_estudiantes_res']
        cantidad_estudiantes_res_total = request.json['cantidad_estudiantes_res_total']
        return jsonify(ReservaModel.add_reserva(cod_usuario, cod_grupo, cod_materia, cod_ambiente, cod_dia, cod_bloque, fecha_res, cantidad_estudiantes_res, cantidad_estudiantes_res_total))
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/get_history_all')
def get_history_all():
    print("aa")
    try:
        print("aa")
        history = ReservaModel.get_history_all()
        return jsonify(history)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/get_history_one/<id>')
def get_history_one(id):
    try:
        historia = ReservaModel.get_history_one(id)
        return jsonify(historia)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
