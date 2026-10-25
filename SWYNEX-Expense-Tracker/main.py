
import json
from pathlib import Path
from expense_utils import add_expense, view_expenses, calculate_total

DATA_FILE = Path("expenses.json")


def load_expenses():
    """Load saved expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expense data must be a list.")

        return data

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Error loading expenses: {error}")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True

    except OSError as error:
        print(f"Error saving expenses: {error}")
        return False


def main():
    expenses = load_expenses()

    while True:
        print("\n===== SWYNEX EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            expense = add_expense()

            if expense is not None:
                expenses.append(expense)

                if save_expenses(expenses):
                    print("Expense added successfully!")
                else:
                    expenses.pop()
                    print("Expense was not saved.")

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print(f"Total expenses: Rs. {calculate_total(expenses):.2f}")

        elif choice == "4":
            print("Thank you for using SWYNEX Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
