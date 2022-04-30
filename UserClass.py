class User:
  def __init__(self):
    self.username = ""
    self.firstname = ""
    self.lastname = ""
    self.password = ""
    self.shippingaddress = ""
    self.shippingstate = ""
    self.shippingzip = ""
    self.ccnum = ""

  
  
  def login(self, connection, username, password):
    cursor = connection.cursor()
    mypassword_queue =[]
    sql_query = "SELECT *FROM users WHERE username ='%s' AND password ='%s'" % (username, password)
    
    try:
      cursor.execute(sql_query)
      myresults =cursor.fetchall()
      for row in myresults:
        for x in row:
          mypassword_queue.append(x)
    except:
      print('error occured')
      
    if (username and password) in mypassword_queue:
      
      return True
    else:
           
            
        
        

              

  def createAccount(self, connection, username, firstname, lastname, password):
  
    cursor = connection.cursor()
    #cursor.execute("SELECT EXISTS(SELECT * from users WHERE username=%(username)s)", {'username' :username})
   

    #cursor.execute("SELECT username FROM users WHERE WHERE username=%(username)s)", {'username' :username})
    # cursor.execute("SELECT EXISTS(SELECT * from users WHERE username=%(username)s)", {'username' :username})
    # checkUsername = cursor.fetchone()
    # print(checkUsername)
    # if checkUsername != 0:
    #   print('Username does not exist')
    # else:
    #   print('Logged In!')
    query = "INSERT INTO users (username, firstname, lastname, password) VALUES (%s, %s, %s, %s)"
    data = (username, firstname, lastname, password)
    cursor.execute(query, data)
    connection.commit()
    print("Account created")
    self.username = username
    self.firstname = firstname
    self.lastname = lastname
    self.password = password
    return True
  
    
   

   
        