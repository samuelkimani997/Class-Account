class Account:
    def __init__(self, balance=1000):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance + amount
            print(f"Amount {amount} deposited successfully.")
        else:
            print("Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance - amount
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def send(self, amount):
        if amount <= self.balance:
            self.balance - amount
            print(f"Amount {amount} sent successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.balance

bank_account = Account() 
while True:
    print("\nWelcome to Simple Banking System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Send")
    print("4. Check Balance")
    print("5. Exit")
    ("\nWelcome to Simple Banking System")
    choice = input("Please enter your choice: ")

    if choice == "1":
        deposit_amount = float(input("Enter amount to deposit: "))
        bank_account.deposit(deposit_amount)
        print(f"Deposit successful. Your new balance is {bank_account.check_balance()}")

    elif choice == "2":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        bank_account.withdraw(withdraw_amount)
        print(f"Withdrawal successful. Your new balance is {bank_account.check_balance()}")

    elif choice == "3":
        send_amount = float(input("Enter amount to send: "))
        bank_account.send(send_amount)
        print(f"Send successful. Your new balance is {bank_account.check_balance()}")

    elif choice == "4":
        print(f"Your current balance is: {bank_account.check_balance()}")

    elif choice == "5":
        print("Thank you for using Simple Banking System")
        break

    else:
        print("Invalid choice. Please try again.")