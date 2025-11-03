#impoting date time to log the transaction details
import datetime
class ATM():
    def __init__(self,bank_name,branch_location,balance,acnt_holder_name):
        self.bank_name = bank_name
        self.branch_location = branch_location
        self.balance = balance
        self.acnt_holder_name = acnt_holder_name
        self.transactions = []

    def withdraw(self,amount=None):
        
        if amount is None:
            amount = float(input("Enter the withdrawl amount: Rs. "))
        if amount > self.balance:   # if withdrawl amount if more than the acount balance
            print("Insufficient funds")
            return
        self.balance -= amount
        # to get the type of transaction, debited amount and time stamp on the mini statement, appending the log details 
        self.transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Wecome to {self.bank_name} Bank")
        print(f"Amount Withdrawn is: Rs.{amount}")
        print(f"Total Balance in {self.bank_name} is: Rs.{self.balance}")
        
    def deposit(self, amount=None):
        if amount is None:
            amount = float(input("Enter the withdrawl amount: Rs. "))
        self.balance += amount
        # to get the type of transaction, credited amount and time stamp on the mini statement, appending the log details 
        self.transactions.append({
        "type": "Deposit",
        "amount": amount,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })   
        print(f"Wecome to {self.bank_name} Bank")
        print(f"Amount deposited is: Rs.{amount}")
        print(f"Total Balance in {self.bank_name} is: Rs.{self.balance}")

    def mini_statement(self,):
        print(" ")
        print(f"Wecome to {self.bank_name} Bank")
        print(f"\nMini statement for {self.acnt_holder_name}")
        print(f"Current balance in {self.bank_name} is: {self.balance}")
        print("Recent transactions: ")
        print("-"*40)
        for txn in self.transactions[-5:]:  # Shows last 5 transactions
            print(f"{txn['time']} - {txn['type']}: Rs.{txn['amount']}")
        print("-"*40)

    def exit(self, ):
        print("-"*40)
        print(f"Thank you for banking with {self.bank_name} Bank!")
    
SBI = ATM("SBI","Charminar",10000,"Pooja")
HDFC = ATM("HDFC","Kondapur",20000,"Pooja")
Axis = ATM("Axis","West Maredpally",30000,"Pooja")
ICICI = ATM("ICICI","Gachibowli",40000,"Pooja")
SBI.mini_statement()
ICICI.deposit()
Axis.withdraw()
HDFC.mini_statement()
Axis.mini_statement()
ICICI.exit()
Axis.deposit()
