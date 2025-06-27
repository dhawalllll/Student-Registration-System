import sqlite3

con = sqlite3.connect("mydb.db")

c = con.cursor()

#c.execute("create table student(id INTEGER PRIMARY KEY AUTOINCREMENT, fullname TEXT, email TEXT, password TEXT)")

#c.execute("alter table student add address  varchar(100)")

c.execute("alter table student add column photo varchar(500)")




con.commit()
con.close()
