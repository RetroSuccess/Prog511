account_number = int(input("What's your account number?: "))
account_type = input("Enter your account type ('s' for savings, 'c' for checking): ")
min_balance = float(input("What's the minimum balance for your account?: "))
current_balance = float(input("What is your current balance?: "))

# Check the account type
if account_type == "s":
    # Savings account
    if current_balance < min_balance:
        current_balance -= 10
        print(f"Account Number: {account_number}")
        print("Account type: Savings Account")
        print("Your balance was below the minimum.")
        print("A R10 service charge was taken.")
    else:
        current_balance += current_balance * 0.04
        print(f"Account Number: {account_number}")
        print("Account type: Savings Account")
        print("You earned 4% interest on your savings")

    print("Your updated balance is: R", round(current_balance, 2))

elif account_type == "c":
    # Checking account
    if current_balance < min_balance:
        current_balance -= 25
        print(f"Account Number: {account_number}")
        print("Account type: Checking account")
        print("Your balance was below the minimum")
        print("A R25 service charge was taken.")
    else:
        if current_balance <= min_balance + 5000:
            current_balance += current_balance * 0.03
            interest_rate = 3
        else:
            current_balance += current_balance * 0.05
            interest_rate = 5

        print("Account Number:", account_number)
        print("Account type: Checking account")
        print(f"You earned {interest_rate}% interest on your checking account")

    print("Your updated balance is: R", round(current_balance, 2))

else:
    print("You entered an invalid account type. Please use 's' or 'c'.")
