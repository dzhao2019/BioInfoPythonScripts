import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')
# Filter the data to include only years 1960-1969
df = df[0:10]

df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')

# Group by 'Year' and calculate the total rainfall
total = df_melted.groupby('Year')['Rainfall'].sum().reset_index()

# Create a bar plot - Total rainfall per year
sns.barplot(data=total, x='Year', y='Rainfall')

# Add labels and title
plt.ylabel('Total Rainfall (mm)')
plt.title('Total Rainfall per Year (1960-1969)')

plt.show()
# Example3_bar_plot Total Rainfall per Year (1960-1969).png
#============================

df = pd.read_csv('london_rainfall.csv')
df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')
# Filter the data to include only years since 2010
df_melted = df_melted[df_melted['Year']>2010]
# Create a bar plot - Average rainfall per year
sns.barplot(data=df_melted, x='Year', y='Rainfall')
plt.show()

# Example3_bar_plot Average rainfall per year since 2010.png

