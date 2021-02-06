def collect_account_number() -> str:
    account_number = input('Enter Account Number: ')
    return account_number


def validate_account_number(account_number: str) -> bool:
    if len(account_number) != 10:
        return False
    else:
        return True


def create_account(account_number: str) -> None:
    sql_query = 'INSERT INTO Account(AccountNumber, AccountBalance, AccountType, AccountStatus, AOD) VALUES (%s, %s ,' \
                '%s, %s, %s) '


def deposit(account_number: str) -> str:
    amount = input('Enter your Deposit amount : ')
    sql_query = 'UPDATE Account SET AccountBalance = AccountBalance + ' + amount + ' WHERE AccountNumber = ' + account_number
    return sql_query


def withdraw(account_number: str) -> None:
    amount = input('Enter your Withdrawal amount : ')
    sql_query = 'UPDATE Account SET AccountBalance = AccountBalance - ' + amount + ' WHERE AccountNumber = ' + account_number
    print(sql_query)


def main():
    # collect the account number
    user_account_number: str = collect_account_number()

    # validate account number return true/false if acct num is valid
    is_valid = validate_account_number(user_account_number)
    if not is_valid:
        print("Invalid Account Number!")
        return

    # create account (balance will be zero initially
    create_account(user_account_number)

    # pay some money into account
    deposit(user_account_number)

    # withdraw money from account
    withdraw(user_account_number)


def run_tests():
    assert validate_account_number("1000000") == False, "1000000 is not a valid account number"
    assert validate_account_number("1234567891") == True, "1234567891 is a valid account number"


if __name__ == '__main__':
    run_tests()
    main()
