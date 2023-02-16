import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2334,'utkarsh',45.62,34,'example')")
mycursor.execute("insert into test1.test1_table values (2335,'utkarsh1',85.62,34,'example_final')")
mydb.commit()
mydb.close()