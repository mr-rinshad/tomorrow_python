class BankAccount:
    # Constructor
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")
        print("Updated Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")
            print("Updated Balance:", self.balance)

    def display(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# --- Main Program ---
print("Enter Account Details:")
acc_no = input("Account Number: ")
name = input("Account Holder Name: ")
acc_type = input("Type of Account: ")
balance = float(input("Initial Balance: "))

acc = BankAccount(acc_no, name, acc_type, balance)

acc.display()

amount = float(input("\nEnter amount to deposit: "))
acc.deposit(amount)

amount = float(input("\nEnter amount to withdraw: "))
acc.withdraw(amount)

acc.display()