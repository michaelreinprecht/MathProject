import pandas as pd
from tabulate import tabulate

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Map the mission statuses to 'Successful' and 'Unsuccessful'
missions_df['Mission_Status'] = missions_df['Mission_Status'].replace(
    {'Success': 'Successful', 'Failure': 'Unsuccessful', 'Prelaunch Failure': 'Unsuccessful', 'Partial Failure': 'Unsuccessful'}
)

# Extract month from Date using fixed positions
missions_df['Month'] = missions_df['Date'].str[4:7]

# Define a dictionary to map month abbreviations to their respective order
month_order = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

# Sort by Month
missions_df['Month'] = missions_df['Month'].map(month_order)
missions_df = missions_df.sort_values(by='Month')

# Convert month numbers back to abbreviations
missions_df['Month'] = missions_df['Month'].map({v: k for k, v in month_order.items()})

# Count successful missions per Month
success_counts_per_month = missions_df[missions_df['Mission_Status'] == 'Successful'].groupby('Month').size().reset_index(name='Successful_Missions')

# Count failed missions per Month
failed_counts_per_month = missions_df[missions_df['Mission_Status'] == 'Unsuccessful'].groupby('Month').size().reset_index(name='Failed_Missions')

# Count total missions per Month
total_counts_per_month = missions_df.groupby('Month').size().reset_index(name='Total_Missions')

# Merge counts into one DataFrame
merged_counts = pd.merge(success_counts_per_month, failed_counts_per_month, on='Month', how='outer')
merged_counts = pd.merge(merged_counts, total_counts_per_month, on='Month', how='outer')

# Fill missing values with 0
merged_counts = merged_counts.fillna(0)

# Calculate relative frequencies
total_successful_missions = merged_counts['Successful_Missions'].sum()  # Total count of successful missions
total_failed_missions = merged_counts['Failed_Missions'].sum()  # Total count of failed missions
total_missions = merged_counts['Total_Missions'].sum()  # Total count of missions

merged_counts['Successful_Missions_Relativ'] = merged_counts['Successful_Missions'] / total_successful_missions
merged_counts['Failed_Missions_Relativ'] = merged_counts['Failed_Missions'] / total_failed_missions
merged_counts['Total_Missions_Relativ'] = merged_counts['Total_Missions'] / total_missions

# Define the output file path
output_file_path = 'missions_per_month.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.20f}'.format

# Save the result to a new CSV file
merged_counts.to_csv(output_file_path, index=False)

# Print the result in a nice table format
print(tabulate(merged_counts, headers='keys', tablefmt='psql'))

print(f"File saved to {output_file_path}")
