import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Shankar",
  passwd="Shankar@123",
  database="demodb1"
)

mycursor = mydb.cursor()

table_name = input("Enter the table name : ")

try:
    mycursor.execute("CREATE TABLE "+table_name+" (name VARCHAR(255), address VARCHAR(255))")
except:
    pass

limit = int(input("Enter the no.of Records to be inserted :"))

sql = "INSERT INTO "+table_name+" (name, address) VALUES (%s, %s)"

for _ in range(limit):
    name, address = input("Enter name and address : ").split()
    val = (name, address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted Successfully !!!")

mycursor.execute("select * from "+table_name)

for i in mycursor:
    print(i)
