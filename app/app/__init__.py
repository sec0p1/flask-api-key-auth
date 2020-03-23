"""Root package."""

import os
from flask_api import FlaskAPI


def create_app(config_type):
    """App factory.

    Args:
        config_type: Name of the config file without extension.
    Returns:
        App object.

    """

    # Get root dir path to craete a path to the config file.
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.abspath(os.path.join(curr_dir, os.pardir))

    # Create app with specified configuration.
    app = FlaskAPI(__name__)
    configuration = os.path.join(root_dir, 'config', str(config_type) + '.py')
    app.config.from_pyfile(configuration)

    # Import and register blueprints.
    from app.auth import authentication
    from app.books import books

    # Register blueprints.
    app.register_blueprint(authentication)
    app.register_blueprint(books)

    return app
