import sqlite3
con=sqlite3.Connection('phonebookdb')
cur=con.cursor()
cur.execute('select * from phonebook')
print cur.fetchall()
