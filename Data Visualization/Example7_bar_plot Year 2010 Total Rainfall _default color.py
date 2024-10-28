import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

melted_df = df.melt(id_vars=['Year'], var_name='Month', value_name='Rainfall')

# Filter the data to include only years greater than 2010
melted_df = melted_df[melted_df['Year'] > 2010]

# Group by 'Year' and calculate the total rainfall
total_rainfall_per_year = melted_df.groupby('Year')['Rainfall'].sum().reset_index()

plt.figure(figsize=(10, 6))
# Create a bar plot - Total rainfall per year
sns.barplot(data=total_rainfall_per_year, x='Year', y='Rainfall')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Total Rainfall (mm)')
plt.title('Total Rainfall per Year (After 2010)')
# Remove the top and right spines for better aesthetics
sns.despine()
plt.tight_layout()
plt.show()




