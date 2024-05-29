import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
input_file = 'mission_launches.csv'  # Replace with your input file path
df = pd.read_csv(input_file)

# Replace empty strings or missing values in the Price column with 0.0
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)

# Group by the organisation and sum the Price
grouped_df = df.groupby('Organisation', as_index=False)['Price'].sum()

# Rename the Price column to Total_Spending
grouped_df = grouped_df.rename(columns={'Price': 'Total_Spending'})

# Calculate the total spending across all organisations
total_spending = grouped_df['Total_Spending'].sum()

# Add a column for the proportion of total spending
grouped_df['Spending_Relative'] = grouped_df['Total_Spending'] / total_spending

# Calculate mean and standard deviation
mean_spending = round(grouped_df['Total_Spending'].mean(), 4)
std_spending = round(grouped_df['Total_Spending'].std(), 4)

# Define the output file path
output_file = 'price_per_organisation.csv'  # Replace with your desired output file path

# Set display format for float numbers
pd.options.display.float_format = '{:,.4f}'.format

# Save the result to a new CSV file
grouped_df.to_csv(output_file, index=False)

# Print the result in a nice table format
print(grouped_df.to_string(index=False))

# Plot the total spending per organisation
plt.figure(figsize=(12, 8))
plt.bar(grouped_df['Organisation'], grouped_df['Total_Spending'], color='skyblue')

# Highlight mean and standard deviation
plt.axhline(mean_spending, color='red', linestyle='--', label=f'Mean: {mean_spending}')
plt.axhline(mean_spending + std_spending, color='green', linestyle='--', label=f'Standard Deviation: {std_spending}')
plt.axhline(mean_spending - std_spending, color='green', linestyle='--')

plt.xlabel('Organisation')
plt.ylabel('Total Spending')
plt.title('Total Spending per Organisation')
plt.xticks(rotation=90)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

print("\nThe output has been saved to", output_file)
