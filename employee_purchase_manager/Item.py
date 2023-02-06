#Items have item ID, Name, and cost. Similar to employee, I'm going to have the manager auto assign IDs for the items. 

#In addition to project requirements, I wanted to add quantity to prevent purchases of items that exist in the system
#but my not be available due to stock shortages
class Item:
    def __init__(self,name,price,quantity):
        self.item_id = 0
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def print_item(self):
        print(self.item_id,self.name,self.cost)