import json

from flask import jsonify, request
from app import utils
from flask import current_app as app
from .models import db, RequestsModel


@app.route("/")
def index():
    response = jsonify(
        message=(
            "Available routes are: / ; /get_requests , /fibonacci/<int> ; /power/<x>/<y> ; /factorial/<int:n>"
        )
    )
    response.status_code = 200

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response


@app.route("/get_requests")
def get_requests():
    all_data = RequestsModel.query.all()
    print(all_data)
    response = jsonify(all_requests=(str(all_data)))
    response.status_code = 200

    return response


@app.route("/fibonacci/<int:n>")
def fibonacci(n):
    response = jsonify(fibonacci=utils.nth_fibonacci(n))
    response.status_code = 200

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response

