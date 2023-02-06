#Decided to do a purchase Id for search functionality.

from Purchase import Purchase

class PurchaseManager:
    def __init__(self):
        self.item_list = []
        self.purchase_id = 3000
    
    def add_purchase(self,Purchase):
        price = Purchase.Item.price
        

        #add to employee class purchase total and discount total
        #grab the employee discount, do that math to the item price
        #then store that to employee total, and the amount discounted to employee discount

