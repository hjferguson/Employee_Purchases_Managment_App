#CLI: python -m unittest test_employee_manager.py
import unittest
import sys
sys.path.append("..")
from EmployeeManager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    
    def test_one_new_employee(self):
        EM = EmployeeManager()
        EM.add_employee("Harlan","manager",5)
        expecting = "0, Harlan, manager, 5, 0, 0, 1000\n"
        self.assertEqual(EM.print_all_employees(),expecting)

    def test_ten_new_employees(self):
        EM = EmployeeManager()
        EM.add_employee("Harlan","manager",5)
        EM.add_employee("Raleigh","hourly",1)
        EM.add_employee("Owen","hourly",2)
        EM.add_employee("Casey","manager",3)
        EM.add_employee("Bruno","hourly",4)
        EM.add_employee("Ryan","hourly",5)
        EM.add_employee("Jill","hourly",10)
        EM.add_employee("Lukas","manager",20)
        EM.add_employee("Jordan","manager",30)
        EM.add_employee("Matt","hourly",40)
        
        expecting = "0, Harlan, manager, 5, 0, 0, 1000\n1, Raleigh, hourly, 1, 0, 0, 1001\n2, Owen, hourly, 2, 0, 0, 1002\n"
        expecting += "3, Casey, manager, 3, 0, 0, 1003\n4, Bruno, hourly, 4, 0, 0, 1004\n5, Ryan, hourly, 5, 0, 0, 1005\n"
        expecting += "6, Jill, hourly, 10, 0, 0, 1006\n7, Lukas, manager, 20, 0, 0, 1007\n8, Jordan, manager, 30, 0, 0, 1008\n"
        expecting += "9, Matt, hourly, 40, 0, 0, 1009\n"
        
        
        self.assertEqual(EM.print_all_employees(),expecting)


