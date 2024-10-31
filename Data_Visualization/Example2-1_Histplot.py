import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')

# Create a histogram - rainfall
sns.histplot(data=df_melted, x='Rainfall')

# Remove the top and right spines for better aesthetics
sns.despine()
plt.show()

# Example2-1_Histplot.png



