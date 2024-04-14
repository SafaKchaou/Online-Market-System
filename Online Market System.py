import time  #Import time module #As a reference I used: https://www.programiz.com/python-programming/time

def welcome():
    print("****Welcome to Medipol Online Market****")  # The title shown when the program is first excuted
    print("Please log in by providing your user credentials:")  # To show for the user that he/she will enter his/her credentials

def credential_input():
    user_name = input("User Name: ")
    password = input("Password: ")
    return user_name,password
def Dispaly1(): #Function that will display the main menu and return the choice of the user from this menu
    menu = {"1": "Search for a product", "2": "See Basket", "3": "Check Out", "4": "Logout", "5": "Exit"}
    print("Please choose one of the following Services:")
    for i in menu:
        ch = str(i) + "." + menu[i]
        print(ch)
    choice = input("Your Choice: ")
    while choice not in menu.keys():
        print("Invalid menu entry!Please enter again")
        choice = input("Your Choice: ")
    return choice
def valid(search_term,Inventory):   #Function that will return True if there is at least one item in the inventory dictionary that matches the term that the user search for
    test = False
    for i in Inventory:
        if search_term.lower() in i and Inventory[i][0] != 0:
            test = True
    return test
def searching(search_term,Inventory):  #Function that will return a list contains all the items in the inventory dictionary that matches the item that the user search for, and it returns the total number of these items
    list = []
    counter = 1
    for i in Inventory:
        if search_term.lower() in i :
            list.append([counter,i,Inventory[i][0],Inventory[i][1]])
            counter += 1
    return list,counter-1
def add_item_to_basket(basket,p,amount):   #Adding items to the basket of the user
    basket.append(p+[amount])
def Dispaly2():   #Function that will display the basket sub menu and returns the selection made by the user
    menu2 = {"1": "Update amount", "2": "Remove an item", "3": "Check out", "4": "Go back to main menu"}
    print("Please choose an option:")
    for i in menu2:
        ch = str(i) + "." + menu2[i]
        print(ch)
    selection =input("Your selection: ")
    while selection not in menu2.keys():
        print("Invalid entry!Please enter again")
        selection = input("Your selection: ")
    return selection
def updating_basket(basket,change_item,new_amount):  #Function that will update the amount of the item which the user changed
    basket[change_item - 1][4] = new_amount
    return basket
def printing_basket(basket):   #Function that will display the content of the basket
    if basket != []:
        counter = 1
        total = 0
        for i in basket:
            print(f"{counter}.{i[1]} price = {i[3]}$ amount = {i[4]} total = {i[3] * i[4]}$")
            counter += 1
            total += i[3] * i[4]
        print(f"Total {total}$")
    else:
        print("Your basket is empty")
        print("Total  0$")
def Date():   #Function that will print the real date when the user logout
    current_time = time.localtime()
    current_date = time.strftime("%Y-%m-%d",current_time)
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    T = str(current_hour) + ":" + str(current_minute)
    print(current_date,T)
def Display_receipt(basket):    #Function that will display the receipt
    print("Processing your receipt...\n******* Medipol Online Market ********\n**************************************\n444 8 544\nmedipol.edu.tr")
    print("— — — — — — — — — — — —")
    printing_basket(basket)
    print("— — — — — — — — — — — —")
    Date()
    print("Thank You for using our Market!")
def decrease(Inventory,basket):   #Function that will decrease the amount of the product when the user check out
    for i in basket:
        Inventory[i[1]][0] =  Inventory[i[1]][0] - i[4]
    return Inventory
def Dispaly3():   #Funtion that will display the menu of the admin
    menu3 = {"1": "Activate User Account", "2": "Deactivate User Account", "3": "Add User", "4": "Remove User", "5":"Logout","6":"Exit"}
    print("Please choose one of the following services :")
    for i in menu3:
        ch = str(i) + "." + menu3[i]
        print(ch)
    admin_choice = input("Your selection: ")
    while admin_choice not in menu3.keys():
        print("Invalid entry!Please enter again")
        admin_choice = input("Your selection: ")
    return admin_choice
