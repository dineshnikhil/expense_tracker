from get_user_expense import get_user_expense
from store_expense import store_expense_to_dataframe
from get_summary import get_summary
from get_ur_expense_graph import get_expenses_graph

def main() -> None:
    
    file_path = 'data/demo.csv'
    
    # Entering in to the loop of the user input.
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
    
    # Giving the Over all summearay of the user expendeture.
    get_summary(file_path)
    
    show_graph_flag = input("Where you want a pictorial presentation of the summary (Y / N ): ")
    if ( show_graph_flag == 'y'):
        get_expenses_graph(file_path)
        print("hope you like the graph..Thank you for using the application")
    else:
        print("Thanky you for using this application.")
    
    

if __name__ == '__main__':
    main()      
