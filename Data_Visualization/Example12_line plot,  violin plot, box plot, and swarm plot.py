import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('london_rainfall.csv')

# Melt the DataFrame
# convert month columns (January - December)
# into a single column named 'Month'
melted_df = pd.melt(df, id_vars=['Year'],
                    var_name='Month',
                    value_name='Rainfall')
print(melted_df)
# Define the dictionary to map each month to its corresponding season
seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season using the seasons dictionary
melted_df['Season'] = melted_df['Month'].map(seasons)

decades = lambda x: (x // 10) * 10
melted_df['Decade'] = melted_df['Year'].apply(decades)

# Set up a 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
sns.set_theme(style="ticks")

# 1. Line plot - Average monthly rainfall over the years
sns.lineplot(data=melted_df.groupby('Year', as_index=False).mean(),
             x='Year', y='Rainfall', ax=axes[0, 0], color='b')
axes[0, 0].set_title('Average Monthly Rainfall')
axes[0, 0].set_ylabel('Average Rainfall (mm)')

# Create custom order and color palette for Seasons
order=['Spring', 'Summer', 'Autumn', 'Winter']
season_palette = {
    'Spring': '#66c2a5',  # Light Green
    'Summer': '#fc8d62',  # Orange
    'Autumn': '#8da0cb',  # Light Blue
    'Winter': '#e78ac3'   # Pink
}
# 2. Violin plot - Rainfall distribution by season
sns.violinplot(data=melted_df, x='Season', y='Rainfall', ax=axes[0, 1],
               palette=season_palette, order=order)
axes[0, 1].set_title('Rainfall Distribution by Season')
axes[0, 1].set_ylabel('Rainfall (mm)')

order_mth = ['January', 'February', 'March', 'April','May', 'June', 'July',
             'August','September','October', 'November','December']
# 3. Box plot - Monthly rainfall distribution across years
sns.boxplot(data=melted_df, x='Month', y='Rainfall', ax=axes[1, 0],
            palette='Set3', order=order_mth)
axes[1, 0].set_title('Monthly Rainfall Distribution')
axes[1, 0].set_ylabel('Rainfall (mm)')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Swarm plot - Total rainfall per year
sns.swarmplot(data=melted_df, x='Decade', y='Rainfall',ax=axes[1, 1],
               hue='Season', hue_order=order, palette=season_palette)
axes[1, 1].set_title('Seasonal Rainfall')
axes[1, 1].set_ylabel('Rainfall (mm)')
axes[1, 1].legend(title='Season', bbox_to_anchor=(1.25, 0.1), loc='lower right')
# Adjust layout and remove spines
sns.despine()

plt.tight_layout()
plt.show()


