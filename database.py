import sqlite3

conn = sqlite3.connect("mydata.db")

sql = "CREATE TABLE blog (data_published TEXT, header TEXT, text TEXT, avtors TEXT, href TEXT NOT NULL PRIMARY KEY)"
sql = "CREATE TABLE release (title TEXT, h1 TEXT, release_date TEXT, href TEXT REFERENCES blog(href), old_href,TEXT, old_href_last TEXT)"
# sql = "SELECT * FROM books"
cursor = conn.cursor()
cursor.execute(sql)
#
# res = cursor.fetchall()
#
# for r in res:
#     print("Name:", r[0])
#     print("Price:", r[1])

conn.close()





# conn = sqlite3.connect("mydata.db")
# cursor = conn.cursor()

# sql = "CREATE TABLE books (name TEXT, price TEXT, description TEXT, info TEXT)"
# sql = "SELECT * FROM books"
# cursor.execute(sql)
# res = cursor.fetchall()
# print(res)
# sql = "INSERT INTO books VALUES (?, ?, ?, ?)"