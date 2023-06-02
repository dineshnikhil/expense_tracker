import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_expenses_graph(file_path):
    df = pd.read_csv(file_path)
    df['Category'] = df['Category'].apply(lambda category: category.split(" ")[1])
    amount_by_category = df.groupby('Category')['Amount'].sum().reset_index().rename(columns={'Amount': 'Amount_spend'}).sort_values('Amount_spend', ascending=False)
    
    # ploting the amount_by_category
    fig = plt.figure()
    ax = sns.barplot(data=amount_by_category, x='Category', y='Amount_spend', color='#FF6969')

    fig.set_facecolor("#A6D0DD")
    ax.set_facecolor("#FFD3B0")

    for p in ax.patches:
        ax.annotate(f"{p.get_height():.1f}", (p.get_x() + p.get_width() / 2, p.get_height()), 
                    ha='center', va='bottom')
    
    
    plt.title("Expenses by Category")  # Set the chart title    
    plt.show()