from flask import jsonify
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt


def expect(ns, model, exclude_fields=[], name_suffix="Input"):
    """
    Returns a decorator like @ns.expect(), but removes specified fields from the model.
    """

    def decorator(func):
        # Clone and remove specified fields
        input_model = ns.clone(model.name + name_suffix, model)
        for field in exclude_fields:
            input_model.pop(field, None)

        # Apply the modified model with ns.expect
        return ns.expect(input_model)(func)

    return decorator


def role(allowed_roles):
    """
    Protect routes based on roles.
    """

    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            claims = get_jwt()
            user_role = claims["role"]

            if user_role not in allowed_roles:
                response = jsonify(
                    {"message": "Access forbidden: insufficient permissions"}
                )
                response.status_code = 403
                return response

            return f(*args, **kwargs)

        return decorated_function

    return decorator
