import pandas as pd
import matplotlib.pyplot as plt

# Create a dummy DataFrame
data = {
    'Category': ['A', 'B', 'C'],
    'Value': [10, 20, 30]
}

df_grouped = pd.DataFrame(data)

# Extract data for plotting
categories = df_grouped['Category']
values = df_grouped['Value']

# Create a bar plot
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Sum')
plt.title('Sum by Category')

# Display the plot
plt.show()