
from datetime import date


def add_expense():
    """Collect and validate a new expense."""
    try:
        amount_text = input("Enter amount (Rs.): ").strip()
        amount = float(amount_text)

        if not amount_text or amount <= 0:
            print("Error: Amount must be greater than zero.")
            return None

        if not amount < float("inf"):
            print("Error: Enter a valid, finite amount.")
            return None

        category = input("Enter category: ").strip()
        if not category:
            print("Error: Category cannot be empty.")
            return None

        description = input("Enter description: ").strip()
        if not description:
            print("Error: Description cannot be empty.")
            return None

        return {
            "date": date.today().isoformat(),
            "amount": round(amount, 2),
            "category": category,
            "description": description,
        }

    except ValueError:
        print("Error: Please enter a valid number for the amount.")
        return None


def view_expenses(expenses):
    """Display all saved expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== YOUR EXPENSES =====")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['date']} | "
            f"Rs. {expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def calculate_total(expenses):
    """Calculate the sum of all expense amounts."""
    return sum(expense["amount"] for expense in expenses)
