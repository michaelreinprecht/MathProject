import pandas as pd
from tabulate import tabulate

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Map the mission statuses to 'Successful' and 'Unsuccessful'
missions_df['Mission_Status'] = missions_df['Mission_Status'].replace(
    {'Success': 'Successful', 'Failure': 'Unsuccessful', 'Prelaunch Failure': 'Unsuccessful', 'Partial Failure': 'Unsuccessful'}
)

# Extract the organisation from Location using regular expressions
missions_df['Organisation'] = missions_df['Organisation'].str.extract(r'([^,]+)')

# Sort by Organisation
missions_df = missions_df.sort_values(by='Organisation')

# Count occurrences of Rocket_Status where it is StatusActive by organisation
active_status_counts_per_org = missions_df[missions_df['Rocket_Status'] == 'StatusActive'].groupby('Organisation').size().reset_index(name='Active_Status_Count')

# Calculate the total count of StatusActive across all organisations
total_active_status = active_status_counts_per_org['Active_Status_Count'].sum()

# Calculate relative frequencies
active_status_counts_per_org['Active_Status_Relative'] = active_status_counts_per_org['Active_Status_Count'] / total_active_status

# Define the output file path
output_file_path = 'active_status_per_organisation.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.20f}'.format

# Save the result to a new CSV file
active_status_counts_per_org.to_csv(output_file_path, index=False)

# Print the result in a nice table format
print(tabulate(active_status_counts_per_org, headers='keys', tablefmt='psql'))

print(f"File saved to {output_file_path}")
