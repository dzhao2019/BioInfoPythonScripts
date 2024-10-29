import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')



# Melt the DataFrame to convert from wide format to long format
melted_df = df.melt(id_vars=['Year'], var_name='Month', value_name='Rainfall')

# Define the dictionary to map each month to its corresponding season
seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season
# using the seasons dictionary
melted_df['Season'] = melted_df['Month'].map(seasons)

# Filter rows for years greater than 2015

# Filter rows where 'Season' is either 'Summer' or 'Winter'
melted_df = melted_df[(melted_df['Season'] == 'Summer')
                      | (melted_df['Season'] == 'Winter')]

# Create a violin plot - Rainfall by Year, grouped by Season
plt.figure(figsize=(8, 5))
#sns.violinplot(data=melted_df, x='Year', y='Rainfall', hue='Season', palette='muted')

decades = lambda x: (x // 10) * 10
melted_df['Decade'] = melted_df['Year'].apply(decades)

# Draw a nested violinplot
sns.violinplot(data=melted_df, x='Decade',
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

