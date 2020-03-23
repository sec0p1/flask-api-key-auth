"""Auth wrappers module."""

from functools import wraps
from flask import abort, request, current_app


def api_key_required(func):
    """Api key required wrapper."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """Decorate function."""
        registered_api_keys = current_app.config.get('API_KEYS')
        sent_api_key = request.headers.get("Authorization")
        if not sent_api_key or sent_api_key not in registered_api_keys:
            abort(401)

        return func(*args, **kwargs)
    return decorated_function
