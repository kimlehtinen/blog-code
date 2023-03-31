from flask import Flask
from flask_migrate import Migrate
from src.di.di_container import DI
from db import db


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from src.web import post_routes
    container = DI()
    container.wire(modules=[post_routes])
    app.container = container

    from src.infra.models import post_model
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(post_routes.post_api, url_prefix="/post")

    return app
