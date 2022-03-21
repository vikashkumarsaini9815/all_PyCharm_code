import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")