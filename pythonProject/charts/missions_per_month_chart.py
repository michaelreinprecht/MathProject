import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV file
file_path = '../missions_per_month.csv'  # Adjust the path as needed
data_df = pd.read_csv(file_path)

# Define the years and values to plot
years = data_df['Month']
absolute_values = ['Successful_Missions', 'Failed_Missions', 'Total_Missions']
relative_values = ['Successful_Missions_Relativ', 'Failed_Missions_Relativ', 'Total_Missions_Relativ']

# Create subplots for each value
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
fig.subplots_adjust(hspace=0.5, wspace=0.4)  # Increase vertical spacing between subplots

# Plot absolute values
for i, value in enumerate(absolute_values):
    ax = axes[i, 0]
    ax.bar(years, data_df[value], color='skyblue')
    ax.set_title(value)
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')

    # Calculate mean and standard deviation
    mean_val = data_df[value].mean()
    std_val = data_df[value].std()

    # Highlight mean and standard deviation
    ax.axhline(y=mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
    ax.axhline(y=mean_val + std_val, color='green', linestyle='--', label=f'Std Dev: {std_val:.2f}')
    ax.axhline(y=mean_val - std_val, color='green', linestyle='--')

    # Add legend
    ax.legend()

# Plot relative values
for i, value in enumerate(relative_values):
    ax = axes[i, 1]
    ax.bar(years, data_df[value], color='skyblue')
    ax.set_title(value)
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
