import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
sns.set_style("ticks", {"xtick.major.size": 16, "ytick.major.size": 16})
sns.despine(top=True, right=True)

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

df_melted = df.melt(id_vars=['Year'],
                    var_name='Month', value_name='Rainfall')

sns.catplot(data=df_melted, x='Month', y='Rainfall',
            kind='box',  height=5, aspect=2)

plt.tight_layout()
plt.show()


