import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

melted_df = df.melt(id_vars=['Year'],
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
melted_df['Season'] = melted_df['Month'].map(seasons)

# Create a histogram - rainfall
sns.histplot(data=melted_df, x='Rainfall',
             hue='Season',
             multiple="stack",
             hue_order=['Spring', 'Summer', 'Autumn','Winter'])

# Remove the top and right spines for better aesthetics
sns.despine()
plt.show()



