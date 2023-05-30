import pandas as pd
import os

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