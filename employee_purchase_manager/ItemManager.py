from Item import Item

class ItemManager:
    def __init__(self):
        self.item_list = []
        self.item_id = 200
        
    #menu will sanitize
    def add_item(self,name,price,quantity):
        temp = Item(name,price,quantity)
        temp.item_id = self.item_id
        self.item_id += 1
        self.item_list.append(temp)

    def item_exsists(self,ID):
        ID = int(ID)
        for x in self.item_list:
            
            if(x.item_id == ID):
                return x
        return False
    
    # def print_item(self):
    #     print(self.item_id,self.name,self.price)

    # def print_all_items(self):
    #     print("Item number, Item name, Item cost")
    #     for item in self.item_list:
    #         item.print_item()

    def print_item(self):
        print("{:<12} {:<20} ${:.2f}".format(self.item_id, self.name, self.price))

    def print_all_items(self):
        print("{:<12} {:<20} {:<12}".format("Item number", "Item name", "Item cost"))
        for item in self.item_list:
            item.print_item()
    
    