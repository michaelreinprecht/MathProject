import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = '../price_per_year.csv'
data_df = pd.read_csv(file_path)

# Calculate average total spending per year
average_total_spending_per_year = data_df.groupby('Year')['Total_Spending'].mean()

# Create subplots for each boxplot with increased spacing
fig, axes = plt.subplots(1, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

# Plot boxplot for average total spending per year
boxplot = axes.boxplot(average_total_spending_per_year, vert=False, widths=0.7)

# Annotate quartiles and whiskers
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
positions = [1.2, 1.1, 1.3]  # Different y-positions for quartiles to avoid overlap
for pos, value in zip(positions, quartiles):
    axes.annotate(f'{value:.2f}', xy=(value, 1), xytext=(value, pos),
                  textcoords='data', ha='center', va='bottom', fontsize=10,
                  bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

# Add annotations for the whiskers
positions = [0.9, 0.9]  # Different y-positions for whiskers to avoid overlap
for pos, value in zip(positions, whiskers):
    axes.annotate(f'{value:.2f}', xy=(value, 1), xytext=(value, pos),
                  textcoords='data', ha='center', va='top', fontsize=10,
                  bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

axes.set_xlabel('Average Total Spending per Year')
axes.set_title('Boxplot of Average Total Spending per Year')

plt.show()
