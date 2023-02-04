#Items have item ID, Name, and cost. Similar to employee, I'm going to have the manager auto assign IDs for the items. 
class Item:
    def __init__(self,name,cost):
        self.item_id = 0
        self.name = name
        self.cost = cost
        
    
    def print_item(self):
        print(self.item_id,self.name,self.cost)