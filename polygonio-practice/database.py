import sqlite3

# define a connection and a cursos
# Connections are used to connect to a database

connection = sqlite3.connect("store_transactions.db")
cursor = connection.cursor()

# create stores table

command1="""CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)
"""

cursor.execute(command1)

# create purchase table

command2="""CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id) REFERENCES stores(store_id))"""
cursor.execute(command2)

# add to stores
cursor.execute("INSERT INTO stores VALUES (21,'Minneapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95,'Chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64,'Iowa City, IA')")


# add to purchase
cursor.execute("INSERT INTO purchases VALUES (43,12,43")
cursor.execute("INSERT INTO purchases VALUES (93,21,43)")
cursor.execute("INSERT INTO purchases VALUES (61,12.53)")

# get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id=79")

#delete

cursor.execute("DELETE FROM purchases WHERE purchase_id=43")