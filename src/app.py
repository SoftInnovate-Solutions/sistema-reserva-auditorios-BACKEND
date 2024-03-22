from flask import Flask
from flask_cors import CORS
from config import config
from routers import ambiente,edificio,facultad,piso,tipo_ambiente,estado_ambiente

app = Flask(__name__)

CORS(app,resources = {'*': {'origin':'http//localhost:5173'}})

def page_not_found(error):
    return '<h1>Not found page</h1>',404

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(ambiente.main, url_prefix='/ambiente')
    app.register_blueprint(edificio.main, url_prefix='/edificio')
    app.register_blueprint(facultad.main, url_prefix='/facultad')
    app.register_blueprint(piso.main, url_prefix='/piso')
    app.register_blueprint(tipo_ambiente.main, url_prefix='/tipo_ambiente')
    app.register_blueprint(estado_ambiente.main, url_prefix='/estado_ambiente')
    app.register_error_handler(404,page_not_found)
    app.run()

