from app import app
from app.decorators import is_json, validate_json


@app.route("/")
def home():
    return {"message": "Hello Flask!"}


@app.route("/service", methods=["POST"])
@is_json
@validate_json
def service():
    return {"success": True}
