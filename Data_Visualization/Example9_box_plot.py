import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')
# Filter the data to include only years 1960-1969

melted_df = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')

plt.figure(figsize=(12, 6))
# Box plot - Monthly rainfall distribution across years
sns.boxplot(data=melted_df,
            x='Month', y='Rainfall',
            palette='Set3',
            order=['January', 'February', 'March', 'April',
                   'May', 'June', 'July', 'August',
                   'September', 'October', 'November','December'])

plt.tick_params(axis='x', rotation=45)

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Distribution')


sns.despine()
plt.show()




