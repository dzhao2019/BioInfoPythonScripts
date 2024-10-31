import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
sns.set_style("ticks", {"xtick.major.size": 16, "ytick.major.size": 16})
sns.despine(top=True, right=True)



# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

df_melted = df.melt(id_vars=['Year'], var_name='Month', value_name='Rainfall')

seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season using the seasons dictionary
df_melted['Season'] = df_melted['Month'].map(seasons)

average_yearly_rainfall = df_melted.groupby('Year')['Rainfall'].mean().reset_index()
mean_rainfall = average_yearly_rainfall['Rainfall'].mean()
print(f"Mean value of the average yearly rainfall: {mean_rainfall:.2f} mm")

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 6))

hue_ranking = ['Spring', 'Summer', 'Autumn', 'Winter']
palette = {'Winter': "tab:blue", 'Autumn': "tab:orange",
           'Spring': "tab:green", 'Summer': "tab:red"}
markers = {'Spring':'s' ,'Summer': 'D',
            'Autumn':'X',  'Winter':'o'}
# Scatter plot - rainfall for Jan - Mar
sns.scatterplot(data=df_melted, x='Year', y='Rainfall',
                hue='Season', style='Season',
                hue_order=hue_ranking,markers=markers,
                palette=palette,s=50,legend=True,ax=ax)
sns.lineplot(x=df_melted['Year'], y=504,  linestyle=":",
             label='Mean yearly rainfall', color='b', ax=ax)

sns.despine()
# Set the title and labels for the axis
ax.set_title('Seasonal Rainfall (mm)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Rainfall (mm)', fontsize=12)

# Rotate x-axis labels for better readability
ax.tick_params(axis='x', rotation=45)

# Customize the legend position and format
ax.legend(loc='lower right',
          bbox_to_anchor=(1.2, 0.1))

# Save the figure to a PNG file
fig.savefig('Scatter Plot with a Line Plot_yearly_rainfall_distribution.png',
            dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()


