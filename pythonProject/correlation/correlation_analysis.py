import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load data from CSV files
file_path1 = '../active_status_per_year.csv'
file_path2 = '../price_per_year.csv'

data_df1 = pd.read_csv(file_path1)
data_df2 = pd.read_csv(file_path2)

# Merge dataframes on 'Year'
merged_df = pd.merge(data_df1, data_df2, on='Year')

# Calculate correlation coefficient
correlation_matrix = merged_df.corr()
corr_coeff = correlation_matrix.loc['Total_Spending', 'Active_Status_Count']
print(f'Correlation coefficient: {corr_coeff:.2f}')

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(merged_df['Total_Spending'], merged_df['Active_Status_Count'])


# Plot scatter plot with linear regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='Total_Spending', y='Active_Status_Count', label='Data Points')
plt.plot(merged_df['Total_Spending'], intercept + slope * merged_df['Total_Spending'], 'r', label=f'Regression: y={intercept:.2f}+{slope:.2f}x')
plt.title(f'Active Rockets from Year vs Total Spending for Year\n\nCorrelation coefficient: {corr_coeff:.2f}')
plt.xlabel('Total Spending for Year')
plt.ylabel('Active Rockets from Year')
plt.legend()
plt.tight_layout()

# Show plot
plt.show()