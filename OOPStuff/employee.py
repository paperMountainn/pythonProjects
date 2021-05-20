class Employee:
    company_name = "Doge Pte Ltd"
    raise_ratio = 1.04
    num_of_employees = 0

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        Employee.num_of_employees +=1

    def print_name(self):
        print(f"{self.first_name} {self.last_name}")

    def apply_raise(self):
        self.salary = self.salary * self.raise_ratio
        # using self.raise_ratio will allow any subclass to override the constant when they wanted to
        # => self.salary * self.raise_ratio
         
        return self.salary
    
    # decorators
    @classmethod
    def set_raise_ratio(cls, ratio):
        cls.raise_ratio = ratio
    
    # alternative constructor
    @classmethod
    def create_employee_with_raw_info(cls, raw_information):
        first, last, age, salary = raw_information.split("-")
        return cls(first, last, age, salary)
        

    @staticmethod
    def is_work_day(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True






