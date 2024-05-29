import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../active_status_per_year.csv'
data_df = pd.read_csv(file_path)

# Calculate mean and standard deviation for Active_Status_Count
mean_count = data_df['Active_Status_Count'].mean()
std_count = data_df['Active_Status_Count'].std()

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Plot Active_Status_Count
ax1.bar(data_df['Year'], data_df['Active_Status_Count'], color='skyblue')
ax1.set_ylabel('Active Status Count')
ax1.set_title('Active Status Count by Year')
ax1.tick_params(axis='x', rotation=90)

# Highlight mean and standard deviation
ax1.axhline(y=mean_count, color='red', linestyle='--', label=f'Mean: {mean_count:.2f}')
ax1.axhline(y=mean_count + std_count, color='green', linestyle='--', label=f'Std Dev: {std_count:.2f}')
ax1.axhline(y=mean_count - std_count, color='green', linestyle='--')

# Add legend
ax1.legend()

# Plot Active_Status_Relative
ax2.bar(data_df['Year'], data_df['Active_Status_Relative'], color='salmon')
ax2.set_ylabel('Active Status Relative')
ax2.set_title('Active Status Relative by Year')
ax2.tick_params(axis='x', rotation=90)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
