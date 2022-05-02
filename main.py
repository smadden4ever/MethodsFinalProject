# Remove these fake credentials once database works
fake_username = "admin"
fake_password = "password"
logged_in = False

from dis import show_code
from UserClass import User
import mysql.connector
import sys

from ItemClass import Item 
from ShoppingCartClass import ShoppingCart
from OrderClass import Order


username = ""
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
def viewStore(connection, user, inventory, cart):
    inventory.viewAll(connection)
    print("1. to purchase\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
            print("Store info:")
            inventory.viewAll(connection)
            print("Please enter the movie id of the item you'd like to purchase: ")
            movieId = input()
            print("Please enter the quantity that you'd like to purchase: ")
            quantity = input()
            result = inventory.removeAmountFromStockOf(connection, quantity, movieId)
            if(result):
                cart.addToCart(connection, user.getUsername(), movieId, quantity)
                viewStore(connection, user, inventory, cart)
            else:
                viewStore(connection, user, inventory, cart)
        case 2:
            loggedInMenu(connection, user, inventory, cart)

# Menu that display's when the user wants to view items in the store 
def viewOrderHistory(connection, user, inventory, cart):
    print("Your Order History:")
    order = Order()
    order.viewOrderHistory(connection, user.getUsername())
    print("1. Go back to the menu")
    user_choice = userChoice({1})
    match user_choice:
        case 1:
           loggedInMenu(connection, user, inventory, cart)

# Menu that display's the user's cart and information
def viewCart(connection, user, inventory, cart):
    print("1. View Cart\n2. Remove Item from Cart\n3. Checkout\n4. Go back to the menu")
    user_choice = userChoice({1, 2, 3, 4})
    match user_choice:
        case 1:
            cart.viewCart(connection, user.getUsername())
            viewCart(connection, user, inventory, cart)
        case 2:
            print("Please enter the movie id of the item you'd like to remove from your cart: ")
            movieId = input()
            cart.removeFromCart(connection, user.getUsername(), movieId)
            viewCart(connection, user, inventory, cart)
        case 3:
            cart.checkoutCart(connection, user.getUsername())
            viewCart(connection, user, inventory, cart)
        case 4:
            loggedInMenu(connection, user, inventory, cart)

# Menu that let's the user edit their account information

def editAccountInfo(connection, user, inventory, cart):
    print("1. Edit Shipping Information\n2. Edit Payment Information\n3. Delete Account\n4. Go back to the menu")
    user_choice = userChoice({1, 2, 3, 4})
    match user_choice:
        case 1:
            print("Edit Shipping Info")
            shipping_address = input("Enter shipping address: ")
            shipping_state = input("Enter shipping state: ")
            shipping_zipcode = intSpecificChoice("Enter shipping zip code: ")
            if (user.editAccount(connection, user.getUsername(), shipping_address, shipping_state, shipping_zipcode, None)):
                loggedInMenu(connection, user, inventory, cart)
        case 2:
            print("Edit Payment Info")
            ccnum = int(input("Enter credit card number: "))
            if (user.editAccount(connection, user.getUsername(), None, None, None, ccnum)):
                loggedInMenu(connection, user, inventory, cart)
        case 3:
            print("Are you sure you want to delete your account?")
            print("1. Yes\n2. No")
            confirm = userChoice({1, 2})
            match confirm:
                case 1:
                    logged_in = False;
                    if (user.deleteAccount(connection, user.getUsername())):
                        print("Deleted account returning to menu")

                        menu(connection, user, inventory, cart)
                    else:
                        print("Error deleting account")
                        loggedInMenu(connection, user, inventory, cart)
                case 2:
                    loggedInMenu(connection, user, inventory, cart)
        case 4:
            loggedInMenu(connection, user, inventory, cart)

        
# Menu that displays when the user is logged in       
def loggedInMenu(connection, user, inventory, cart):
    print("You're logged in",)
    print("1. View Items in Store\n2. View Order History\n3. Cart Information\n4. Edit Account Information\n5. Logout\n6. Exit Program")
    user_choice = userChoice({1, 2, 3, 4, 5, 6})
    match user_choice:
        case 1:
            viewStore(connection, user, inventory, cart)
        case 2:
            viewOrderHistory(connection, user, inventory, cart)
        case 3:
            viewCart(connection, user, inventory, cart)
        case 4:
            editAccountInfo(connection, user, inventory, cart)
        case 5:
            logged_in = False
            menu(connection, user, inventory, cart)
        case 6:
            print("Exiting the program")
            exit()

# Menu which display's when the user wants to log in
def login(connection, user, inventory, cart):
    print("1. Enter username and password\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
   
            print("Enter Username: ", end = '')
            username = input()
            print("Enter Password: ", end = '')
            password = input()
            
            if (user.login(connection, username, password)):
                logged_in = True
                loggedInMenu(connection, user, inventory, cart)
            else: 
                print("Invalid credentials, please try again.")
                login(connection, user, inventory, cart)
        case 2:
            menu(connection, user, inventory, cart)
       
    

    
# Menu that displays when the user wants to create an account
def createAccount(connection, user, inventory, cart):
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
        loggedInMenu(connection, user, inventory, cart)
    else:
        menu(connection, user, inventory, cart)

def menu(connection, user, inventory, cart):
    
    print("1. Login\n2. Create Account\n3. Exit Program")
    user_choice = userChoice({1, 2, 3})
    match user_choice:
        case 1:
            login(connection, user, inventory, cart)
        case 2:
            createAccount(connection, user, inventory, cart)
        case 3:
            print("Exiting the program")
            exit()
    
       
   
        

def main():
    inventory = Item()
    user = User()
    cart = ShoppingCart()
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="methods_project"
        )   
                
        menu(connection, user, inventory, cart)
        
    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

if __name__ == "__main__":
    main()