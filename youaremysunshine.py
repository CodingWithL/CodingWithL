class Expense:
    def __init__(self, d, a):
        self.d = d
        self.a = a

    def __str__(self):
        return f"{self.d}: ${self.a:.2f}"

def add_expense(expenses):
    try:
        d, a = input("Enter expense description: "), float(input("Enter expense amount: "))
        if a <= 0: raise ValueError
        expenses.append(Expense(d, a))
        print("Expense added.")
    except: print("Invalid input.")

def display_expenses(expenses):
    print("List of expenses:", *[f"{e.d}: ${e.a:.2f}" for e in expenses], sep="\n" if expenses else "\nNo expenses added.")

def calculate_total(expenses):
    total = sum(e.a for e in expenses)
    print(f"Total expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        print("\n1. Add Expense\n2. Display Expenses\n3. Calculate Total Expenses\n4. Quit")
        c = input("Enter your choice: ")
        if c == "1": add_expense(expenses)
        elif c == "2": display_expenses(expenses)
        elif c == "3": calculate_total(expenses)
        elif c == "4": print("Exiting."); break
        else: print("Invalid choice.")

if __name__ == "__main__": main()