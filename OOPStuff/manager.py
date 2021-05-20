from employee import Employee

class Manager(Employee):
    def __init__(self, first_name, last_name, age, salary, emp_list=None):
        super().__init__(first_name, last_name, age, salary)
        if (emp_list == None):
            self.emp_list = []
        else:
            self.emp_list = emp_list
        
    
    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.pop(emp)
    
    def print_emp(self):
        print("The Employee(s) are: ")
        for emp in self.emp_list:
            
            emp.print_name()