/* log in */
select username from users where username = g_username and users.password = g_password /* check if user+pw combo exists */

/* create account */
select username from users where username = g_username /* check if username exists */
insert into users values (g_username, g_firstname, g_lastname, g_password, g_shippingaddress, g_shippingstate, g_shippingzip, g_ccnum) /* create account */

/* view all items in a category */
select title, price, itemid from items

/* view all items in user's cart */
select items.title, items.price, cart.quantity from items inner join cart on items.itemid = cart.itemid where cart.ordered = 0 and cart.username = g_username

/* add item to shopping cart */
insert into cart values (g_itemid, g_username, g_quantity, 0)

/* remove item from cart */
delete from cart where username = g_username and itemid = g_itemid

/* checkout items in cart (and add order to order history) */
select items.price, cart.quantity from items inner join cart on items.itemid = carts.itemid where username = g_username and cart.ordered = 0
update cart set ordered = 1 where username = g_username and ordered = 0

/* view user's order history */
select cart.itemid, items.title, items.price, cart.quantity from items inner join cart on items.itemid = carts.itemid where cart.username = g_username and cart.ordered = 1

/* edit shipping info */
update users set shippingaddress = g_shippingaddress, shippingstate = g_shippingstate, shippingzip = g_shippingzip where username = g_username

/* edit payment info */
update users set ccnum = g_ccnum where username = g_username

/* delete account (with order history and cart data) */
delete from cart where username = g_username
delete from users where username = g_username