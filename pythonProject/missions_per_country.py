import pandas as pd
import re

from tabulate import tabulate

# Load the CSV file
file_path = 'mission_launches.csv'
missions_df = pd.read_csv(file_path)

# Map the mission statuses to 'Successful' and 'Unsuccessful'
missions_df['Mission_Status'] = missions_df['Mission_Status'].replace(
    {'Success': 'Successful', 'Failure': 'Unsuccessful', 'Prelaunch Failure': 'Unsuccessful', 'Partial Failure': 'Unsuccessful'}
)

# Extract country from Location using regular expressions
missions_df['Country'] = missions_df['Location'].str.extract(r',\s*([A-Za-z ]+)$')

# Sort by Country
missions_df = missions_df.sort_values(by='Country')

# Count successful missions per Country
success_counts_per_country = missions_df[missions_df['Mission_Status'] == 'Successful'].groupby('Country').size().reset_index(name='Successful_Missions')

# Count failed missions per Country
failed_counts_per_country = missions_df[missions_df['Mission_Status'] == 'Unsuccessful'].groupby('Country').size().reset_index(name='Failed_Missions')

# Count total missions per Country
total_counts_per_country = missions_df.groupby('Country').size().reset_index(name='Total_Missions')

# Merge counts into one DataFrame
merged_counts = pd.merge(success_counts_per_country, failed_counts_per_country, on='Country', how='outer')
merged_counts = pd.merge(merged_counts, total_counts_per_country, on='Country', how='outer')

# Fill missing values with 0
merged_counts = merged_counts.fillna(0)

# Calculate relative frequencies
total_successful_missions = merged_counts['Successful_Missions'].sum()  # Total count of successful missions
total_failed_missions = merged_counts['Failed_Missions'].sum()  # Total count of failed missions
total_missions = merged_counts['Total_Missions'].sum()  # Total count of missions

merged_counts['Successful_Missions_Relativ'] = merged_counts['Successful_Missions'] / total_successful_missions
merged_counts['Failed_Missions_Relativ'] = merged_counts['Failed_Missions'] / total_failed_missions
merged_counts['Total_Missions_Relativ'] = merged_counts['Total_Missions'] / total_missions

# Calculate mean and standard deviation
mean_successful = merged_counts['Successful_Missions'].mean()
std_successful = merged_counts['Successful_Missions'].std()

mean_failed = merged_counts['Failed_Missions'].mean()
std_failed = merged_counts['Failed_Missions'].std()

mean_total = merged_counts['Total_Missions'].mean()
std_total = merged_counts['Total_Missions'].std()

# Define the output file path
output_file_path = 'missions_per_country.csv'

# Set display format for float numbers
pd.options.display.float_format = '{:,.20f}'.format

# Save the result to a new CSV file
merged_counts.to_csv(output_file_path, index=False)

# Print the result in a nice table format
print(tabulate(merged_counts, headers='keys', tablefmt='psql'))

# Print mean and standard deviation
print("\nMean and Standard Deviation of Missions per Country:")
print(f"Mean Successful Missions: {mean_successful}, Standard Deviation: {std_successful}")
print(f"Mean Failed Missions: {mean_failed}, Standard Deviation: {std_failed}")
print(f"Mean Total Missions: {mean_total}, Standard Deviation: {std_total}")

print(f"File saved to {output_file_path}")
