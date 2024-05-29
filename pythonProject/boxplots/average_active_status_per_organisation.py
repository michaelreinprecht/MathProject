import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../active_status_per_organisation.csv'
data_df = pd.read_csv(file_path)

# Calculate average total missions, successful missions, and failed missions per year
average_total_missions_per_organisation = data_df.groupby('Organisation')['Active_Status_Count'].mean()

# Create subplots for each boxplot with increased spacing
fig, axes = plt.subplots(1, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

# Plot boxplot for average total missions per year
axes.boxplot(average_total_missions_per_organisation, vert=False, widths=0.7)
axes.set_xlabel('Average Number of Rockets still active per Organisation')
axes.set_title('Boxplot of Average Rockets still active per Organisation')

plt.show()
