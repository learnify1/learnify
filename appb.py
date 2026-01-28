from flask import Flask
from Controllersb.controladorb import blueprint_home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_home, url_prefix='/api/v1')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host=('0.0.0.0'))
