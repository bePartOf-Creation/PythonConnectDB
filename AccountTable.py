import mysql.connector
from mysql.connector import Error
from CreateDB import *
from myUtils import *

account_num = input("Enter your Account Number: ")
if len(account_num) != 10:
    print("Invalid Account Number")
else:
    num = int(account_num)

account_type = int(input("Enter 1 for Saving Account, Enter 2 for Current Account : "))
if account_type == 1:
    account_type = "savings"
else:
    account_type = "current"

aob = input('Enter your TransactionDate in YYYY-MM-DD: ')
if aob == "":
    print("TransactionDate is missing")


def account_table():
    global connect
    try:
        connect = mysql.connector.connect(
            host='localhost',
            database='bankApp',
            user='Ocode',
            password='1n1f1x123201',
            auth_plugin='mysql_native_password'
        )
        print('Connection to the Database was successful')
        cursor = connect.cursor()

        sql_query = 'INSERT INTO Account(AccountNumber, AccountType, AccountStatus ,AOD) ' \
                    'VALUES (%s, %s ,%s, %s) '
        values = [(account_num, account_type, 'active', aob )]
        cursor.executemany(sql_query, values)
        connect.commit()
        print(cursor.rowcount, "Record Inserted Successfully.")

    except Error as e:
        print('Not connected due to ', e)
    finally:
        if connect is not None and connect.is_connected():
            connect.close()
            print('Database Shutdown')


def main():
    account_table()


if __name__ == '__main__':
    main()