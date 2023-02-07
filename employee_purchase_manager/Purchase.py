#Purchase links the item and the employee together
#Purchase manager will have ability to store purchase history and update employee information
from Item import Item
from Employee import Employee
import datetime #purchases usually have a time associated

class Purchase:
    def __init__(self,Item,Employee):
        self.Item = Item
        self.Employee = Employee
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S)") #time of transaction formatted to: yyyy-mm-dd hh:mm:ss

    def print_purchase(self):
        print("Item: ",self.Item,"Employee: ",self.Employee)
    
            
