import sqlite3

print("Welcome to your favorite Ice Cream Store")
#availableFlavors = ["chocolate", "vanilla", "strawberry"] 
while True:
    container = input("Do you prefer ice cream in a cone or in cup?\n")
    print(container)
    if container == ("cup" or "cone"):
        break

print("Order successfull")