import pandas as pd
from tabulate import tabulate

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Extract year from date
missions_df['Year'] = missions_df['Date'].str.extract(r'(\d{4})')

# Count occurrences of Rocket_Status where it is StatusActive by year
active_status_counts_per_year = missions_df[missions_df['Rocket_Status'] == 'StatusActive'].groupby('Year').size().reset_index(name='Active_Status_Count')

# Calculate the total count of StatusActive across all countries
total_active_status = active_status_counts_per_year['Active_Status_Count'].sum()

# Calculate relative frequencies
active_status_counts_per_year['Active_Status_Relative'] = active_status_counts_per_year['Active_Status_Count'] / total_active_status

# Define the output file path
output_file_path = 'active_status_per_year.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.20f}'.format

# Save the result to a new CSV file
active_status_counts_per_year.to_csv(output_file_path, index=False)

# Print the result in a nice table format
print(tabulate(active_status_counts_per_year, headers='keys', tablefmt='psql'))

print(f"File saved to {output_file_path}")
