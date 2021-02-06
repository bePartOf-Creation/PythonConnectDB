import mysql.connector
from mysql.connector import Error

first_name = input('Enter your FirstName: ')
if first_name == "":
    print("First name must be entered")

last_name = input('Enter your LastName: ')
if last_name == "":
    print("Last name must be entered")

middle_name = input('Enter your MiddleName: ')
if middle_name == "":
    print("MiddleName Must be Entered")

dob = input('Enter your DateOfBirth in YYYY-MM-DD: ')
if dob == "":
    print("DateOfBirth is missing")

phone = input('Enter Your Phone NUmber: ')
if len(phone) != 11:
    print("Invalid phone number")
else:
    phone_number = int(phone)

occupation = input('Enter your Occupation: ')
if occupation == "":
    print("This fields must be entered")


def insert_values():
    global conn
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='bankApp',
            user='Ocode',
            password='1n1f1x123201',
            auth_plugin='mysql_native_password'
        )
        print('Connection to the Database was successful')
        cursor = conn.cursor()

        sql_query = 'INSERT INTO Customer(FirstName, LastName, MiddleName, DateOfBirth, PhoneNumber, Occupation) ' \
                    'VALUES (%s, %s ,%s, %s, %s ,%s) '
        values = [(first_name, last_name, middle_name, dob, phone, occupation)]
        cursor.executemany(sql_query, values)
        conn.commit()
        print(cursor.rowcount, "Record Inserted Successfully.")

    except Error as e:
        print('Not connected due to ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database Shutdown')


def main():
    insert_values()


if __name__ == '__main__':
    main()
