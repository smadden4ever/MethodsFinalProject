from tabulate import tabulate

class Item:
    def __init__(self):
        self.stock = ""
        self.price = ""
        self.title = ""
        self.itemid = ""


    def viewAll(self, connection):
        cursor = connection.cursor()
        cursor.execute('SELECT itemid, title, price, stock from items')
        result = cursor.fetchall()
        print(tabulate(result, headers=['Movie ID', 'Title', 'Price', 'Stock Available'], tablefmt='psql'))

    def removeAmountFromStockOf(self, connection, quantity, itemid):
        stock = self.getStockOf(connection, itemid)
        if (int(quantity) > int(stock)):
            print("Not enough in stock")
            return False
        updatedStock = int(stock) - int(quantity)
        cursor = connection.cursor()
        cursor.execute('UPDATE items SET stock = %s WHERE itemid = %s', (int(updatedStock), itemid, ))
        connection.commit()
        return True

    def getStockOf(self, connection, itemid):
        cursor = connection.cursor()
        cursor.execute('SELECT stock FROM items WHERE itemid = %s', (itemid,))
        result = cursor.fetchall()
        for x in result:
            return x[0]
