/* log in */
SELECT username
FROM   users
WHERE  username = g_username
       AND users.password = g_password /* check if user+pw combo exists */
/* create account */
SELECT username
FROM   users
WHERE  username = g_username /* check if username exists */

INSERT INTO users
VALUES      (g_username,
             g_firstname,
             g_lastname,
             g_password,
             g_shippingaddress,
             g_shippingstate,
             g_shippingzip,
             g_ccnum) /* create account */
/* view all items in a category */
SELECT title,
       price,
       itemid
FROM   items

/* view all items in user's cart */
SELECT items.title,
       items.price,
       cart.quantity
FROM   items
       INNER JOIN cart
               ON items.itemid = cart.itemid
WHERE  cart.ordered = 0
       AND cart.username = g_username

/* add item to shopping cart */
INSERT INTO cart
VALUES      (g_itemid,
             g_username,
             g_quantity,
             0)

/* remove item from cart */
DELETE FROM cart
WHERE  username = g_username
       AND itemid = g_itemid

/* checkout items in cart (and add order to order history) */
SELECT items.price,
       cart.quantity
FROM   items
       INNER JOIN cart
               ON items.itemid = carts.itemid
WHERE  username = g_username
       AND cart.ordered = 0

UPDATE cart
SET    ordered = 1
WHERE  username = g_username
       AND ordered = 0

/* view user's order history */
SELECT cart.itemid,
       items.title,
       items.price,
       cart.quantity
FROM   items
       INNER JOIN cart
               ON items.itemid = carts.itemid
WHERE  cart.username = g_username
       AND cart.ordered = 1

/* edit shipping info */
UPDATE users
SET    shippingaddress = g_shippingaddress,
       shippingstate = g_shippingstate,
       shippingzip = g_shippingzip
WHERE  username = g_username

/* edit payment info */
UPDATE users
SET    ccnum = g_ccnum
WHERE  username = g_username

/* delete account (with order history and cart data) */
DELETE FROM cart
WHERE  username = g_username

DELETE FROM users
WHERE  username = g_username 