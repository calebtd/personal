import pandas as pd
import paramiko
import pymysql
from os.path import expanduser
from sshtunnel import SSHTunnelForwarder


class Connection:
    """Takes all the variables needed to make a connection"""

    def __init__(self, ssh_host, ssh_port, ssh_user, ssh_key,
                 sql_host, sql_port, sql_user, sql_pass, sql_name):
        self.ssh_host = ssh_host
        self.ssh_port = ssh_port
        self.ssh_user = ssh_user

        self.sql_host = sql_host
        self.sql_port = sql_port
        self.sql_user = sql_user
        self.sql_pass = sql_pass
        self.sql_name = sql_name

        home = expanduser('~')
        self.ssh_key = paramiko.RSAKey.from_private_key_file(home + ssh_key)

        self.tunnel = SSHTunnelForwarder(
            ssh_host=self.ssh_host,
            ssh_port=self.ssh_port,
            ssh_username=self.ssh_user,
            ssh_pkey=self.ssh_key,
            remote_bind_address=(self.sql_host, self.sql_port))

        self.tunnel.start()

        self.connection = pymysql.connect(host='127.0.0.1', user=self.sql_user,
                                          passwd=self.sql_pass, db=self.sql_name,
                                          port=self.tunnel.local_bind_port)
        # self.cursor = self.connection.cursor()

    def run_query(self, input_query):
        """Takes a string of a query to run.
            query: a SQL query on the database of the connection
            returns: the results of the query
            :rtype: object"""

        data = pd.read_sql_query(input_query, self.connection)

        return data

    def close(self):
        """Call this once we're done making queries"""

        self.connection.close()
        self.tunnel.close()


if __name__ == "__main__":
    conn = Connection('home.dillenbeck.org', 22, 'caleb', '/.ssh/id_rsa',
                      'localhost', 3306, 'caleb', '', 'caleb')

    # accountBalance = 42.22

    # query = 'UPDATE LPCU SET BALANCE = 32.22 WHERE USER_ID = 1'
    query = 'SELECT BALANCE FROM LPCU WHERE USER_ID = 1;'

    print(conn.run_query(query))

    # print(conn.run_query('SELECT BALANCE FROM LPCU WHERE USER_ID = 1;')['BALANCE'][0])

    conn.close()

    # ssh_host, ssh_port, ssh_user, ssh_key,
    # sql_host, sql_port, sql_user, sql_pass, sql_name
