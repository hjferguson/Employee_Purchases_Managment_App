#Lab Professor: Michael
#Written by: Harlan Ferguson 101133838
from EmployeeManager import EmployeeManager 

if __name__ == "__main__":
    EM = EmployeeManager()
    EM.add_employee("Harlan", "Full-Time", 5)
    EM.add_employee("Amanda","Part-Time",2)
    EM.print_all_employees()
