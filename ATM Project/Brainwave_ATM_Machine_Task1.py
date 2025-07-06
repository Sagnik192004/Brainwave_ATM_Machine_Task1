class ATM:
    def __init__(self):  # Corrected constructor method
        # initializing empty dictionary {pin: amount}
        self.users = {}

    def display_menu(self):
        print("\nWelcome to the ATM:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

    def create_account(self):
        pin = input("Enter your PIN: ")
        if pin in self.users:
            print("Account with this PIN already exists.")
        else:
            balance = float(input("Enter initial balance: "))
            self.users[pin] = balance
            print("Account created successfully.")

    def check_balance(self, pin):
        if pin in self.users:
            print(f"Your balance is: {self.users[pin]}")
        else:
            print("Invalid PIN.")

    def deposit_money(self, pin, amount):
        if pin in self.users:
            self.users[pin] += amount
            print("Deposit successful.")
        else:
            print("Invalid PIN.")

    def withdraw_money(self, pin, amount):
        if pin in self.users:
            if amount <= self.users[pin]:
                self.users[pin] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid PIN.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                pin = input("Enter your PIN: ")
                self.check_balance(pin)
            elif choice == "3":
                pin = input("Enter your PIN: ")
                amount = float(input("Enter deposit amount: "))
                self.deposit_money(pin, amount)
            elif choice == "4":
                pin = input("Enter your PIN: ")
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw_money(pin, amount)
            elif choice == "5":
                print("Exiting the ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage:
atm = ATM()
atm.run()
