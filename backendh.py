import sqlite3

def add():
    conn = sqlite3.connect("/home/asif/python3/GUI/hotelmanage/customer.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customers (ID INTEGER PRIMARY KEY, date TEXT, name TEXT, email  TEXT, package TEXT, num_of_room TEXT, room_type TEXT, food_type TEXT, room_no TEXT, addr TEXT, nationality TEXT, total_payment INTEGER)")
    conn.commit()
    conn.close()

def insert(date, name, email, package, num_of_room, room_type, food_type, room_no, addr, nationality, total_payment):
    conn = sqlite3.connect("/home/asif/python3/GUI/hotelmanage/customer.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO customers VALUES(NULL, ?,?,?,?,?,?,?,?,?,?,?)",(date, name, email, package, num_of_room, room_type, food_type, room_no, addr, nationality, total_payment))
    conn.commit()
    conn.close()
#insert("12-20-29", "asif", "asif@gmail.com","7 days","1","vip","vip","80","bangladesh","ban", 100 )

def view():
    conn = sqlite3.connect("/home/asif/python3/GUI/hotelmanage/customer.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(date="", email=""):
    conn = sqlite3.connect("/home/asif/python3/GUI/hotelmanage/customer.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE date=? OR email=?", (date, email))
    rows= cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def delete(id):
    conn = sqlite3.connect("/home/asif/python3/GUI/hotelmanage/customer.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(date, name, email, package, num_of_room, room_type, food_type, room_no, addr, nationality, total_payment):
    conn = sqlite3.connect("/home/asif/python3/pract.db")
    cur = conn.cursor()
    cur.execute("UPDATE customers SET date=?, name=?, package=?, num_of_room=?, room_type=?, food_type=?, room_no=?, addr=?, nationality=?, total_payment=? WHERE email=?",(date, name, package, num_of_room, room_type, food_type, room_no, addr, nationality, total_payment, email))
    conn.commit()
    conn.close()
