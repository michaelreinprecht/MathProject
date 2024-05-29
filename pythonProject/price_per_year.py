import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Extract year from date column using regular expressions
missions_df['Year'] = missions_df['Date'].str.extract(r'(\d{4})')

# Replace empty strings or missing values in the Price column with 0.0
missions_df['Price'] = pd.to_numeric(missions_df['Price'], errors='coerce').fillna(0)

# Calculate total spending per year
spending_per_year = missions_df.groupby('Year', as_index=False)['Price'].sum().rename(columns={'Price': 'Total_Spending'})

# Calculate the total spending across all years
total_spending = spending_per_year['Total_Spending'].sum()

# Add a column for the proportion of total spending
spending_per_year['Spending_Relative'] = spending_per_year['Total_Spending'] / total_spending

# Calculate mean and standard deviation
mean_spending = round(spending_per_year['Total_Spending'].mean(), 4)
std_spending = round(spending_per_year['Total_Spending'].std(), 4)

# Define the output file path
output_file_path = 'price_per_year.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.4f}'.format

# Save the result to a new CSV file
spending_per_year.to_csv(output_file_path, index=False)

# Print the result in a nice table format
print(spending_per_year.to_string(index=False))

# Plot the total spending per year
plt.figure(figsize=(12, 8))
plt.bar(spending_per_year['Year'], spending_per_year['Total_Spending'], color='skyblue')

# Highlight mean and standard deviation
plt.axhline(mean_spending, color='red', linestyle='--', label=f'Mean: {mean_spending}')
plt.axhline(mean_spending + std_spending, color='green', linestyle='--', label=f'Standard Deviation: {std_spending}')
plt.axhline(mean_spending - std_spending, color='green', linestyle='--')

plt.xlabel('Year')
plt.ylabel('Total Spending')
plt.title('Total Spending per Year')
plt.xticks(rotation=90)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

print(f"\nFile saved to {output_file_path}")
