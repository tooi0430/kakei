class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expense = 0

    def record_income(self, amount):
        if amount > 0:
            self.income += amount
            print(f"Income of {amount} recorded.")
        else:
            print("Income amount must be positive.")

    def record_expense(self, amount):
        if amount > 0:
            self.expense += amount
            print(f"Expense of {amount} recorded.")
        else:
            print("Expense amount must be positive.")

    def show_balance(self):
        balance = self.income - self.expense
        print(f"Total Income: {self.income}")
        print(f"Total Expense: {self.expense}")
        print(f"Current Balance: {balance}")

def main():
    budget = BudgetTracker()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Record Income")
        print("2. Record Expense")
        print("3. Show Balance")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            budget.record_income(amount)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            budget.record_expense(amount)
        elif choice == '3':
            budget.show_balance()
        elif choice == '4':
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
