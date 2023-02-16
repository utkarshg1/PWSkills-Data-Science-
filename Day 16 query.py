import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("SELECT * FROM test1.test1_table")
mycursor.execute("SELECT c1, c5 FROM test1.test1_table")
for i in mycursor.fetchall():
    print(i)
mydb.close()