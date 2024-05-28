# pep 8
from flask import Blueprint,jsonify,request
from models.ambienteModel import AmbienteModel
from models.entities.ambiente import Ambiente

main = Blueprint('ambiente_blueprint',__name__)

@main.route('/all')
def get_ambientes_all():
    try:
        ambientes = AmbienteModel.get_ambientes_all()
        return jsonify(ambientes)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/one/<id>')
def get_ambiente_one(id):
    try:
        ambiente = AmbienteModel.get_ambiente_one(id)
        if ambiente != None:
            return jsonify(ambiente)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/filter/<filtro>')
def get_ambientes_filter(filtro):
    try:
        ambiente = AmbienteModel.get_ambientes_filter(filtro)
        if ambiente != None:
            return jsonify(ambiente)
        return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_ambiente():
    try:
        nombre_amb = request.json['nombre_amb']
        capacidad_amb = request.json['capacidad_amb']
        ubicacion_amb = request.json['ubicacion_amb']
        descripcion_amb = request.json['descripcion_amb']
        albergacion_max_amb = request.json['albergacion_max_amb']
        albergacion_min_amb = request.json['albergacion_min_amb']
        cod_estado_ambiente = request.json['cod_estado_ambiente']
        cod_piso = request.json['cod_piso']
        cod_edificacion = request.json['cod_edificacion']
        cod_facultad = request.json['cod_facultad']
        cod_tipo_ambiente = request.json['cod_tipo_ambiente']
        ambiente = Ambiente(nombre_amb=str(nombre_amb), capacidad_amb=int(capacidad_amb),ubicacion_amb= str(ubicacion_amb),
                            descripcion_amb= str(descripcion_amb),cod_estado_ambiente=int(cod_estado_ambiente), 
                            cod_piso= int(cod_piso), cod_edificacion = int(cod_edificacion),
                            cod_facultad= int(cod_facultad), cod_tipo_ambiente = int(cod_tipo_ambiente), 
                            albergacion_min_amb=albergacion_min_amb, albergacion_max_amb=albergacion_max_amb)
        affected_rows = AmbienteModel.add_ambiente(ambiente)
        if affected_rows == 1:
            return jsonify(affected_rows)
        return jsonify({'message': "Error al insertar"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_ambiente(id):
    try:
        ambiente = Ambiente(cod_ambiente = id)
        affected_rows = AmbienteModel.delete_ambiente(ambiente)
        if affected_rows == 1:
            return jsonify(ambiente.cod_ambiente)
        else:
            return jsonify({'message': "Ambiente no eliminado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_ambiente(id):
    try:
        nombre_amb = request.json['nombre_amb']
        capacidad_amb = request.json['capacidad_amb']
        ubicacion_amb = request.json['ubicacion_amb']
        descripcion_amb = request.json['descripcion_amb']
        cod_estado_ambiente = request.json['cod_estado_ambiente']
        cod_piso = request.json['cod_piso']
        cod_edificacion = request.json['cod_edificacion']
        cod_facultad = request.json['cod_facultad']
        cod_tipo_ambiente = request.json['cod_tipo_ambiente']
        ambiente = Ambiente(cod_ambiente=id, nombre_amb=nombre_amb, capacidad_amb=capacidad_amb, 
                            ubicacion_amb=ubicacion_amb, descripcion_amb=descripcion_amb,
                            cod_estado_ambiente=cod_estado_ambiente, cod_piso=cod_piso, cod_edificacion=cod_edificacion, 
                            cod_facultad=cod_facultad, cod_tipo_ambiente=cod_tipo_ambiente)
        affected_rows = AmbienteModel.update_ambiente(ambiente)
        if affected_rows == 1:
            return jsonify(ambiente.cod_ambiente)
        else:
            return jsonify({'message': "Error al actualizar el ambiente"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/one_setting/<id>')
def get_one_setting(id):
    try:
        ambiente = AmbienteModel.get_one_setting(id)
        if ambiente != None:
            return jsonify(ambiente)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/update_setting/<id>', methods=['PUT'])
def update_setting_ambiente(id):
    try:
        albergacion_max_amb = request.json['albergacion_max_amb']
        albergacion_min_amb = request.json['albergacion_min_amb']
        ambiente = Ambiente(cod_ambiente=id, albergacion_max_amb=albergacion_max_amb, albergacion_min_amb=albergacion_min_amb)
        affected_rows = AmbienteModel.update_setting_ambiente(ambiente)
        if affected_rows == 1:
            return jsonify(ambiente.cod_ambiente)
        else:
            return jsonify({'message': "Error al actualizar los ajustes del ambiente"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

