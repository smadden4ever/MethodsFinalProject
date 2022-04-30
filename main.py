# Remove these fake credentials once database works
fake_username = "admin"
fake_password = "password"
logged_in = False;

from UserClass import User
import mysql.connector
import sys

    

# Userchoice function that does basic input test with values being amount of choices
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
def viewStore():
    print("1. Choose Category\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
            print("Store info:")
            loggedInMenu()
        case 2:
            loggedInMenu()

# Menu that display's when the user wants to view items in the store 
def viewOrderHistory():
    print("View Order History:")
    print("1. Go back to the menu")
    user_choice = userChoice({1})
    match user_choice:
        case 1:
           loggedInMenu()

# Menu that display's the user's cart and information
def viewCart():
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
            loggedInMenu()
        case 4:
            loggedInMenu()

# Menu that let's the user edit their account information

def editAccountInfo():
    print("1. Edit Shipping Information\n2. Edit Payment Information\n3. Delete Account\n4. Go back to the menu")
    user_choice = userChoice({1, 2, 3, 4})
    match user_choice:
        case 1:
            print("Edit Shipping Info")
            loggedInMenu()
        case 2:
            print("Edit Payment Info")
            loggedInMenu()
        case 3:
            print("Are you sure you want to delete your account?")
            print("1. Yes\n2. No")
            confirm = userChoice({1, 2})
            match confirm:
                case 1:
                    logged_in = False;
                    print("Deleted account returning to menu")
                    menu()
                case 2:
                    loggedInMenu()
        case 4:
            loggedInMenu()


# Menu that display's when the user wants to view items in the store 
def viewStore():
    print("1. Choose Category\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
            print("Store info:")
            loggedInMenu()
        case 2:
            loggedInMenu()
       
        
# Menu that displays when the user is logged in       
def loggedInMenu():
    print("1. View Items in Store\n2. View Order History\n3. Cart Information\n4. Edit Account Information\n5. Logout\n6. Exit Program")
    user_choice = userChoice({1, 2, 3, 4, 5, 6})
    match user_choice:
        case 1:
            viewStore()
        case 2:
            viewOrderHistory()
        case 3:
            viewCart()
        case 4:
            editAccountInfo()
        case 5:
            logged_in = False;
            menu()
        case 6:
            print("Exiting the program")
            exit()

# Menu which display's when the user wants to log in
def login():
    print("1. Enter username and password\n2. Go back to the menu")
    user_choice = userChoice({1, 2})
    match user_choice:
        case 1:
   
            print("Enter Username: ", end = '')
            username = input();
            print("Enter Password: ", end = '')
            password = input();

            sql = """
                    SELECT username 
                    FROM   users
                    WHERE  username = %(username)s
                        AND users.password = %(password)s
                    """
            data = ()
            conn = None
            try:
                # read database configuration
                params = config()
                # connect to the PostgreSQL database
                conn = psycopg2.connect(**params)
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, {'username': username, 'password': password})
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            if ((username == fake_username) & (password == fake_password)):
                logged_in = True
                loggedInMenu()
            else: 
                print("Invalid credentials, please try again.")
                login()
        case 2:
            menu()
       
    

    
# Menu that displays when the user wants to create an account
def createAccount():
    print("Enter username and password to create")

# The main menu 
def menu():
    print("1. Login\n2. Create Account\n3. Exit Program")
    user_choice = userChoice({1, 2, 3})
    match user_choice:
        case 1:
            login()
        case 2:
            createAccount()
        case 3:
            print("Exiting the program")
            exit()
    
       
   
        

def main():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="methodsproject"
        )
    
        # p1 = User("John", 36)
        # p1.myfunc()
        menu()

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

if __name__ == "__main__":
    main()
