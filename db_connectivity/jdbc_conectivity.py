import pymysql

# step 1 - connet to database
connection=pymysql.connect(
    host="localhost",
    user='root',
    password='root',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:

        # step 2 create a table
        create_query="""
        CREATE TABLE IF NOT EXISTS employees(
        id INT  AUTO_INCREMENT PRIMARY KEY ,
        name VARCHAR(100),
        department VARCHAR(100)
        );"""
        cursor.execute(create_query)

#step 3 -- INSERT DATA

        insert_query="INSERT INTO employees (name ,department) VALUES (%s ,%s)"
        values=[("john","IT"),("sembiyan","data engineer"),("smith","HR"),("steve rogger","Team Leader")]
        cursor.executemany(insert_query,    values)
        connection.commit()

#step 4 : select Data
        select_query="SELECT * FROM employees"
        cursor.execute(select_query)
        result=cursor.fetchall()

        #  for row in result:       
         #  print(row)

#write the output in another file
        with open("employees_output.txt","w") as f:
            for row in result:
                f.write(f'{row}\n')

finally:
    connection.close()
