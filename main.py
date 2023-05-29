import os
import pandas as pd
from datetime import date

def main() -> None:
    
    file_path = 'data/demo.csv'
    
    while True:
        # Getting the user input
        expense = get_user_expense()
        # Storing the expense in the dataframe
        store_expense_to_dataframe(expense, file_path)
        # asking user wheather they want to continue or no
        continue_flag = input("🧾 Do you one more expense to add (yes(y)/no(n)): ")
        if continue_flag == 'y':
            continue
        else:
            break
         
    get_summerized_feedback(file_path)    

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
            
      

def store_expense_to_dataframe(expense, file_path):
    
    if(os.stat(file_path).st_size == 0):
        new_dectionary = {"Date": [expense['Date']], "Name": [expense['Name']], "Category": [expense['Category']], "Amount": [expense['Amount']]}
        df = pd.DataFrame(new_dectionary)
        df.to_csv(file_path, index=False)
        print("✔️ Expense has been successfully added..!")
    else:
        df = pd.read_csv(file_path)
        df.loc[len(df)] = expense
        df.to_csv(file_path, index=False)
        print("✔️ Expense has been successfully added..!")
        

def get_summerized_feedback(fiel_path):
    df = pd.read_csv(fiel_path)
    amount_by_category = df.groupby('Category')['Amount'].sum().reset_index().rename(columns={'Amount': 'Amount_spend'}).sort_values('Amount_spend', ascending=False)
    
    print("Expenses By Category 📈")
    # Iterate through each category and its sum
    for index, row in amount_by_category.iterrows():
        category = row['Category']
        amount = row['Amount_spend']
        print(f"  {category}:  {amount}")
    
    total_spend = amount_by_category['Amount_spend'].sum()
    print(f"💵 Total Spent: {total_spend:.2f}")   
    
    
        
main()