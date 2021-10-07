import mysql.connector

username = input("enter username: ")
databasename = input("enter database name: ")
password = input("enter password: ")
hostname = input("enter hostname: ")


try:
    conn = mysql.connector.connect(user = username, database=databasename, password = password, host= hostname, port= 3306)
    cursor = conn.cursor()
    mySql_Create_Table_Query = """CREATE TABLE emp ( 
                                 e_no int NOT NULL PRIMARY KEY ,
                                 ename varchar(250) NOT NULL,
                                 designation varchar(250) NOT NULL,
                                 sal int,
                                 mgr int,
                                 deptno int,
                                 FOREIGN KEY (deptno) REFERENCES dept(deptno)) """
    cursor = conn.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
except mysql.connector.ProgrammingError:
    print("table already exist")
