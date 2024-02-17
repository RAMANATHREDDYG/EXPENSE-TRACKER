from datetime import datetime
from collections import defaultdict

# Dictionary to store expenses, with categories as keys
expenses = defaultdict(list)


# Function to add an expense to the expenses dictionary
def add_expense(category, amount, description, date):
    expenses[category].append({"amount": amount, "description": description, "date": date})


# Function to get the total expenses and monthly expenses summary
def get_monthly_summary(month, year):
    total_expenses = 0
    monthly_expenses = defaultdict(int)

    # Iterate over each category and its corresponding entries
    for category, entry in expenses.items():
        # Iterate over each entry in the category
        for item in entry:
            entry_date = datetime.strptime(item['date'], "%Y-%m-%d")
            # Check if the entry date matches the specified month and year
            if entry_date.month == month and entry_date.year == year:
                # Increment the monthly expense for the category
                monthly_expenses[category] += item['amount']
                # Increment the total expenses
                total_expenses += item['amount']

    return total_expenses, monthly_expenses


# Function to print the main menu
def print_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add My Expense")
    print("2. View My Monthly Expenses Summary")
    print("3. Exit")


# Function to add an expense via user input
def add_expense_menu():
    # Get input for expense details
    category = input("\nEnter expense category (e.g., food, transportation, entertainment): ")
    amount = 0
    while True:
        try:
            amount = float(input("Enter amount spent: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    description = input("Enter a brief description about that expense: ")
    date = datetime.now().strftime("%Y-%m-%d")

    # Add the expense to the expenses dictionary
    add_expense(category, amount, description, date)
    print("\n**********Expense added successfully!***************")


# Function to view monthly expenses summary
def view_expenses_menu():
    while True:
        try:
            month = int(input("\nEnter month (1-12): "))
            year = int(input("Enter year: "))
            if 1 <= month <= 12 and year >= 0:
                break
            else:
                print("Invalid month or year. Please enter valid values.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Get monthly summary and display it
    total_expenses, monthly_expenses = get_monthly_summary(month, year)
    print("\nMonthly Summary for {}/{}:".format(month, year))
    print("Total expenses: RS {:.2f}/-".format(total_expenses))
    if total_expenses:
        print("The categories in which you spend your expenses.\n")
        for category, amount in monthly_expenses.items():
            print("{}: RS {:.2f}/-".format(category, amount))


# Main program loop
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense_menu()

    elif choice == '2':
        view_expenses_menu()

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
