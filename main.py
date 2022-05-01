# Remove these fake credentials once database works
fake_username = "admin"
fake_password = "password"
logged_in = False;

from UserClass import User


import mysql.connector
import sys

    

# Userchoice function that does basic input test with values being amount of choices

def intSpecificChoice(input_string):
    
    try:
        user_input = int(input(input_string))
        return user_input
        
    except:
        print("Please input a valid integer")
        return intSpecificChoice(input_string)


def userChoice(values):
    try:
        user_input = int(input())
        if (user_input not in values):
            raise ValueError
        return  user_input
    except ValueError:
        print('Please input a correct option.')
        return userChoice(values)

# Menu that display's when the user wants to view items in the store 
def viewStore(connection, user):
    print("1. Choose Category\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
            print("Store info:")
            loggedInMenu(connection, user)
        case 2:
            loggedInMenu(connection, user)

# Menu that display's when the user wants to view items in the store 
def viewOrderHistory(connection, user):
    print("View Order History:")
    print("1. Go back to the menu")
    user_choice = userChoice({1})
    match user_choice:
        case 1:
           loggedInMenu(connection, user)

# Menu that display's the user's cart and information
def viewCart(connection, user):
    print("1. View Cart\n2. Remove Item from Cart\n3. Checkout\n4. Go back to the menu")
    user_choice = userChoice({1, 2, 3, 4})
    match user_choice:
        case 1:
            print("View cart items")
            loggedInMenu()
        case 2:
            print("Items to remove")
            loggedInMenu()
        case 3:
            print("Checkout cart")
            loggedInMenu(connection, user)
        case 4:
            loggedInMenu(connection, user)

# Menu that let's the user edit their account information

def editAccountInfo(connection, user):
    print("1. Edit Shipping Information\n2. Edit Payment Information\n3. Delete Account\n4. Go back to the menu")
    user_choice = userChoice({1, 2, 3, 4})
    match user_choice:
        case 1:
            print("Edit Shipping Info")
            shipping_address = input("Enter shipping address: ")
            shipping_state = input("Enter shipping state: ")
            shipping_zipcode = intSpecificChoice("Enter shipping zip code: ")
            if (user.editAccount(connection, user.getUsername(), shipping_address, shipping_state, shipping_zipcode, None)):
                loggedInMenu(connection, user)
        case 2:
            print("Edit Payment Info")
            ccnum = int(input("Enter credit card number: "))
            if (user.editAccount(connection, user.getUsername(), None, None, None, ccnum)):
                loggedInMenu(connection, user)
        case 3:
            print("Are you sure you want to delete your account?")
            print("1. Yes\n2. No")
            confirm = userChoice({1, 2})
            match confirm:
                case 1:
                    logged_in = False;
                    if (user.deleteAccount(connection, user.getUsername())):
                        print("Deleted account returning to menu")

                        menu(connection, user)
                    else:
                        print("Error deleting account")
                        loggedInMenu(connection, user)
                case 2:
                    loggedInMenu(connection, user)
        case 4:
            loggedInMenu(connection, user)


# Menu that display's when the user wants to view items in the store 
def viewStore(connection, user):
    print("1. Choose Category\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
            print("Store info:")
            loggedInMenu(connection, user)
        case 2:
            loggedInMenu(connection, user)
       
        
# Menu that displays when the user is logged in       
def loggedInMenu(connection, user):
   
    print("1. View Items in Store\n2. View Order History\n3. Cart Information\n4. Edit Account Information\n5. Logout\n6. Exit Program")
    user_choice = userChoice({1, 2, 3, 4, 5, 6})
    match user_choice:
        case 1:
            viewStore(connection, user)
        case 2:
            viewOrderHistory(connection, user)
        case 3:
            viewCart(connection, user)
        case 4:
            editAccountInfo(connection, user)
        case 5:
            logged_in = False;
            menu(connection, user)
        case 6:
            print("Exiting the program")
            exit()

# Menu which display's when the user wants to log in
def login(connection, user):
    print("1. Enter username and password\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
   
            print("Enter Username: ", end = '')
            username = input();
            print("Enter Password: ", end = '')
            password = input();
            
            if (user.login(connection, username, password)):
                logged_in = True
                print("Your logged in")
                loggedInMenu(connection, user)
            else: 
                print("Invalid credentials, please try again.")
                login(connection, user)
        case 2:
            menu(connection, user)
       
    

    
# Menu that displays when the user wants to create an account
def createAccount(connection, user):
   
    username = input("Enter username: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    shipping_address = input("Enter Shipping address: ")
    shipping_state = input("Enter shipping state: ")
    shipping_zip = intSpecificChoice("Enter shipping zip code: ")
    ccnum = intSpecificChoice("Enter credit card number: ")
    if (user.createAccount(connection, username, first_name, last_name, password, shipping_address, shipping_state, shipping_zip, ccnum)):
        logged_in = True
        loggedInMenu(connection, user)
    else:
        menu(connection, user)
def menu(connection, user):
    
    print("1. Login\n2. Create Account\n3. Exit Program")
    user_choice = userChoice({1, 2, 3})
    match user_choice:
        case 1:
            login(connection, user)
        case 2:
            createAccount(connection, user)
        case 3:
            connection.close()
            print("Exiting the program")
            exit()
    
       
   
        

def main():
    user = User()
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="methods_project"
        )   
                
        menu(connection, user)
        
    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

if __name__ == "__main__":
    main()
