import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")
print(tips)
# Draw a boxplot to show bills by day
sns.boxplot(x="day", y="total_bill",
            data=tips)

plt.show()

#sns.set_theme(style="ticks", palette="pastel")
# hue="smoker", palette=["m", "g"],
