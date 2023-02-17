#construct manager class for employee class
#this will hold a list of current employees, and also have the methods for add/del
#will also auto assign ID and disc_id
from Employee import Employee

class EmployeeManager:
    def __init__(self):
        
        self.employee_list = []
        self.employee_ID = 0
        self.employee_discount_ID = 1000
    
    #menu will sanitize
    def add_employee(self,name,employee_type,years_worked):
        temp = Employee(name,employee_type,years_worked)
        #behind the scenes we also need to set the ID and discount ID
        temp.id = self.employee_ID
        self.employee_ID += 1
        temp.emp_disc_num = self.employee_discount_ID
        self.employee_discount_ID += 1
        #add to list
        self.employee_list.append(temp)

    def employee_exsists(self,ID):
        ID = int(ID)
        for x in self.employee_list:
            if(x.id == ID):
                return x
        return False


        
    
    def print_all_employees(self):
        s = ""
        #print("ID,Name,Employment type,years worked,total purchased, total discounts, discount id ")
        for employee in self.employee_list:
            s += employee.print_employee()
        return s
        

