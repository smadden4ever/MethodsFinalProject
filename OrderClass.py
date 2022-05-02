class Order:
    def __init__(self):
        self.id = ""
        self.uid = ""
        self.orderString = ""

    def viewOrderHistory(self, connection, uid):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE uid=%s", (uid,))
        result = cursor.fetchall()
        try:
            for x in result:
                print("---------------------")
                print(x[2])
                print("Total order cost:", x[3])
        except:
            print("No order history")

    def addToOrderHistory(self, connection, uid, orderString):
        cursor = connection.cursor()
        cursor.execute("SELECT total FROM cart WHERE uid=%s", (uid,))
        result = cursor.fetchall()
        total = 0.0
        for x in result:
            total += float(x[0])
        print(total)
        cursor.execute("INSERT INTO orders (uid, orderString, total) VALUES (%s, %s, %s)", (uid, orderString, total))
        print("Order successfully placed")
        connection.commit()