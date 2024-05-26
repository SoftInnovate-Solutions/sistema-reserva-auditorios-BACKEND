from flask import Blueprint,jsonify,request
from models.periodoModel import PeriodoModel
from models.entities.periodo_reserva import Periodo_Reserva

main = Blueprint('periodo_blueprint',__name__)

@main.route('/all')
def get_periodos_all():
    try:
        periodos = PeriodoModel.get_periodos_all()
        return jsonify(periodos)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/one/<id>')
def get_periodo_one(id):
    try:
        periodo = PeriodoModel.get_periodo_one(id)
        if periodo != None:
            return jsonify(periodo)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500






@main.route('/add', methods=['POST'])
def add_periodo():
    try:
        fecha_inicio_general_per = request.json['fecha_inicio_general_per']
        fecha_fin_general_per = request.json['fecha_fin_general_per']
        fecha_inicio_docente_per = request.json['fecha_inicio_docente_per']
        fecha_fin_docente_per = request.json['fecha_fin_docente_per']
        fecha_inicio_auxiliar_per = request.json['fecha_inicio_auxiliar_per']
        fecha_fin_auxiliar_per = request.json['fecha_fin_auxiliar_per']
        notificacion_per = request.json['notificacion_per']

        periodo = Periodo_Reserva(fecha_inicio_general_per = fecha_inicio_general_per, fecha_fin_general_per = fecha_fin_general_per,
                          fecha_inicio_docente_per = fecha_inicio_docente_per, fecha_fin_docente_per = fecha_fin_docente_per,
                          fecha_inicio_auxiliar_per = fecha_inicio_auxiliar_per, fecha_fin_auxiliar_per = fecha_fin_auxiliar_per,
                          notificacion_per = notificacion_per, estado_visualizacion_per = True)
        affected_rows = PeriodoModel.add_periodo(periodo)
        if affected_rows == 1:
            return jsonify(affected_rows)
        else:
            return jsonify({'message': "Error al insertar"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/periodo_general')
def get_periodo_general():
    try:
        periodo = PeriodoModel.get_periodo_general()
        return jsonify(periodo)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/periodo_docente')
def get_periodo_docente():
    try:
        periodo = PeriodoModel.get_periodo_docente()
        return jsonify(periodo)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@main.route('/periodo_auxiliar')
def get_periodo_auxiliar():
    try:
        periodo = PeriodoModel.get_periodo_auxiliar()
        return jsonify(periodo)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_periodo(id):
    try:
        periodo_reserva = Periodo_Reserva(id)
        affected_rows = PeriodoModel.delete_periodo(periodo_reserva)
        if affected_rows >= 1:
            return jsonify(periodo_reserva.cod_periodo_reserva)
        else:
            return jsonify({'message': "Periodo no eliminado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_periodo(id):
    try:
        fecha_inicio_general_per = request.json['fecha_inicio_general_per']
        fecha_fin_general_per = request.json['fecha_fin_general_per']
        fecha_inicio_docente_per = request.json['fecha_inicio_docente_per']
        fecha_fin_docente_per = request.json['fecha_fin_docente_per']
        fecha_inicio_auxiliar_per = request.json['fecha_inicio_auxiliar_per']
        fecha_fin_auxiliar_per = request.json['fecha_fin_auxiliar_per']

        periodo = Periodo_Reserva(cod_periodo_reserva=id, fecha_inicio_general_per= fecha_inicio_general_per,
                                  fecha_fin_general_per = fecha_fin_general_per, fecha_inicio_docente_per=fecha_inicio_docente_per,
                                  fecha_fin_docente_per = fecha_fin_docente_per, fecha_inicio_auxiliar_per = fecha_inicio_auxiliar_per,
                                  fecha_fin_auxiliar_per= fecha_fin_auxiliar_per
                                  )
        affected_rows = PeriodoModel.update_periodo(periodo)
        if affected_rows == 1:
            return jsonify(periodo.cod_periodo_reserva)
        else:
            return jsonify({'message': "Error al actualizar el periodo"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

