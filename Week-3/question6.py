#No6   
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def annual_salary(self):
        return f'Annual salary: {12 * self.salary}'

e1 = Employee("Jack", 30000)
print(e1.annual_salary())