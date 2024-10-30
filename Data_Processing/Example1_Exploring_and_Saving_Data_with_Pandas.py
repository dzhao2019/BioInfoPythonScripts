# Import pandas for data manipulation
import pandas as pd

# Load the data from a CSV file into a DataFrame
df = pd.read_csv('Diamond_results.csv')

# Display the first 5 rows of the DataFrame to get a quick look at the data
print("\ndf.head():")
print(df.head())

# Display information about the DataFrame, including column data types and non-null counts
print("\ndf.info():")
print(df.info())

# Display summary statistics for numerical columns in the DataFrame
print("\ndf.describe():")
print(df.describe())

# Select the last 10 rows of the DataFrame and save them as a new DataFrame (df2)
df2 = df.tail(10)
print("\nLast 10 rows of data (df2):")
print(df2)

# Save the new DataFrame (df2) to a CSV file without the index column
df2.to_csv('Diamond_results_t10.csv', index=False)
