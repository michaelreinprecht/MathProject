import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../missions_per_organisation.csv'
data_df = pd.read_csv(file_path)

# Sort DataFrame by 'Organisation'
data_df = data_df.sort_values(by='Organisation')

# Define the organizations and values to plot
organizations = data_df['Organisation']
missions = [
    ('Successful_Missions', 'Successful_Missions_Relativ'),
    ('Failed_Missions', 'Failed_Missions_Relativ'),
    ('Total_Missions', 'Total_Missions_Relativ')
]

# Plot each type of mission in separate figures
for mission in missions:
    absolute_value, relative_value = mission

    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    fig.subplots_adjust(hspace=0.5, wspace=0.4)  # Increase vertical spacing between subplots

    # Plot absolute value
    ax = axes[0]
    ax.bar(organizations, data_df[absolute_value], color='skyblue')
    ax.set_title(absolute_value)
    ax.set_xlabel('Organisation')
    ax.set_ylabel('Value')

    # Calculate mean and standard deviation
    mean_val = data_df[absolute_value].mean()
    std_val = data_df[absolute_value].std()

    # Highlight mean and standard deviation
    ax.axhline(y=mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
    ax.axhline(y=mean_val + std_val, color='green', linestyle='--', label=f'Std Dev: {std_val:.2f}')
    ax.axhline(y=mean_val - std_val, color='green', linestyle='--')

    # Add legend
    ax.legend()

    # Rotate x-axis tick labels
    ax.set_xticklabels(organizations, rotation=90)  # Rotate labels by 90 degrees

    # Plot relative value
    ax = axes[1]
    ax.bar(organizations, data_df[relative_value], color='skyblue')
    ax.set_title(relative_value)
    ax.set_xlabel('Organisation')
    ax.set_ylabel('Value')

    # Rotate x-axis tick labels
    ax.set_xticklabels(organizations, rotation=90)  # Rotate labels by 90 degrees

    # Adjust layout
    plt.tight_layout()

    # Show plot
    plt.show()
