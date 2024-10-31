import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')
seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season using the seasons dictionary
df_melted['Season'] = df_melted['Month'].map(seasons)

# Set up the matplotlib figure
plt.figure(figsize=(8, 6))

# Violin plot
sns.violinplot(data=df_melted,
               x='Season', y='Rainfall',
               color='skyblue', inner=None,
               fill=False)
# Swarm plot
sns.swarmplot(data=df_melted,
              x='Season', y='Rainfall',
              color='grey', size=4)

# Adding titles and labels
plt.title("Violin Plot with Overlaid Swarm Plot")
plt.xlabel('Season')
plt.ylabel('Rainfall (mm)')
sns.despine()
plt.show()
