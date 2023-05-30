import pandas as pd
import time

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


def get_summary(file_path):
    print("Loading...", end="", flush=True)
    time.sleep(3)
    print("\r" + " " * len("Loading..."), end="", flush=True)
    print('\n')
    get_summerized_feedback(file_path)