import mysql.connector
from mysql.connector import Error
from CreateDB import *

account = input("Enter your Account Number: ")
if len(account) != 10:
    print("Invalid Account Number")
else:
    num = int(account)

Tob = input('Enter your TransactionDate in YYYY-MM-DD: ')
if Tob == "":
    print("TransactionDate is missing")

transaction_type = int(input("Enter 1 for ATM, Enter 2 for TRANSFER : "))
if transaction_type == 1:
    transaction_type = "ATM"
else:
    transaction_type = "TRANSFERS"

transaction_medium = input("Enter your Transaction medium: ")
if transaction_medium == "":
    print("Transaction medium must be entered")


def transaction_table():
    global create_transact
    try:
        create_transact = mysql.connector.connect(
            host='localhost',
            database='bankApp',
            user='Ocode',
            password='1n1f1x123201',
            auth_plugin='mysql_native_password'
        )
        print('Connection to the Database was successful')
        cursor = create_transact.cursor()

        sql_query = 'INSERT INTO TRANSACTIONS(AccountNumber, TransactionDate, TransactionTYpe ,TransactionMedium) ' \
                    'VALUES (%s, %s ,%s, %s) '
        values = [(account, Tob, 'active',transaction_type)]
        cursor.executemany(sql_query, values)
        create_transact.commit()
        print(cursor.rowcount, "Record Inserted Successfully.")

    except Error as e:
        print('Not connected due to ', e)
    finally:
        if create_transact is not None and create_transact.is_connected():
            create_transact.close()
            print('Database Shutdown')


def main():
    transaction_table()


if __name__ == '__main__':
    main()
