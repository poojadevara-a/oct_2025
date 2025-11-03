################# ATM Functions Task ##################

balance = 50000
user = "Pooja"
#To generate the mini statement to store the credit and debit details, taken transactions empty list to log the transaction details
transactions = []
#impoting date time to log the transaction details
import datetime
#debit functions given
def debit():
    global balance
    amount = float(input("Enter the withdrawl amount: Rs. "))
    if amount > balance:   # if withdrawl amount if more than the acount balance
        print("Insufficient funds")
    else:
        balance -= amount
        # to get the type of transaction, debited amount and time stamp on the mini statement, appending the log details 
        transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Wecome, {user}")
        print(f"Amount Withdrawn is: Rs.{amount}")
        print(f"Total Balance is: Rs.{balance}")
        print(f"To withdraw again press 1. Withdraw Money")
# credit functions given
def credit():
    global balance
    amount = float(input("Enter the amount to be deposited: Rs. "))
    balance += amount
    # to get the type of transaction, credited amount and time stamp on the mini statement, appending the log details 
    transactions.append({
        "type": "Deposit",
        "amount": amount,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })   
    print("Wecome, {user}")
    print(f"Amount deposited is: Rs.{amount}")
    print(f"Total Balance is: Rs.{balance}")
# functions for checking balance
def check_balance():
    global balance
    print(f"Your account balance is: Rs.{balance}")
# functions for pin change
def pin_change():
    old_input = int(input("Enter your old pin: "))
    new_input = int(input("Enter your new pin: "))
    print(f"{user} pin changed successfully!")
# functions to get mini statement
def mini_statement():
    print(f"\nMini statement of {user}")
    print(f"Current balance is: {balance}")
    print("Recent transactions: ")
    for txn in transactions[-5:]:  # Shows last 5 transactions
        print(f"{txn['time']} - {txn['type']}: Rs.{txn['amount']}")

# used while condition to iterate

while True:
    print("\nATM Menu")
    print("1. Withdraw Money")
    print("2. Deposit Money")
    print("3. To check Balance")
    print("4. For Pin change")
    print("5. For Mini statement")
    print("6. Exit")
    
    choice = input("Please select the numbers from (1-6): ")

    if choice == "6":
        print("Thank you for banking with us!")
        break   
    elif choice == "1":
        debit()
        print("Thank you for banking with us!")
    elif choice == "2":
        credit()
        print("Thank you for banking with us!")
    elif choice == "3":
        check_balance()
        print("Thank you for banking with us!")
    elif choice == "4":
        pin_change()
        print("Thank you for banking with us!")
    elif choice == "5":
        mini_statement()
        print("Thank you for banking with us!")
    elif choice == "6":
        print("Thank you for banking with us!")
        print("Do not forget to takeout your card!")
        break
    else:
        print("Invalid input. Please enter the correct number")





