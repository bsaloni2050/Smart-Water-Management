import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute('''DROP TABLE COMPANY''')
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

x = conn.execute('''Select * from COMPANY''')

for c in x:
    print (c[0])
    print (c[1])
    print (c[2])
    print (c[3])

conn.close()
