import mysql.connector
from mysql.connector import Error


create_tb = None


def my_bank_tables():
    try:
        create_tbl = mysql.connector.connect(
            host='localhost',
            database='bankApp',
            user='Ocode',
            password='1n1f1x123201',
            auth_plugin='mysql_native_password'
        )
        print('Connection to the Database was successful')
        print('Creating Tables')

        customer = 'CREATE TABLE Customer(''CustomerId INT NOT NULL AUTO_INCREMENT,' \
                                           'FirstName VARCHAR(35) NOT NULL,' \
                                           'LastName VARCHAR (35) NOT NULL,' \
                                           'MiddleName VARCHAR (35) NOT NULL,' \
                                           'DateOfBirth DATE  NOT NULL,' \
                                           'PhoneNumber VARCHAR(11),' \
                                           'Occupation VARCHAR (20),' \
                                           'CONSTRAINT  customer_pk PRIMARY KEY(CustomerId));'

        account = 'CREATE TABLE Account(' 'AccountNumber VARCHAR(12) NOT NULL,' \
                                          'CustomerId INT NOT NULL AUTO_INCREMENT,' \
                                          'AccountType VARCHAR (20) NOT NULL,' \
                                          'AccountStatus VARCHAR (15) NOT NULL,' \
                                          'AOD DATE  NOT NULL,' \
                                          'CONSTRAINT Account_pk PRIMARY KEY(AccountNumber),' \
                                          'CONSTRAINT fk_Customer_Account FOREIGN KEY(CustomerId)' \
                                          'REFERENCES Customer(CustomerId));'

        transaction = 'CREATE TABLE TRANSACTIONS(TransactionId INT NOT NULL AUTO_INCREMENT,' \
                      'AccountNumber VARCHAR (12) NOT NULL,' \
                      'TransactionDate DATE NOT NULL,' \
                      'TransactionTYpe VARCHAR(20),' \
                      'TransactionMedium  VARCHAR (15),' \
                      'CONSTRAINT  Transaction_pk PRIMARY KEY(TransactionId),' \
                      'CONSTRAINT fk_Account_Transaction FOREIGN KEY(AccountNumber)' \
                      'REFERENCES Account(AccountNumber));'

        cursor = create_tbl.cursor()
        cursor.execute(transaction)
        records = cursor.fetchall()
        print('Customer Table Has been Created')
        print('Account Table Has been Created')
        print('Transaction Table Has been Created')

    except Error as e:
        print('Not connecting due to ', e)
    finally:
        if create_tbl is not None and create_tbl.is_connected():
            create_tbl.close()
            print('Database ShutDown')





def main():
    my_bank_tables()


if __name__ == '__main__':
    main()




