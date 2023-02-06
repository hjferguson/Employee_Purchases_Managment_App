#Purchase links the item and the employee together
#Purchase manager will have ability to store purchase history and update employee information
from Item import Item
from Employee import Employee

class Purchase:
    def __init__(self,Item,Employee):
        self.Item = Item
        self.Employee = Employee

    def print_purchase(self):
        print("Item: ",self.Item,"Employee: ",self.Employee)
    
            
