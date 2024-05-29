import pandas as pd
import re
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Extract country from Location using regular expressions
missions_df['Country'] = missions_df['Location'].str.extract(r',\s*([A-Za-z ]+)$')

# Replace empty strings or missing values in the Price column with 0.0
missions_df['Price'] = pd.to_numeric(missions_df['Price'], errors='coerce').fillna(0)

# Group by the country and sum the Price
spending_per_country = missions_df.groupby('Country', as_index=False)['Price'].sum().rename(columns={'Price': 'Total_Spending'})

# Calculate the total spending across all countries
total_spending = spending_per_country['Total_Spending'].sum()

# Add a column for the proportion of total spending
spending_per_country['Spending_Relative'] = spending_per_country['Total_Spending'] / total_spending

# Calculate mean and standard deviation
mean_spending = round(spending_per_country['Total_Spending'].mean(), 4)
std_spending = round(spending_per_country['Total_Spending'].std(), 4)

# Define the output file path
output_file_path = 'price_per_country.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.4f}'.format

# Save the result to a new CSV file
spending_per_country.to_csv(output_file_path, index=False)

# Plot the total spending per country
plt.figure(figsize=(12, 8))
plt.bar(spending_per_country['Country'], spending_per_country['Total_Spending'], color='skyblue')

# Highlight mean and standard deviation
plt.axhline(mean_spending, color='red', linestyle='--', label=f'Mean: {mean_spending}')
plt.axhline(mean_spending + std_spending, color='green', linestyle='--', label=f'Standard Deviation: {std_spending}')
plt.axhline(mean_spending - std_spending, color='green', linestyle='--')

plt.xlabel('Country')
plt.ylabel('Total Spending')
plt.title('Total Spending per Country')
plt.xticks(rotation=90)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

print(f"\nFile saved to {output_file_path}")
