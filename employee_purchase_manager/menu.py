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
        
        if userIn == "1": # create employee
            name = input("Please input employee full name: ")
            while name.isnumeric() or not name.strip():
                if name.isnumeric():
                    print("Please input a valid name")
                else:
                    print("Invalid input. Please enter a non-blank name.")
                name = input("Please enter employee full name: ")
            name = name.title()
            if name == "No":
                continue
            
            
            jobTitle = input("Please input job title either 'manager' or 'hourly': ")
            if jobTitle == "NO":
                continue
            while jobTitle != "manager" and jobTitle != "hourly":
                jobTitle = input("Please input either 'manager' or 'hourly': ")
                if jobTitle == "NO":
                    break
            #I'm sure there is a cleaner way of doing this, but I am too braindead to try a better approach. This works...
            # and if it ain't broke, don't fix it    
            if jobTitle == "NO":
                continue
            
            
            years_worked = input("Please input years worked: ")
            if years_worked == "NO":
                continue
            while years_worked.isdigit() == False:
                print("Please input valid integer")
                years_worked = input("Please input years worked: ")
                if years_worked == "NO":
                    break
            if years_worked == "NO":
                continue
            years_worked = int(years_worked)
            while years_worked < 0 or years_worked > 70:
                print("Please input valid integer between 0-70")
                years_worked = int(input("Please input years worked: "))
                if years_worked == "NO":
                    break
            if years_worked == "NO":
                continue

            EM.add_employee(name,jobTitle,years_worked)
  
        if(userIn == "2"): #create item

            
            name = input("Please input item name: ")
            while name.isnumeric() or not name.strip():
                if name.isnumeric():
                    print("Please input a valid name")
                else:
                    print("Invalid input. Please enter a non-blank name.")
                name = input("Please enter item name: ")
            name = name.title()
            if name == "No":
                continue
            
            price = input("Please input price: ")
            if price == "NO":
                continue
            while price.isdigit() == False:
                print("Please input valid integer")
                price = input("Please input price: ")
                if price == "NO":
                    break
            if price == "NO":
                continue
            price = float(price)
            while price < 0 or price > 10000:
                print("Please input valid integer between 0-10,000")
                price = float(input("Please input price: "))
                

            quantity = input("Please input item quantity: ")
            if quantity == "NO":
                continue
            while quantity.isdigit() == False:
                print("Please input valid integer")
                quantity = input("Please input item quantity: ")
                if quantity == "NO":
                    break
            if quantity == "NO":
                continue
            quantity = int(quantity)
            while quantity < 0 or quantity > 1000:
                print("Please input valid integer between 0-1000")
                quantity = int(input("Please input item quantity: "))
                
            
            IM.add_item(name,price,quantity)

        if(userIn == "3"): #make purchase
            IM.print_all_items()
            emp_id = input("Please input employee id: ")
            while emp_id.isdigit() == False:
                emp_id = input("Please input a valid id: ")
            
            if (EM.employee_exsists(emp_id) != False):
                item_id = input("Please input item id: ")
                while item_id.isdigit() == False:
                    item_id = input("Please input a valid id: ")
                
                if(IM.item_exsists(item_id) != False):
                    PM.add_purchase(EM.employee_exsists(emp_id),IM.item_exsists(item_id))
                    continue
                print("Item doesn't exsist in the system...")
                continue
            print("Employee doesn't exsist in the system...")
            
        
        if userIn == "4": #all employee summary
            print(EM.print_all_employees())
        
        if userIn == "5":
            break