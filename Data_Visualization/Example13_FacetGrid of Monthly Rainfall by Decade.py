import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')
# Melt the DataFrame to convert month columns (January - December) into a single column named 'Month'
df_melted = pd.melt(df, id_vars=['Year'], value_vars=['January', 'February', 'March', 'April', 'May',
                                                       'June', 'July', 'August', 'September',
                                                       'October', 'November', 'December'],
                    var_name='Month', value_name='Rainfall')

# Define the dictionary to map each month to its corresponding season
seasons = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
}

# Map the 'Month' column to the corresponding season using the seasons dictionary
df_melted['Season'] = df_melted['Month'].map(seasons)

# Facet plot for each month
g = sns.FacetGrid(df_melted, col="Month",
                  col_wrap=4, height=3, aspect=1.2)
g.map(sns.lineplot, "Year", "Rainfall", color="b")

sns.despine()
g.set_titles("{col_name}")
g.set_axis_labels("Year", "Rainfall (mm)")


plt.show()

