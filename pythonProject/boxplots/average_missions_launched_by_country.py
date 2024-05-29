import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../missions_per_country.csv'
data_df = pd.read_csv(file_path)

# Calculate average total missions, successful missions, and failed missions per organisation
average_total_missions_per_org = data_df.groupby('Country')['Total_Missions'].mean()
average_successful_missions_per_org = data_df.groupby('Country')['Successful_Missions'].mean()
average_failed_missions_per_org = data_df.groupby('Country')['Failed_Missions'].mean()

# Create subplots for each boxplot with increased spacing
fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

# Plot boxplot for average total missions per organisation
axes[0].boxplot(average_total_missions_per_org, vert=False, widths=0.7)
axes[0].set_xlabel('Average Number of Total Missions per Country')
axes[0].set_title('Boxplot of Average Total Missions per Country')

# Plot boxplot for average successful missions per organisation
axes[1].boxplot(average_successful_missions_per_org, vert=False, widths=0.7)
axes[1].set_xlabel('Average Number of Successful Missions per Country')
axes[1].set_title('Boxplot of Average Successful Missions per Country')

# Plot boxplot for average failed missions per organisation
axes[2].boxplot(average_failed_missions_per_org, vert=False, widths=0.7)
axes[2].set_xlabel('Average Number of Failed Missions per Country')
axes[2].set_title('Boxplot of Average Failed Missions per Country')

plt.show()
