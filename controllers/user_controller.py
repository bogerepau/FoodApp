import datetime
from functools import wraps
from psycopg2.extensions import AsIs
import jwt
from flask import request, jsonify
from models.user_model import User
from models.db_conn import DBConnection

db = DBConnection()

secrete_key = 'B)36#oot8&"camÄäp'


def encode_token(user_id):
    token = jwt.encode({'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, secrete_key).decode('utf-8')
    return token


def decode_token(token):
    decoded_token = jwt.decode(token, secrete_key, algorithms=['HS256'])
    return decoded_token


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['token']
            try:
                decode = decode_token(token)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token expired!'}), 401
            except jwt.InvalidSignatureError:
                return jsonify({'message': 'Signature verification failed!'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid Token verification failed!'}), 401
        except KeyError:
            return jsonify({'message': 'Missing token!'}), 401
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers['token']
        user_id = decode_token(token)['user_id']
        db.cursor.execute(f"""SELECT id, is_admin FROM users WHERE id={user_id}""")
        user = db.cursor.fetchone()
        if not user['is_admin']:
            return jsonify({'message': 'Only admins can access this route'}), 401
        return func(*args, **kwargs)
    return wrapper


def get_all_users():
    sql_command = """SELECT * FROM users WHERE is_admin=False"""
    db.cursor.execute(sql_command)
    users = db.cursor.fetchall()
    return users


def login_user():
    data = request.get_json(force=True)
    db.cursor.execute("SELECT id, name, password, is_admin FROM users WHERE email=%s", (data["email"],))
    user = db.cursor.fetchone()
    return user


"""
SELECT * FROM users;
SELECT is_admin FROM users;
SELECT * FROM users WHERE is_admin=True;
SELECT * FROM users INNER JOIN orders ON users.email=orders.email;
SELECT * FROM users AS u OUTER JOIN orders AS o ON u.email=o.email;

INSERT INTO users(name, email, password, is_admin) VALUES('bootcamp', 'user@bootcamp.com', '12345', 'true');
INSERT INTO users(name, email, password, is_admin) VALUES('bootcamp', 'user@bootcamp.com', '12345', 'true') RETURNING name, email, is_admin;

UPDATE FROM users SET name='Douglas';
UPDATE FROM users SET name='Douglas' RETURNING name;

DELETE FROM users WHERE id=1;

TRUNCATE FROM users;
"""