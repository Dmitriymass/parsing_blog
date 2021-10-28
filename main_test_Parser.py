import pymysql.cursors
import requests
from bs4 import BeautifulSoup
import sqlite3


url = "https://blog.python.org/"
url_release = "https://www.python.org/downloads/release/python-3110a1/"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; \
                                x64; rv:47.0) Gecko/20100101 Firefox/48.0'}
response = requests.get(url, headers=header)
# if response.status_code == 200:
html = response.text

soup = BeautifulSoup(html, "lxml")
args = []
data_published = soup.find("h2", class_="date-header")
header = soup.find("h3", class_="post-title entry-title")
text = soup.find("div", class_="post hentry")
avtors = soup.find(class_="gmail_default").find_all("a")
for avtor in avtors:
    href = avtor.get("href")

args.append((data_published, header, text, avtors, avtors))

res = requests.get(url_release)
src = res.text

soup1 = BeautifulSoup(src, "lxml")
title = soup1.title.text
h1 = soup1.find("h1", class_="page-title").text
release_date = soup1.find("h1", class_="page-title").next_element.next_element.next_element.next_element.next
text = soup1.find("article", class_="text").text
old_href = soup1.find("article", class_="text").find_all("li")[0].find("a")["href"]
old_href_last = soup1.find("article", class_="text").find_all("li")
for item in old_href_last:
    link_href_attr = item("a")

conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()
cursor.executemany("INSERT INTO blog VALUES (?,?,?,?,?)", args)
conn.commit()
conn.close()


try:
    connection = pymysql.connect(
        host='localhost',
        port='1025',
        user='user',
        password='passwd',
        database='db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:

        with connection.cursor() as cursor:

            insert_query = "INSERT INTO 'blog'('data_published', 'header', 'text', 'avtors', 'href') VALUES(%s, %s, %s, %s, %s );"
            cursor.execute(insert_query)
            connection.commit()
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)