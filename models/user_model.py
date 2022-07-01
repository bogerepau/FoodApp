from werkzeug.security import generate_password_hash, check_password_hash


class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = False

    def check_password(self, password):
        return check_password_hash(self.password, password)
