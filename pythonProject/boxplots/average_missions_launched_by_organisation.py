import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../missions_per_organisation.csv'
data_df = pd.read_csv(file_path)

# Calculate average total missions, successful missions, and failed missions per organisation
average_total_missions_per_org = data_df.groupby('Organisation')['Total_Missions'].mean()
average_successful_missions_per_org = data_df.groupby('Organisation')['Successful_Missions'].mean()
average_failed_missions_per_org = data_df.groupby('Organisation')['Failed_Missions'].mean()

# Create subplots for each boxplot with increased spacing
fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

# Function to annotate quartiles and whiskers on a boxplot
def annotate_boxplot(boxplot, ax, label):
    quartiles = [
        boxplot['medians'][0].get_xdata()[0],  # Median
        boxplot['boxes'][0].get_xdata()[0],    # Q1
        boxplot['boxes'][0].get_xdata()[2],    # Q3
    ]
    whiskers = [
        boxplot['whiskers'][0].get_xdata()[1], # Min
        boxplot['whiskers'][1].get_xdata()[1]  # Max
    ]

    # Add text field for quartiles and whiskers
    text = f'{label}:\n'
    text += f'Whisker start: {whiskers[0]:.2f}\n'
    text += f'Q1 (25%): {quartiles[1]:.2f}\n'
    text += f'Median (50%): {quartiles[0]:.2f}\n'
    text += f'Q3 (75%): {quartiles[2]:.2f}\n'
    text += f'Whisker end: {whiskers[1]:.2f}\n'

    ax.text(0.90, 0.5, text, verticalalignment='center', horizontalalignment='right',
            transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

# Plot boxplot for average total missions per organisation
boxplot_total = axes[0].boxplot(average_total_missions_per_org, vert=False, widths=0.7)
axes[0].set_xlabel('Average Number of Total Missions per Organisation')
axes[0].set_title('Boxplot of Average Total Missions per Organisation')
annotate_boxplot(boxplot_total, axes[0], 'Total Missions')

# Plot boxplot for average successful missions per organisation
boxplot_successful = axes[1].boxplot(average_successful_missions_per_org, vert=False, widths=0.7)
axes[1].set_xlabel('Average Number of Successful Missions per Organisation')
axes[1].set_title('Boxplot of Average Successful Missions per Organisation')
annotate_boxplot(boxplot_successful, axes[1], 'Successful Missions')

# Plot boxplot for average failed missions per organisation
boxplot_failed = axes[2].boxplot(average_failed_missions_per_org, vert=False, widths=0.7)
axes[2].set_xlabel('Average Number of Failed Missions per Organisation')
axes[2].set_title('Boxplot of Average Failed Missions per Organisation')
annotate_boxplot(boxplot_failed, axes[2], 'Failed Missions')

plt.tight_layout()
plt.show()
