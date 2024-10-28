import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

print(df.head(10))
#sns.scatterplot(data=df[df['Year']>=2000], x='Year', y='January')

melted_df = df.melt(id_vars=['Year'], var_name='Month', value_name='Rainfall')

print(melted_df.head())

#sns.scatterplot(data=melted_df[melted_df['Year']<1970], x='Month', y='Rainfall')

melted_df = melted_df[melted_df['Year']>2010]

# Bar plot - Total rainfall per year
sns.barplot(data=melted_df,
            x='Year', y='Rainfall')

plt.show()


