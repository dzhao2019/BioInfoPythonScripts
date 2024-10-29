import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')
df = df[(df['Year'] <= 1969)]

# Pivot data to prepare for heatmap
df_heatmap = df.set_index('Year').loc[:, 'January':'December']

# Convert rainfall to units of 100 mm
df_heatmap = df_heatmap / 100

# Plot heatmap with annotations
sns.heatmap(df_heatmap, cmap='Blues', annot=True,
            fmt=".1f", cbar_kws={'label': 'Rainfall (100 mm)'})

plt.title('Monthly Rainfall Heatmap (1960s)')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Month')
plt.ylabel('Year')
# Rotate x-axis labels
sns.despine()
plt.show()
