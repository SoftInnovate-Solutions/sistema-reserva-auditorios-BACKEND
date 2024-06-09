import multiprocessing
import time
from flask import Flask
from flask_cors import CORS
from config import config
from utils.temporizador import Temporizador
from routers import ambiente, edificacion, facultad, piso, tipo_ambiente, estado_ambiente, bloque, ajuste_ambiente, periodo, final, administrador,reserva,dashboard

app = Flask(__name__)
CORS(app, resources={'*': {'origin': 'http//localhost:5173'}})

def page_not_found(error):
    return '<h1>Not found page</h1>', 404

def run_flask_app():
    app.config.from_object(config['development'])
    app.register_blueprint(ambiente.main, url_prefix='/ambiente')
    app.register_blueprint(edificacion.main, url_prefix='/edificacion')
    app.register_blueprint(facultad.main, url_prefix='/facultad')
    app.register_blueprint(piso.main, url_prefix='/piso')
    app.register_blueprint(tipo_ambiente.main, url_prefix='/tipo_ambiente')
    app.register_blueprint(estado_ambiente.main, url_prefix='/estado_ambiente')
    app.register_blueprint(bloque.main, url_prefix='/bloque')
    app.register_blueprint(ajuste_ambiente.main, url_prefix='/ajuste_ambiente')
    app.register_blueprint(periodo.main, url_prefix='/periodo_reserva')
    app.register_blueprint(final.main, url_prefix='/final')
    app.register_blueprint(administrador.main, url_prefix='/administrador')
    app.register_blueprint(reserva.main, url_prefix='/reserva')
    app.register_blueprint(dashboard.main, url_prefix='/dashboard')
    app.register_error_handler(404, page_not_found)
    app.run()

def hilo():
    while True:
        Temporizador.cerrarPeriodo()
        time.sleep(1)

if __name__ == '__main__':
    contador_process = multiprocessing.Process(target=hilo)
    contador_process.start()

    run_flask_app()
