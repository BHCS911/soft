import mysql.connector


__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='sqluser', password='password',
                                host='127.0.0.1',
                                database='bhcs',
                                auth_plugin='mysql_native_password'                           
                                )
        return __cnx