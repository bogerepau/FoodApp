from flask import Blueprint, request, jsonify
from models.model import Student, students_db

student_blueprint = Blueprint('student_blueprint', __name__)


@student_blueprint.route('/students', methods=["POST", "GET"])
def students():
    if request.method == "POST":
        new_student = Student(request.json["name"], request.json["age"])
        students_db.append(new_student)
        students_list = [{"name": item.name, "age": item.age} for item in students_db]
        resp = jsonify({"message": "successfully created!", "data": students_list})
        resp.status_code = 201
    else:
        students_list = [{"name": item.name, "age": item.age} for item in students_db]
        resp = jsonify({"data": students_list})
        resp.status_code = 200
    return resp