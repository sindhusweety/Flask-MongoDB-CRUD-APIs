from flask import Flask

#application factory function
def create_app():
    app = Flask(__name__)


    from . import crud_api
    app.register_blueprint(crud_api.crud_api)

    from . import db
    return app

