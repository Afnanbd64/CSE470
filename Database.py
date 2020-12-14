import mysql.connector
mydb = mysql.connector.connect(host= "localhost", user ="root", passwd="123456", database= "stock")
mycursor = mydb.cursor()
mycursor.execute("Show database")

for tb in mycursor:
    print(tb)
    