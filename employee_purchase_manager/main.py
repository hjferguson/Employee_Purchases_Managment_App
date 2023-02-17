#Lab Professor: Michael
#Written by: Harlan Ferguson 101133838
from EmployeeManager import EmployeeManager 
from ItemManager import ItemManager
from PurchaseManager import PurchaseManager
from menu import*
if __name__ == "__main__":
    EM = EmployeeManager()
    IM = ItemManager()
    PM = PurchaseManager()
    my_menu(EM,IM,PM)
