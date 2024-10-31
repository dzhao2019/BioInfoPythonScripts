import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('london_rainfall.csv')

# Melt the DataFrame to convert months into a single column
melted_df = pd.melt(df, id_vars=['Year'], var_name='Month', value_name='Rainfall')

# Define the dictionary to map each month to its corresponding season
seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season using the seasons dictionary
melted_df['Season'] = melted_df['Month'].map(seasons)

# Aggregate the data to calculate total rainfall per season per year
seasonal_rainfall = melted_df.groupby(['Year', 'Season'])['Rainfall'].sum().reset_index()

# Pivot the table to have years as rows and seasons as columns
pivot_df = seasonal_rainfall.pivot(index='Year', columns='Season', values='Rainfall')

# Plot a cluster heatmap
sns.set_theme(style="white")
plt.figure(figsize=(10, 8))
sns.clustermap(pivot_df, cmap='coolwarm', standard_scale=1, figsize=(10, 8), linewidths=.5)

plt.title('Cluster Heatmap of Seasonal Rainfall in London')
plt.show()
