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


  def createAccount(self, connection):
    print("Test")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    for x in result:
        print(x) ## all
        