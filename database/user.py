from flask_login import UserMixin
from app import db

import json

from os import urandom
from hashlib import pbkdf2_hmac

SALT_LENGTH = 48
HASH_ITERATIONS = 200000

#Change the pepper before deployment!!!
with open('database\config.json') as config_file:
    PEPPER = bytes.fromhex(
        json.loads(
            config_file.read()
        )['security']['pepper']
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(120), unique = False, nullable = False)
    salt = db.Column(db.String(SALT_LENGTH), unique = False, nullable = False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(kwargs['password'])        

    def set_password(self, password):
        password = password.encode('utf-8')
        self.salt = urandom(SALT_LENGTH)
        spices = self.salt + PEPPER
        self.password = pbkdf2_hmac('sha512', password = password, salt = spices, iterations = HASH_ITERATIONS)

    def verify_password(self, password):
        password = password.encode('utf-8')
        spices = self.salt + PEPPER
        return self.password == pbkdf2_hmac('sha512', password = password, salt = spices, iterations = HASH_ITERATIONS)

    def __repr__(self):
        return f'{self.username}'