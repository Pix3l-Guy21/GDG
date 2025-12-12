#No5
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def set_grade(self, new_grade):
        self.__grade = new_grade
    def get_grade(self):
        return self.__grade

std1 = Student("John", 90)

print(std1.get_grade())