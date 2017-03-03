from flask import g
from functools import wraps
from errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps
        def decorated_func(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_func
    return decorator