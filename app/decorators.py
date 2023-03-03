from flask import request
from functools import wraps
from schema import Schema, Regex, SchemaError


def is_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return {"success": False}, 400
        return f(*args, **kwargs)

    return wrapper


schema = Schema(
    {
        "email_address": Regex(r"^[a-z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$"),
        "username": Regex(r"^[a-zA-Z]{1}[a-zA-Z0-9_.-]{2,}"),
    }
)


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            schema.validate(request.json)
            return f(*args, **kwargs)
        except SchemaError as s:
            return {"success": False, "message": str(s)}, 400

    return wrapper
