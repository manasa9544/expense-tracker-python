# Simple Expense Tracker

def add_expense():
    item = input("Enter item name (food/rent/travel): ")
    amount = float(input("Enter amount: "))
    with open("expenses.txt", "a") as f:
        f.write(f"{item} - {amount}\n")
    print("Expense Saved!")

def show_expenses():
    total = 0
    try:
        with open("expenses.txt", "r") as f:
            print("\n--- All Expenses ---")
            for line in f:
                print(line.strip())
                # get amount after -
                amount = float(line.split("-")[1].strip())
                total += amount
        print(f"Total Expense: Rs. {total}")
    except FileNotFoundError:
        print("No expenses yet!")

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Wrong choice!")
