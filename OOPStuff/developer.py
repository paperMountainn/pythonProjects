from employee import Employee

class Developer(Employee):
    # override raise_ratio
    raise_ratio = 2

    # Developer, on top of having first_name, last_name, age and salary
    # also has a programming language
    def __init__(self, first_name, last_name, age, salary, prog_language):
        super().__init__(first_name, last_name, age, salary)
        self.prog_language = prog_language

    
