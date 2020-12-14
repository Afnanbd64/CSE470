import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database= "Stocks"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM PRODUCTS")

for myresult in range ():
    myresult = mycursor.fetchone()
    print(myresult)

    
    





