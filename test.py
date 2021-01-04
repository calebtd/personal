import mysql_cursor

conn = mysql_cursor.Connection('home.dillenbeck.org', 'caleb', '/.ssh/id_rsa',
                               'caleb', '/sql_pass.txt', 'caleb')

users = conn.execute_read_query("SELECT * FROM LPCU")

print(users)

if 'Caleb' in users:
    print('True')
else:
    print('False')

conn.close()
