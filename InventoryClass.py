from psycopg2 import connect


class Item:
  def __init__(self):
    self.itemid = None
    self.stock = None
    self.price = None
    self.title = ""

  def getQuantity(self, connection, itemid):
    cursor = connection.cursor()
    cursor.execute('SELECT quantity FROM item WHERE itemid = %d', (itemid,))
    result = cursor.fetchall()

  def createAccount(self, connection):
    print("Test")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    for x in result:
        print(x) ## all