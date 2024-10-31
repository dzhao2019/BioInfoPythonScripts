import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')



# Melt the DataFrame to convert from wide format to long format
df_melted = df.melt(id_vars=['Year'], var_name='Month', value_name='Rainfall')

# Define the dictionary to map each month to its corresponding season
seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season
# using the seasons dictionary
df_melted['Season'] = df_melted['Month'].map(seasons)


decades = lambda x: (x // 10) * 10
df_melted['Decade'] = df_melted['Year'].apply(decades)

# Draw a nested violinplot
sns.violinplot(data=df_melted, x='Decade',
               y='Rainfall', hue='Season',
               split=True, inner='quart',
               hue_order=['Summer','Winter'])

plt.legend(title='Decade', bbox_to_anchor=(1.20, 0.1),
           loc='lower right')


# Remove the top and right spines for better aesthetics
sns.despine()
plt.title('Rainfall Distribution in London (Summer vs Winter)')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')

plt.tight_layout()
plt.show()

# Example5_violin_plot Summer & Winter in decades.png