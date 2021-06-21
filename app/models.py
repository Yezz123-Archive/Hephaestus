from . import db


class RequestsModel(db.Model):
    __tablename__ = "requests_model"
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String(200))
    response = db.Column((db.String(200)))

    def __init__(self, request, response):
        self.request = request
        self.response = response

    def __repr__(self):
        return " Request was {}. Response was: {}".format(self.request, self.response)
