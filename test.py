import mysql_cursor

conn = mysql_cursor.Connection('home.dillenbeck.org', 'caleb', '/.ssh/id_rsa',
                               'caleb', '/sql_pass.txt', 'caleb')

users = conn.execute_read_query("SELECT USER_ID, PASS FROM LPCU WHERE USER_ID = 1")

print(users[0][1])

conn.close()
