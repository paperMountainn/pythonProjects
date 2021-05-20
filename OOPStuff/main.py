from manager import Manager
from developer import Developer
from employee import Employee
import datetime

# initialise objects
em_1 = Employee("Prscilla", "Tan", 21, 10);
em_2 = Employee("Jodi", "Tan", 22, 20);

dev_1 = Developer("Zoe", "Doge", 22, 5, "Javascript");

man_1 = Manager("Doge", "Cat", 26, 100000, [dev_1])


print(man_1)