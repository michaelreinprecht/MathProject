import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../missions_per_year.csv'
data_df = pd.read_csv(file_path)

# Calculate average total missions, successful missions, and failed missions per year
average_total_missions_per_year = data_df.groupby('Year')['Total_Missions'].mean()
average_successful_missions_per_year = data_df.groupby('Year')['Successful_Missions'].mean()
average_failed_missions_per_year = data_df.groupby('Year')['Failed_Missions'].mean()

# Create subplots for each boxplot with increased spacing
fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

# Function to annotate quartiles and whiskers on a boxplot
def annotate_boxplot(boxplot, ax):
    quartiles = [
        boxplot['medians'][0].get_xdata()[0],  # Median
        boxplot['boxes'][0].get_xdata()[0],    # Q1
        boxplot['boxes'][0].get_xdata()[2],    # Q3
    ]
    whiskers = [
        boxplot['whiskers'][0].get_xdata()[1], # Min
        boxplot['whiskers'][1].get_xdata()[1]  # Max
    ]

    # Add annotations for the quartiles
    positions = [1.2, 1.0, 1.4]  # Different y-positions for quartiles to avoid overlap
    for pos, value in zip(positions, quartiles):
        ax.annotate(f'{value:.2f}', xy=(value, 1), xytext=(value, pos),
                    textcoords='data', ha='center', va='bottom', fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

    # Add annotations for the whiskers
    positions = [0.9, 0.9]  # Different y-positions for whiskers to avoid overlap
    for pos, value in zip(positions, whiskers):
        ax.annotate(f'{value:.2f}', xy=(value, 1), xytext=(value, pos),
                    textcoords='data', ha='center', va='top', fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

# Plot boxplot for average total missions per year
boxplot_total = axes[0].boxplot(average_total_missions_per_year, vert=False, widths=0.7)
axes[0].set_xlabel('Average Number of Total Missions per Year')
axes[0].set_title('Boxplot of Average Total Missions per Year')
annotate_boxplot(boxplot_total, axes[0])

# Plot boxplot for average successful missions per year
boxplot_successful = axes[1].boxplot(average_successful_missions_per_year, vert=False, widths=0.7)
axes[1].set_xlabel('Average Number of Successful Missions per Year')
axes[1].set_title('Boxplot of Average Successful Missions per Year')
annotate_boxplot(boxplot_successful, axes[1])

# Plot boxplot for average failed missions per year
boxplot_failed = axes[2].boxplot(average_failed_missions_per_year, vert=False, widths=0.7)
axes[2].set_xlabel('Average Number of Failed Missions per Year')
axes[2].set_title('Boxplot of Average Failed Missions per Year')
annotate_boxplot(boxplot_failed, axes[2])

plt.tight_layout()
plt.show()
