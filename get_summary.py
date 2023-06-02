import pandas as pd
import time
from generate_organe_text import orange_text

def get_summerized_feedback(fiel_path):
    df = pd.read_csv(fiel_path)
    amount_by_category = df.groupby('Category')['Amount'].sum().sort_values(ascending=False).reset_index().rename(columns={'Amount': 'Amount_spend'})
    
    print("Expenses By Category 📈")
    print('\n')
    # Iterate through each category and its sum
    for index, row in amount_by_category.iterrows():
        category = row['Category']
        amount = row['Amount_spend']
        print(f"  {category}:  {amount}")
    
    print('\n')
    total_spend = orange_text(amount_by_category['Amount_spend'].sum().round(2))
    print(f"💵 Total Spent: {total_spend}")
    print(f"You have Spend monstly in the {orange_text(amount_by_category.loc[0, 'Category'])} category.")


def get_summary(file_path):
    print("Loading...", end="", flush=True)
    time.sleep(3)
    print("\r" + " " * len("Loading..."), end="", flush=True)
    print('\n')
    get_summerized_feedback(file_path)