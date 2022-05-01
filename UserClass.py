class User:
    def __init__(self):
        self.username = ""
        self.firstname = ""
        self.lastname = ""
        self.password = ""
        self.shippingaddress = ""
        self.shippingstate = ""
        self.shippingzip = None
        self.ccnum = None

    def getUsername(self):
        return self.username

    def deleteAccount(self, connection, username):
        print(username)
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE username=%s"

        data = (username,)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        return True

    def editAccount(self, connection, username, shippingaddress, shippingstate, shippingzip, ccnum):
        cursor = connection.cursor()
        if (shippingaddress):
            sql = "UPDATE users SET shippingaddress = %s, shippingstate = %s, shippingzip = %s WHERE username = %s"
            val = (shippingaddress, shippingstate, shippingzip, username)
            cursor.execute(sql, val)
            connection.commit()
            self.shippingaddress = shippingaddress
            self.shippingstate = shippingstate
            self.shippingzip = shippingzip
            cursor.close()
            return True
        else:
            sql = "UPDATE users SET ccnum = %s WHERE username = %s"
            val = (ccnum, username)
            cursor.execute(sql, val)
            connection.commit()
            self.ccnum = ccnum
            cursor.close()
            return True

    def login(self, connection, username, password):
        cursor = connection.cursor()
        mypassword_queue = []
        sql_query = "SELECT *FROM users WHERE username ='%s' AND password ='%s'" % (
            username, password)

        try:
            cursor.execute(sql_query)
            myresults = cursor.fetchall()
            for row in myresults:
                for x in row:
                    mypassword_queue.append(x)
        except:
            print('error occured')

        if (username and password) in mypassword_queue:
            self.username = username
            self.password=  password
            cursor.close()
            cursor = connection.cursor()
            cursor.execute("SELECT * from users WHERE username=%s", (username,))
            checkUserData = cursor.fetchone()
            self.firstname = checkUserData[1]
            self.lastname = checkUserData[2]
            self.shippingaddress = checkUserData[4]
            self.shippingstate = checkUserData[5]
            self.shippingzip = checkUserData[6]
            self.ccnum = checkUserData[7]
            cursor.close()
            return True

        else:
            cursor.close()
            return False

    def createAccount(self, connection, username, firstname, lastname, password, shipping_address, shipping_state, shipping_zip, ccnum):

        cursor = connection.cursor()
        cursor.execute(
            "SELECT EXISTS(SELECT * from users WHERE username=%(username)s)", {'username': username})
        checkUsername = cursor.fetchone()

        if (checkUsername[0] == 0):
            query = "INSERT INTO users (username, firstname, lastname, password, shippingaddress, shippingstate, shippingzip, ccnum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (username, firstname, lastname, password,
                    shipping_address, shipping_state, shipping_zip, ccnum)
            try:
                cursor.execute(query, data)
                connection.commit()
                print("Account created")
                self.username = username
                self.firstname = firstname
                self.lastname = lastname
                self.password = password
                self.shippingaddress = shipping_address
                self.shippingstate = shipping_state
                self.shippingzip = shipping_zip
                self.ccnum = ccnum
              
                cursor.close()
                return True
            except:
                print('Account not created')
        else:
            print("Account already exists")
            cursor.close()
            return False
