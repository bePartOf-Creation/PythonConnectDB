import mysql.connector
from mysql.connector import Error


def connect_init():
    global create_db
    try:
        create_db = mysql.connector.connect(
            host='localhost',
            user='Ocode',
            password='1n1f1x123201',
            auth_plugin='mysql_native_password')
        print('Creating a Database......')
        cursor = create_db.cursor()
        cursor.execute("CREATE DATABASE bankApp")
        my_db = cursor.fetchall()
        print('Your Database has Created..')
    except Error as e:
        print("Not connecting due to ", e)
    if create_db is not None and create_db.is_connected():
        create_db.close()
        print("Database Shutdown")


def main():
    connect_init()


if __name__ == '__main__':
    main()
