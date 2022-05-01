from psycopg2 import connect
from tabulate import tabulate

class Item:
  def __init__(self):
    self.itemid = None
    self.stock = None
    self.price = None
    self.title = ""

  def viewAll(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT itemid, title, price from items')
    result = cursor.fetchall()
    print(tabulate(result, headers=['Item ID', 'Title', 'Price'], tablefmt='psql'))

  def removeAmountFromStockOf(connection, quantity, itemid):
    stock = Item.getStockOf(connection, itemid)
    print('test:', stock)
    if (quantity > stock):
      return -1
    updatedStock = stock - quantity
    print('updated:', updatedStock)
    cursor = connection.cursor()
    cursor.execute('UPDATE items SET stock = %s WHERE itemid = %s', (updatedStock, itemid))
    connection.commit()
    return updatedStock

  def getStockOf(connection, itemid):
    cursor = connection.cursor()
    cursor.execute('SELECT stock FROM items WHERE itemid = %s', (itemid,))
    result = cursor.fetchall()
    for x in result:
      return x[0]
        