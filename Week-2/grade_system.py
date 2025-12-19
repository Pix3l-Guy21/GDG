#Question #4: Grade management system
#Also answer to Question #14 printing score and prompting if not found

#demo dictionary
student_grades = {
    "Abebe": 40,
    "Solomon": 80,
    "Robel": 90,
    "Dawit": 70,
    "Mohamed": 80
}

def get_grade(student_grades, student_name):
    try:
        print(f'{student_name}\'s grade: {student_grades[student_name]}')
    except KeyError:
        print('Student not found in the system')

#demo call
get_grade(student_grades, "Dawit")