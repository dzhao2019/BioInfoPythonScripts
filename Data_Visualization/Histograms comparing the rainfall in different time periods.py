import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read and prepare the data
df = pd.read_csv('london_rainfall.csv')

# Create subplots
fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(12, 5))

# Plot histogram for January rainfall
sns.histplot(df['January'], stat='percent', ax=ax0)
ax0.set(title='January Rainfall', xlabel='Rainfall (mm)')
# Add a vertical line at a certain threshold (e.g., 500 mm)
ax0.axvline(x=504, label='Mean (504 mm)', linestyle='--', color='r')
ax0.set_xlim(df['January'].min(), df['January'].max())  # January
ax0.legend()

# Plot histogram for February rainfall
sns.histplot(df['February'], stat='percent', ax=ax1)
ax1.set(title='February Rainfall', xlabel='Rainfall (mm)', xlim=(0, 2000))

# Add a vertical line at a certain threshold (e.g., 500 mm)
ax1.axvline(x=504, label='Mean (504 mm)', linestyle='--', color='r')
ax1.set_xlim(df['February'].min(), df['February'].max())  # February
ax1.legend()

# Plot histogram for February rainfall
sns.histplot(df['March'], stat='percent', ax=ax2)
ax2.set(title='March Rainfall', xlabel='Rainfall (mm)', xlim=(0, 2000))

# Add a vertical line at a certain threshold (e.g., 500 mm)
ax2.axvline(x=504, label='Mean (504 mm)', linestyle='--', color='r')
ax2.set_xlim(df['March'].min(), df['March'].max())  # March
ax2.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