def main(Inventory,user_basket,User_Ac_Info,status):    #The main function
    start = 0    #Initiating a variable through which the loop is controled (to be excuted or not)
    while start == 0:  #Loop for the hall code/to be runned even if the user chose to logout

        welcome()

        user_name,password = credential_input()

        while user_name not in User_Ac_Info.keys():
            print("Your user name and/or password is not correct. Please try again!")
            user_name,password = credential_input()

        l = 0    #Initiating a variable through which the loop is controled (to be excuted or not)
        h = 0    #Initiating a variable through which the loop is controled (to be excuted or not)
        while user_name != "admin" and h == 0 :  #This loop will check the situation (blocked or not) for all users excep the admin

            while (user_name, password) not in User_Ac_Info.items() or status[user_name] != 0:
                if status[user_name] != 0:   #Showing that the user is blocked
                    print("Your account has been blocked. please contact the administrator.")
                    user_name,password = credential_input()

                    while user_name not in User_Ac_Info.keys():
                        print("Verify your user name!")

                        user_name,password = credential_input()

                    if user_name == "admin":
                        l = 1
                        break
                else:
                    print("Your user name and/or password is not correct. Please try again!") #Demanding from the user to re-enter the credentials due to an error (uncorrect user name or uncorrect password)
                    user_name,password = credential_input()
                    while user_name not in User_Ac_Info.keys():
                        print("Verify your user name!")
                        user_name,password = credential_input()  
                    if user_name == "admin":
                        l = 1
                        break

            print("Successfully logged in!")   #The message that shows that the access is correct
            print("Welcome,", user_name,"! Please choose one of the following options by entering the corresponding menu number.")
            while l == 0 :
                for i in range (len(user_basket)):
                    if user_name == user_basket[i][0]:
                        index = i    #Getting the index of the basket corresponding to the user from user_basket (in which the basket will be stored)
                m = 0   #Initiating a variable through which the loop is controled (to be excuted or not)
                while m == 0:
                    k = 0   #Initiating a variable through which the loop is controled (to be excuted or not)
                    j = 0   #Initiating a variable through which the loop is controled (to be excuted or not)
                    h = 0   #Initiating a variable through which the loop is controled (to be excuted or not)
                    choice = Dispaly1()   #Displaying the main menu and returning the choice of the user
                    if choice == "1":       #The search funcionality will be runned
                        search_term = input("What are you searching for? ")
                        while not valid(search_term, Inventory): #The user still will be asked for the search term (or turning to the main menu) until it will match the products in the Inventory dictionary
                            search_term = input("Your search did not match any items. Please try something else (Enter 0 for main menu): ")
                            if search_term == "0":  #Turning to the main menu
                                k = 1
                                break
                        while k == 0 :
                            search_items,number = searching(search_term,Inventory)
                            print(f"found {number} similar items")
                            for i in range (len(search_items)):
                                print(f"{search_items[i][0]}.{search_items[i][1]} {search_items[i][3]}$")   #Printing the items that matches the search item and their price
                            select_item = -1
                            while not (0<select_item<=number) :
                                select_item = int(input("Please select which item you want to add to your basket (Enter 0 for main menu): "))
                                if select_item == 0:  #Turning to the main menu
                                    j = 1
                                    k = 1
                                    break
                            while j == 0:
                                for i in search_items:
                                    if i[0] == select_item:
                                        p = i
                                print(f"Adding {p[1]}.")
                                amount = int(input("Enter Amount: "))
                                while not 0<amount<= p[2] :
                                    amount = int(input("Sorry! The amount exceeds the limit, Please try again with smaller amount (Enter 0 for main menu):"))
                                    if amount == 0:  #Turning to the main menu
                                        h = 1
                                        j = 1
                                        k = 1
                                        break
                                while h == 0:
                                    add_item_to_basket(user_basket[index][1],p,amount) #Adding the item to the basket
                                    print(f"Added {p[1]} into your Basket.")
                                    print("Going back to main menu....")
                                    h = 1
                                    j = 1
                                    k = 1
                    elif choice == "2":    #Displaying the basket and the basket sub menu
                        x = 0  #Initiating a variable through which the loop is controled (to be excuted or not)
                        while x==0:
                            printing_basket(user_basket[index][1])  #Displaying the basket
                            selection = Dispaly2()    #Displaying the basket sub menu
                            if selection == "1":  #update amount is selected
                                change_item = int(input("Please select which item to change its amount: "))
                                new_amount = int(input("Please type the new amount: "))
                                while user_basket[index][1][(change_item)-1][2] < new_amount:  #Cheking if the amount exceed the limit or not
                                    print("The amount exceeds the limit")
                                    new_amount = int(input("Please type the new amount: "))
                                user_basket[index][1] = updating_basket(user_basket[index][1],change_item,new_amount)  #Updating the amount
                            elif selection == "2":  #delete item is selected
                                remove_item = int(input("Please enter which item you want to remove : "))
                                del user_basket[index][1][remove_item -1]   #Delete an item from the basket
                            elif selection == "3":  #check out is selected
                                Display_receipt(user_basket[index][1])   #Displaying the receipt
                                Inventory = decrease(Inventory,user_basket[index][1]) #Decrease the amount in the main ammount of the product
                                x = 1
                                break
                            elif selection == "4":  #Turning to the main menu
                                break
                    elif choice == "3":  #Check out
                        Display_receipt(user_basket[index][1])
                        Inventory = decrease(Inventory, user_basket[index][1])
                    elif choice == "4":  #Logout
                        m = 1
                        l = 1
                        h = 1
                        break
                    else:   #Exit
                        l = 1
                        m = 1
                        h = 1
                        start = 1
                        break
        if user_name == "admin":   #All related to the admin
            print("Welcome, admint! Please choose one of the following options by entering the corresponding menu number.")
            stop = 0   #Initiating a variable through which the loop is controled (to be excuted or not)
            while stop == 0:
                admin_choice = Dispaly3()   #Displaying the menu related to the admin
                if admin_choice == "1":   #Activate User Account is chosed
                    user_name_to_be_unblocked = input("Please enter the user name that you want to reactivate : ")
                    status[user_name_to_be_unblocked] = 0 #Turning the state of the user equal to 0 --> the user is unblocked anymore
                elif admin_choice == "2":  #Deactivate User Account is chosed
                    user_name_to_be_blocked = input("Please enter the user name that you want to deactivate : ")
                    status[user_name_to_be_blocked] = 1   #Turning the state of the user equal to 1 --> the user is blocked now
                elif admin_choice == "3":    #Add User is chosed
                    new_user = input("Please enter the name of the user that you want to add : ")
                    new_password = input("Please enter the password of the user that you want to add : ")
                    User_Ac_Info[new_user] = new_password  #Adding a new user to the User_Ac_Info dictionary
                    status[new_user] = 0  #Initializing the state as 0 --> unblocked
                elif admin_choice == "4":   #Remove User is chosed
                    del_user = input("Please enter the name of the user that you want to remove : ")
                    del User_Ac_Info[del_user.lower()] #Delete user from the main dictionary
                elif admin_choice == "5": #Logou is chosed
                    stop = 1
                elif admin_choice == "6": #Exit is chosed
                    start = 1
                    break
User_Ac_Info = {"ahmet":"1234","zeynep":"4444","malek":"7089","admin":"qwerty"}    #Data structur for the user accout information
status = {"ahmet": 0, "zeynep": 0, "malek": 0, "admin": 0}  #Data structure to initiate the sate of the users (unblocked) : state"0"--> unblocked ; state "1" -->blocked
Inventory = {"asparagus":[10,5], "broccoli":[15,6] , "carrots ":[18,7] , "apples":[20,5] , "banana":[10,8] , "berries":[30,3] , "eggs":[50,2] , "mixed fruit juice":[0,8] , "fish sticks":[25,12] , "ice cream":[32,6] , "apple juice":[40,7] , "orange juice":[30,8] , "grape juice":[10,9] }  #Data structure for the market's inventory
user_basket = [["ahmet",[]],["zeynep",[]],["malek",[]]]   #Data structure in which the Basket of the user can be stored after logout
main(Inventory,user_basket,User_Ac_Info,status)    #Calling the main function that will run all the instructions