import mysql.connector
import paramiko
# from mysql.connector import Error
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser


class Connection:
    """Takes all the variables needed to make a connection"""

    def __init__(self, ssh_host, ssh_user, ssh_key_path,
                 sql_user, sql_pass_path, sql_name):
        self.connection = None
        home = expanduser('~')
        ssh_key = paramiko.RSAKey.from_private_key_file(home + ssh_key_path)

        sql_pass_file = open(home + sql_pass_path, 'r')
        sql_pass = sql_pass_file.read()
        sql_pass_file.close()

        self.tunnel = SSHTunnelForwarder(
            ssh_host=ssh_host,
            ssh_port=22,
            ssh_username=ssh_user,
            ssh_pkey=ssh_key,
            remote_bind_address=('127.0.0.1', 3306))

        self.tunnel.start()

        self.connection = mysql.connector.connect(
            host='127.0.0.1',
            user=sql_user,
            password=sql_pass,
            database=sql_name,
            port=self.tunnel.local_bind_port
        )

    def execute_query(self, query):
        """Takes a query to execute for updating, inserting, etc."""
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return 'Done'

    def execute_read_query(self, query):
        """Takes a query to execute for reading, such as select"""
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def close(self):
        """Call this once we're done making queries"""
        self.connection.close()
        self.tunnel.close()


if __name__ == "__main__":
    conn = Connection('home.dillenbeck.org', 'caleb', '/.ssh/id_rsa',
                      'caleb', '/sql_pass.txt', 'caleb')

    read = "SELECT BALANCE FROM LPCU WHERE USER_ID = 1"

    update = "UPDATE LPCU SET BALANCE = 56.56 WHERE USER_ID = 1"

    query_result = conn.execute_read_query(read)
    print(query_result[0][0])

    # print(conn.execute_query(update))

    conn.close()

# ssh_host, ssh_user, ssh_key,
# sql_user, sql_pass, sql_name
