#Expense Tracker project
expense = []
print("Welcome to the Expense Tracker!")
while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        description = input("Enter a description for the expense: ")
        amount = float(input("Enter the amount: "))
        expense.append({'date': date, 'category': category, 'description': description, 'amount': amount})
        print("Expense added successfully!")

    elif choice == 2:
        if (len(expense) == 0):
            print("No expenses recorded.")
        else:
            print("The recorded expenses are:")
            count = 1
            for exp in expense:
                print(f"{count}. Date: {exp['date']}, Category: {exp['category']}, Description: {exp['description']}, Amount: ₹{exp['amount']:.2f}")
                count += 1

    elif choice == 3:
        total = 0
        for exp in expense:
            total += exp['amount']
        print(f"Total Expenses: ₹{total:.2f}")
    elif choice == 4:
        print("Exiting the Expense Tracker. Goodbye!")
        break