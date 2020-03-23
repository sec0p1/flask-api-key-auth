"""Books init."""

from flask import Blueprint

books = Blueprint('books', __name__, template_folder='templates')

from app.books import routes
