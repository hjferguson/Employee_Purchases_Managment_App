#making a menu function. Will then just call the function in main. 
def my_menu(EM,IM,PM):
    while True:
        print("------------------------------")
        print("|    1- Create Employee      |") 
        print("|    2- Create Item          |")
        print("|    3- Make Purchase        |")
        print("|    4- Employee Summary     |")
        print("|    5- Exit Application     |")
        print("------------------------------")

        userIn = input()
        
        if(userIn == "1"): #create employee
            name = input("Please input employee full name: ")
            if(name == "NO"):
                break
            while name.isdigit() == True:
                print("Please input a valid name")
                name = input("Please enter employee's full name: ")
            name = name.title() #ensures each word starts with a capital
            
            jobTitle = input("Please input job title: ")
            while jobTitle.isdigit() == True:
                print("Please input a valid job title")
                jobTitle = input("Please enter job title: ")
            jobTitle = jobTitle.title() #ensures each word starts with a capital

            years_worked = input("Please input years worked: ")
            while years_worked.isdigit() == False:
                print("Please input valid integer")
                years_worked = input("Please input years worked: ")
            years_worked = int(years_worked)
            while years_worked < 0 or years_worked > 60:
                print("Please input valid integer between 0-60")
                years_worked = int(input("Please input years worked: "))

            EM.add_employee(name,jobTitle,years_worked)
  
        if(userIn == "2"): #create item

            name = input("Please input item name: ")
            while name.isdigit() == True:
                print("Please input a valid name")
                name = input("Please input item name: ")
            name = name.title() #ensures each word starts with a capital
            
            price = input("Please input price: ")
            while price.isdigit() == False:
                print("Please input valid integer")
                price = input("Please input price: ")
            price = float(price)
            while price < 0 or price > 10000:
                print("Please input valid integer between 0-10,000")
                price = float(input("Please input price: "))

            quantity = input("Please input item quantity: ")
            while quantity.isdigit() == False:
                print("Please input valid integer")
                quantity = input("Please input item quantity: ")
            quantity = int(quantity)
            while quantity < 0 or quantity > 1000:
                print("Please input valid integer between 0-1000")
                quantity = int(input("Please input item quantity: "))
            
            IM.add_item(name,price,quantity)

        if(userIn == "3"): #make purchase
            emp_id = input("Please input employee id: ")
            while emp_id.isdigit() == False:
                emp_id = input("Please input a valid id: ")
            if (EM.employee_exsists(emp_id) != False):
                item_id = input("Please input item id: ")
                while item_id.isdigit() == False:
                    item_id = input("Please input a valid id: ")
                if(IM.item_exsists(item_id) != False):
                    PM.add_purchase(EM.employee_exsists(emp_id),IM.item_exsists(item_id))
                print("Item doesn't exsist in the system...")
                break
            print("Employee doesn't exsist in the system...")
            break
        
        if(userIn == "4"): #all employee summary
            print(EM.print_all_employees())
        
        if(userIn == "5"):
            break