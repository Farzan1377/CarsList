import os
from flask import Flask


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Makes sure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import users
    from . import shop
    from . import vehicles
    from . import search
    from . import posts
    app.register_blueprint(users.bp)
    app.register_blueprint(shop.bp)
    app.register_blueprint(vehicles.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(posts.bp)

    return app