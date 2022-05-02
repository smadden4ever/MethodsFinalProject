from OrderClass import Order

class ShoppingCart:
    def __init__(self):
        self.id = ""
        self.uid = ""
        self.inventoryId = ""
        self.total = ""
        self.quantityBought = ""

    def viewCart(self, connection, uid):
        cursor = connection.cursor()
        ## sends query and grabs data
        ## SELECT queries return a tuple for each row
        cursor.execute("SELECT * FROM cart WHERE uid=%s", (uid,))
        ## only needed if you're running a SELECT
        ## this actually grabs the data
        result = cursor.fetchall()
        totalPrice = 0
        try:
            for x in result:
                cursor.execute("SELECT itemid, title FROM items WHERE itemid=%s", (x[2],))
                movie = cursor.fetchone()
                print("Movie ID: ", movie[0], "/Movie: ", movie[1], "/quantity in Cart: ", x[3], "/total: $", x[4] )
                totalPrice += x[4]
            print("Total Price for Order: $", totalPrice)
        except:
            print("Cart empty")

        connection.commit()

    def addToCart(self, connection, uid, movieId, quantityBought):
        cursor = connection.cursor()
        ##adds new inventory item to the cart
        cursor.execute("SELECT price FROM items WHERE itemid=%s", (movieId,))
        quantity = cursor.fetchone()[0]
        total = float(quantityBought) * float(quantity)
        print("Movie successfully added to cart. Your total is ", total)
        cursor.execute("INSERT INTO cart (uid, inventoryId, quantityBought, total) VALUES (%s, %s, %s, %s)", (uid, movieId, quantityBought, total))
        connection.commit()

    def removeFromCart(self, connection, uid, MovieId):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cart WHERE uid=%s AND inventoryId=%s", (uid, MovieId))
        print("Movie successfully removed from cart")
        connection.commit()

    def checkoutCart(self, connection, uid):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cart WHERE uid=%s", (uid,))
        result = cursor.fetchall()
        orderString = ""
        try:
            for x in result:
                cursor.execute("SELECT itemid, title FROM items WHERE itemid=%s", (x[2],))
                movie = cursor.fetchone()
                orderString += ("Movie ID: " + str(movie[0]) + "/Movie: " + str(movie[1]) + "/quantity Bought: " + str(x[3]) + "/total: $" + str(x[4]) + "\n")
                
            order = Order()
            order.addToOrderHistory(connection, uid, orderString)
            cursor.execute("DELETE FROM cart WHERE uid=%s", (uid,))
            connection.commit()
        except:
            print("something")


