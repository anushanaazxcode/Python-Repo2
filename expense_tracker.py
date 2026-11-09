import csv
from datetime import datetime

expenses = []


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except ValueError:
        return False


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format.")
        return

    category = input("Enter category: ").strip()

    amount = input("Enter amount: ")
    if not validate_amount(amount):
        print("Invalid amount.")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": float(amount)
    }

    expenses.append(expense)
    print("Expense added successfully.")


def save_to_csv(filename="expenses.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses saved to {filename}")


def total_by_category():
    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("
Spending by Category:")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")


def main():
    while True:
        print("
Expense Tracker")
        print("1. Add Expense")
        print("2. View Totals")
        print("3. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            total_by_category()
        elif choice == "3":
            save_to_csv()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
