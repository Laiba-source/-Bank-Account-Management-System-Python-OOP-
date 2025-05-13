class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited {amount}. New balance: {self.__balance}")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn {amount}. Remaining balance: {self.__balance}")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def display_info(self):
        print(f"Account No: {self.__account_number}, Holder: {self.__holder_name}, Balance: {self.__balance}")


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        acc_no = input("Enter account number: ")
        name = input("Enter account holder name: ")
        account = BankAccount(acc_no, name)
        self.accounts.append(account)
        print("🎉 Account created successfully!")

    def find_account(self, acc_no):
        for account in self.accounts:
            if account.get_account_number() == acc_no:
                return account
        return None

    def deposit_money(self):
        acc_no = input("Enter account number: ")
        account = self.find_account(acc_no)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("❌ Account not found.")

    def withdraw_money(self):
        acc_no = input("Enter account number: ")
        account = self.find_account(acc_no)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("❌ Account not found.")

    def check_balance(self):
        acc_no = input("Enter account number: ")
        account = self.find_account(acc_no)
        if account:
            account.display_info()
        else:
            print("❌ Account not found.")
def menu():
    bank = BankSystem()
    while True:
        print("\n=== Bank Account System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            print("🚪 Thank you for using the bank system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
