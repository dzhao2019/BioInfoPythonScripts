import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')
# Filter the data to include only years 1960-1969

df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')

plt.figure(figsize=(12, 8))
# Box plot - Monthly rainfall distribution
sns.boxplot(data=df_melted,
            x='Month', y='Rainfall')
# Rotate x-axis labels
plt.tick_params(axis='x', rotation=45)

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Distribution')

sns.despine()
plt.show()
# Example4_box_plot monthly default color

# ===================================

plt.figure(figsize=(12, 8))
# Violin plot - Monthly rainfall distribution
sns.violinplot(data=df_melted,
            x='Month', y='Rainfall')
# Rotate x-axis labels
plt.tick_params(axis='x', rotation=45)
# Add labels and title
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Distribution')

sns.despine()
plt.show()

#Example4_violin_plot monthly default color.png


