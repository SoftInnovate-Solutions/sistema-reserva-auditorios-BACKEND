from flask import Blueprint,jsonify,request
from models.dashboard_model import Dashboard_Model

main = Blueprint('dashboard_blueprint',__name__)

@main.route('/reporte_ambientes', methods=['POST'])
def reporte_ambientes():
    try:
        fecha_inicio = request.json['fecha_inicio']
        fecha_fin = request.json['fecha_fin']
        return Dashboard_Model.get_reporte_ambientes(fecha_ini = fecha_inicio, fecha_fin = fecha_fin)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/reporte_docentes', methods=['POST'])
def reporte_docentes():
    try:
        fecha_inicio = request.json['fecha_inicio']
        fecha_fin = request.json['fecha_fin']
        return Dashboard_Model.get_reporte_docentes(fecha_ini = fecha_inicio, fecha_fin = fecha_fin)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

