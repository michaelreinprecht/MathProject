import pandas as pd
from tabulate import tabulate

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Extract country from Location using regular expressions
missions_df['Country'] = missions_df['Location'].str.extract(r',\s*([A-Za-z ]+)$')

# Count occurrences of Rocket_Status where it is StatusActive by country
active_status_counts_per_country = missions_df[missions_df['Rocket_Status'] == 'StatusActive'].groupby('Country').size().reset_index(name='Active_Status_Count')

# Calculate the total count of StatusActive across all countries
total_active_status = active_status_counts_per_country['Active_Status_Count'].sum()

# Calculate relative frequencies
active_status_counts_per_country['Active_Status_Relative'] = active_status_counts_per_country['Active_Status_Count'] / total_active_status

# Define the output file path
output_file_path = 'active_status_per_country.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.20f}'.format

# Save the result to a new CSV file
active_status_counts_per_country.to_csv(output_file_path, index=False)

# Print the result in a nice table format
print(tabulate(active_status_counts_per_country, headers='keys', tablefmt='psql'))

print(f"File saved to {output_file_path}")
