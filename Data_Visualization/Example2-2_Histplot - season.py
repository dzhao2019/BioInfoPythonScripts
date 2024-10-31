import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')

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

# Create a histogram - rainfall
sns.histplot(data=df_melted, x='Rainfall',
             hue='Season',
             multiple="stack",
             hue_order=['Spring', 'Summer', 'Autumn','Winter'])

# Remove the top and right spines for better aesthetics
sns.despine()
plt.show()



