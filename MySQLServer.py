import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="alx_book_store")

mycursor = mydb.cursor()
try:
  mycursor.execute("""
CREATE TABLE IF NOT EXISTS alx_book_store (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
)
""")

except Exception as e:
  print(e)
  
  
print("Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()