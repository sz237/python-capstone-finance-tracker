# Step 1: Welcome Message
print("Welcome to the Personal Finance Tracker!")

# Step 2: Data structure to store expenses
expenses = {}  # Dictionary: {category: [(description, amount), ...]}


# Step 6: Function to add an expense
def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_str = input("Enter amount: ").strip()
        amount = float(amount_str)
        if amount < 0:
            raise ValueError("Amount must be positive.")

        # Store expense
        if category not in data:
            data[category] = []
        data[category].append((description, amount))

        print("Expense added successfully.")

    except ValueError as e:
        print(f"Invalid input. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Step 3: View all expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded.")
        return

    for category, items in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in items:
            print(f"  - {desc}: ${amt:.2f}")


# Step 4: View summary
def view_summary(data):
    if not data:
        print("No expenses recorded.")
        return

    print("\nSummary:")
    for category, items in data.items():
        total = sum(amount for _, amount in items)
        print(f"{category}: ${total:.2f}")


# Step 6 & 7: Menu loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        view_summary(expenses)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1–4.")
