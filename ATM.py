
class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} successfully. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawn {amount} successfully. Current balance: {self.balance}"

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Current Balance:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
