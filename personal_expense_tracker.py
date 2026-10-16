
import csv
import os

FILE_NAME = "expenses.csv"
print("=== Personal Expense Tracker ===")
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            with open(FILE_NAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date, category, description, amount])
            print("Expense saved successfully!")
        except ValueError:
            print("Please enter a valid amount.")
    elif choice == "2":
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid option. Try again.")
