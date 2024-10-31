import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
# Load the dataset from CSV file into a DataFrame
# The data contains rainfall information in London for each month across different years
df = pd.read_csv('london_rainfall.csv')
print(df.head(10))  # Display the first 10 rows of the dataset

#==============================================
# Draw a scatterplot
# Show January Rainfall over years
# Scatterplot of January rainfall across all years, helps to see year-over-year variations
# output: Example1_scatter_plot_January All year.png
sns.scatterplot(data=df, x='Year', y='January')
plt.title('January Rainfall Over the Years')
plt.xlabel('Year')
plt.ylabel('January Rainfall (mm)')
plt.show()

#==============================================
# Filter data for years smaller than or equal to 2000
# Visualizing only the January rainfall for the years before 2000
# output: Example1_scatter_plot_July before 2000.png
sns.scatterplot(data=df[df['Year'] <= 2000], x='Year', y='July')
plt.title('July Rainfall (Before 2000)')
plt.xlabel('Year')
plt.ylabel('July Rainfall (mm)')
plt.show()

#==============================================
# Example of filtering the melted DataFrame to include specific months
# This allows for comparing rainfall trends for different months
df_melted = pd.melt(df, id_vars=['Year'], var_name='Month', value_name='Rainfall')

# Filter the melted DataFrame to include only rows where 'Month' is January, February, or March
filtered = df_melted[df_melted['Month'].isin(['January', 'February', 'March'])]

# Scatterplot showing rainfall for January, February, and March over the years
# Using different colors for each month to visualize differences
# output: Example1_scatter_plot_Jan Feb Mar.png
sns.scatterplot(data=filtered, x='Year', y='Rainfall', hue='Month')
plt.title('Rainfall in January, February, and March Over the Years')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.legend(title='Month')
plt.show()

#==============================================
# Scatterplot with additional customization
# Changing figure size and adding different styles for each month
# output: Example1_scatter_plot_Jan Feb Mar_style.png
plt.figure(figsize=(9, 5))  # Set the figure size
sns.scatterplot(data=filtered, x='Year', y='Rainfall', hue='Month', style='Month')

# Customizing the legend to improve its positioning and readability
plt.title('Rainfall in January, February, and March (Styled)')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.legend(title='Month', bbox_to_anchor=(1.25, 0.1), loc='lower right')
plt.show()
