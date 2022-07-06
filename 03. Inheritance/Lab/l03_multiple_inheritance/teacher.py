from F03_Inheritance.Lab.l03_multiple_inheritance.employee import Employee
from F03_Inheritance.Lab.l03_multiple_inheritance.person import Person


class Teacher(Person, Employee):
    # def __init__(self):
    #     Person.__init__(self)
    #     Employee.__init__(self)

    def teach(self):
        return 'teaching...'