from flask import Flask, jsonify
from controllers.controller import is_admin
from views.view import student_blueprint
from views.user_view import user_blueprint

app = Flask(__name__)
app.register_blueprint(student_blueprint)
app.register_blueprint(user_blueprint)


@app.route('/')
@is_admin
def welcome():
    return jsonify({"message": "Hey, welcome to The Kitchen!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)