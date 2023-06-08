import sqlite3

# Connect to database
conn = sqlite3.connect("C:\\Users\\paul-\\Desktop\\projects\\python\\ice_cream_shop\\orders.db")
cur = conn.cursor()

print("+---------------------------------+")
print("Welcome to your favorite Ice Cream Store")
print("+---------------------------------+")

# Check if customer already exists in table
name = input("Whats your name?\n")
print("+---------------------------------+")
name = name.lower()
cur.execute("SELECT * FROM customers WHERE name = ?", [name])
order = cur.fetchone()

if order == None:
    cur.execute("INSERT INTO customers (name) VALUES (?)", [name])
    conn.commit()

cur.execute("SELECT id FROM customers WHERE name = ?", [name])
id = cur.fetchone()[0]

# Lets customer pick his preferred container and flavor
while True:
    container = input("Do you prefer ice cream in a cone or in cup?\n")
    if container.lower() in ["cup", "cone"]:
        break
print("+---------------------------------+")

while True:
    flavor = input("Which flavor would you like\n")
    if flavor.lower() in ["chocolate", "vanilla", "strawberry"]:
        break
print("+---------------------------------+")

cur.execute("INSERT INTO orders (container, flavor, customer_id) VALUES (?, ?, ?)", [container, flavor, id])
conn.commit()

# Fetch last Order from database
cur.execute("SELECT * FROM orders JOIN customers ON orders.customer_id = customers.id ORDER BY id DESC LIMIT 1")
order = cur.fetchone()

print(f"ORDER SUCCESSFULL - YOUR ORDER:\nID: {order[0]}\nContainer: {order[1]}\nFlavor: {order[2]}\nCustomer ID: {order[3]}")
print("+---------------------------------+")
# CLose connections
cur.close()
conn.close()