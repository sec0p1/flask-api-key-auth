"""Run app script."""

import os
from app import create_app


application = create_app('dev')
if __name__ == '__main__':
    # Run the app.
    application.run()
