from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.username = 'test_user_' + str(id)
        self.password = 'password'

    def __repr__(self):
        return f'{self.id} : {self.username} : {self.passowrd}'