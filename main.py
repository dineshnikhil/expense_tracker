from get_user_expense import get_user_expense
from store_expense import store_expense_to_dataframe
from get_summary import get_summary

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
    
    get_summary(file_path)

if __name__ == '__main__':
    main()      
