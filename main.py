import sqlite3

# Connect to database
conn = sqlite3.connect("C:\\Users\\paul-\\Desktop\\projects\\python\\ice_cream_shop\\orders.db")
cur = conn.cursor()

print("Welcome to your favorite Ice Cream Store")

# Lets customer pick his preferred container and flavor
while True:
    container = input("Do you prefer ice cream in a cone or in cup?\n")
    if container.lower() in ["cup", "cone"]:
        break

while True:
    flavor = input("Which flavor would you like\n")
    if flavor.lower() in ["chocolate", "vanilla", "strawberry"]:
        break

cur.execute("INSERT INTO orders (container, flavor) VALUES (?, ?)", [container, flavor])
conn.commit()

# Fetch last Order from database
cur.execute("SELECT * FROM orders ORDER BY id DESC LIMIT 1")
order = cur.fetchone()

print(f"Your order:\nID: {order[0]}\nContainer: {order[1]}\nFlavor: {order[2]}")

# CLose connections
cur.close()
conn.close()

print("Order successfull")