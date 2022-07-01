# models file that act as the database or data storage
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 18:
            ValueError("Above 18 not permitted!")
        self._age = age


students_db = []
student1 = Student("Victoria", 26)
students_db.append(student1)
student2 = Student("Timothy", 23)
students_db.append(student2)
student3 = Student("Daniel", 37)
students_db.append(student3)
student4 = Student("Peter", 31)
students_db.append(student4)
