from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __table__ = db.Model.metadata.tables['user']

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class City(db.Model):
    __table__ = db.Model.metadata.tables['city']


class Forecast(db.Model):
    __table__ = db.Model.metadata.tables['forecast']
