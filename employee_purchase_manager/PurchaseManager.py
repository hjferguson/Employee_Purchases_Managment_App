#Decided to do a purchase Id for search functionality.

from Purchase import Purchase

class PurchaseManager:
    def __init__(self):
        self.purchase_list = []
        self.purchase_id = 3000
    
    def add_purchase(self,Employee, Item):
        temp = Purchase(Employee, Item)
        price = Item.price
        discounted_price = price - (Employee.employee_discount * price) #0.04
        if discounted_price > 200:
            discounted_price = price - 200
            Employee.total_purchased += discounted_price
            Employee.total_discounts += 200
        else:    
            Employee.total_purchased += discounted_price #discounted price 9.6
            Employee.total_discounts += round((price - discounted_price),2)
            self.purchase_id += 1
            self.purchase_list.append(temp)

    def print_all_purchases(self):
        for purchase in self.item_list:
            purchase.print_purchase()