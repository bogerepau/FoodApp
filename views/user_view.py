from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.user_model import User
from controllers.user_controller import admin_required, get_all_users, token_required, login_user, encode_token

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/users', methods=['GET'])
@token_required
@admin_required
def get_users():
    users = get_all_users()
    if users:
        return jsonify({'message': users}), 200
    return jsonify({'message': 'users not found!'}), 404


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = login_user()
        if check_password_hash(user[2], data['password']):
            return jsonify({'message': 'successfully loggedIn!', 'data': encode_token(user[0])})
        return jsonify({'message': 'Invalid Credentials, Please try again!'}), 401
    return jsonify({'message': 'Bad Request!'}), 400


user_blueprint.route('/register', methods=["POST"])


# def register():
#     if request.method == "POST":
#         if request.json in DBConnection:
#             return jsonify({"message": "Username already registered"})
#         else:
#             new_user = User(
#                 request.json["username"], request.json["email"], request.json["password"])
#             DBConnection.append(new_user)
#         return jsonify({"message": "User has been registered"})