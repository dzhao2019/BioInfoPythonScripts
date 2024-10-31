import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
# Load the dataset from CSV file into a DataFrame
# The data contains rainfall information in London for each month across different years
df = pd.read_csv('london_rainfall.csv')
print(df.head(10))  # Display the first 10 rows of the dataset

# Set up a 2x2 subplot figure
grid_fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Draw a scatterplot (1,1)
# Show January Rainfall over years
# Scatterplot of January rainfall across all years, helps to see year-over-year variations
sns.scatterplot(data=df, x='Year', y='January', ax=axes[0, 0])
axes[0, 0].set_title('January Rainfall Over the Years')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('January Rainfall (mm)')

# Filter data for years smaller than or equal to 2000
# Visualizing only the January rainfall for the years before 2000
sns.scatterplot(data=df[df['Year'] <= 2000], x='Year', y='July', ax=axes[0, 1])
axes[0, 1].set_title('July Rainfall (Before 2000)')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('July Rainfall (mm)')

# Convert DataFrame to Long form, which is required for most Seaborn plots
# This allows for comparing rainfall trends for different months
df_melted = pd.melt(df, id_vars=['Year'], var_name='Month', value_name='Rainfall')

# Filter the melted DataFrame to include only rows where 'Month' is January, February, or March
filtered = df_melted[df_melted['Month'].isin(['January', 'February', 'March'])]

# Scatterplot showing rainfall for January, February, and March over the years (2,1)
# Using different colors for each month to visualize differences
sns.scatterplot(data=filtered, x='Year', y='Rainfall', hue='Month', ax=axes[1, 0])
axes[1, 0].set_title('Rainfall in January, February, and March Over the Years')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Rainfall (mm)')
axes[1, 0].legend(title='Month')

# Scatterplot with additional customization (2,2)
# Changing figure size and adding different styles for each month
sns.scatterplot(data=filtered, x='Year', y='Rainfall', hue='Month', style='Month', ax=axes[1, 1])

# Customizing the legend to improve its positioning and readability
axes[1, 1].set_title('Rainfall in January, February, and March (Styled)')
axes[1, 1].set_xlabel('Year')
axes[1, 1].set_ylabel('Rainfall (mm)')
axes[1, 1].legend(title='Month', bbox_to_anchor=(1.25, 0.1), loc='lower right')

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()

