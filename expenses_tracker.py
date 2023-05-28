from expense import Expense
import datetime


def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 5000

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"🎯 Getting user expense.")
    expense_name = input("Enter expense name: ")  # Prompt the user to enter the expense name
    expense_amount = float(input("Enter expense amount: "))  # Prompt the user to enter the expense amount

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
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_category)
            return new_expense  # Return a new Expense object with the user-provided details
        else:
            print("Invalid category. Please try again")  # Display an error message for an invalid category



def save_expense_to_file(expense: Expense, expense_file_path):
    """
    Save the user's expense details to a file.

    Args:
        expense (Expense): An instance of the Expense class representing the expense details.
        expense_file_path (str): The path to the file where the expense will be saved.
    """
    print(f"🎯 Saving user expense: {expense} to {expense_file_path}")

    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expenses(expense_file_path, budget):
    """
    Summarize the user's expenses based on the expense file and budget.

    Args:
        expense_file_path (str): The path to the expense file.
        budget (float): The budget amount.

    """
    print(f"🎯 Summarizing the user expenses.")

    expenses: list[Expense] = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            name, category, amount = line.strip().split(",")
            line_expense = Expense(
                name=name,
                category=category,
                amount=float(amount)
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈")
    for key, amount in amount_by_category.items():
        print(f"  {key}: {amount:.2f}")

    total_spend = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: {total_spend:.2f}")

    remaining_budget = budget - total_spend
    print(f"✅ Budget Remaining: {remaining_budget:.2f}")

    def get_days_remaining():
        """
        Calculate the number of days remaining in the current month.

        Returns:
            int: The number of days remaining.
        """
        now = datetime.datetime.now()
        current_year = now.year
        current_month = now.month
        last_day_of_month = datetime.datetime(
            current_year, current_month, 1) + datetime.timedelta(days=32)
        days_remaining = (last_day_of_month - now).days

        return days_remaining

    days_remaining = get_days_remaining()
    budget_per_day = remaining_budget / days_remaining
    print(f"👉 Budget per day: {budget_per_day:.2f}")



if __name__ == "__main__":
    main()
