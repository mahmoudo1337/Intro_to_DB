import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="alx_book_store")

mycursor = mydb.cursor()
try:
  mycursor.execute("""
CREATE DATABASE IF NOT EXISTS alx_book_store
""")

except mysql.connector.Error:
  print("An error occured during the connection.")
  
  
print("Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()