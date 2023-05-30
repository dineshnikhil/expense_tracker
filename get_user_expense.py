from datetime import date

def get_user_expense():
    print("🎯 Getting user expense.")
    expense_name = input("Enter expense name: ")  # Prompt the user to enter the expense name
    expense_amount = float(input("Enter expense amount: "))  # Prompt the user to enter the expense amount
    today = date.today()

    expense_categories = [
        "🥘 Food",
        "🏠 Home",
        "🛠️ Work",
        "🎉 Fun",
        "💫 Misc"
    ]  # List of available expense categories

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")  # Display the category options to the user

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1  # Prompt the user to enter a category number

        if selected_index in range(len(expense_categories)):  # Check if the selected index is within the valid range
            selected_category = expense_categories[selected_index]  # Get the selected category
            new_expense = {"Date": today, "Name": expense_name, "Category": selected_category, "Amount": expense_amount}
            print(f"👉 You have spent {expense_amount} on {expense_name} which comes under {selected_category} category.")
            return new_expense  # Return a new Expense object with the user-provided details
        else:
            print("Invalid category. Please try again")  # Display an error message for an invalid category