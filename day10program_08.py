import sqlite3 as lite
con = lite.connect('mtica.db')

cur = con.cursor()
cur.execute("drop table if exists cars")
cur.execute('''Create table cars(
        Id int,Name text,price int)''')
print("table cars created.")
cur.execute("Insert into cars values(1,'Audi',52542)")
cur.execute("Insert into cars values(2,'Mercedes',57127)")

cur.execute("Insert into cars values(3,'Skoda',57127)")
cur.execute("Insert into cars values(4,'Volvo',57127)")
cur.execute("Insert into cars values(5,'Bently',57127)")
cur.execute("Insert into cars values(6,'Citroen',57127)")
cur.execute("Insert into cars values(7,'Hummer',57127)")

con.commit()
print("values in table car inserted.")




