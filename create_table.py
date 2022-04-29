import psycopg2
from config import config
def create_tables():
    commands = (
        """
        create table items (
	        itemid serial primary key,
	        stock int,
	        price int,
	        title varchar(50)
        )
        """,
        """
        create table users (
	        username varchar(25) primary key,
	        firstname varchar(30),
	        lastname varchar(30),
	        password varchar(50),
	        shippingaddress varchar(100),
	        shippingstate varchar(20),
	        shippingzip int,
	        ccnum int
        )
        """,
        """
        create table cart (
	        cartid serial primary key,
	        itemid int not null references items(itemid),
	        username varchar(25) not null references users(username),
	        quantity int,
	        orderid int,
	        ordered bool
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
