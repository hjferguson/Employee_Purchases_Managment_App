from Item import Item

class ItemManager:
    def __init__(self):
        self.item_list = []
        self.item_id = 200
    
    def add_item(self,name,price,quantity):
        temp = Item(name,price,quantity)
        temp.item_id = self.item_id
        self.item_id += 1
        self.item_list.append(temp)
    
    def print_all_items(self):
        for item in self.item_list:
            item.print_item()
    
    