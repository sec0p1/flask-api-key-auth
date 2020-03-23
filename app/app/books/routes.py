"""Book related routes."""

from json import dumps
from app.books import books
from app.auth.wrappers import api_key_required


@books.route('/api/books', methods=['GET'])
@api_key_required
def get_all_books():
    """Get all books endpoint."""
    return [
        {
            'title': 'The Book',
            'year': 2019
        },
        {
            'title': 'Second Book',
            'year': 2020
        }
    ]


@books.route('/', methods=['GET'])
def hello():
    """Example of unathorized route."""
    return {
        'message': 'Hello!'
    }
