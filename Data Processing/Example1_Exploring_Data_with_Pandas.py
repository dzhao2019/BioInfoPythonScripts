import pandas as pd

# Load the data from a TSV file
# Read the 'eukaryotes.tsv' file, specifying that the fields are separated by tabs (	)
# The resulting data is loaded into a DataFrame named 'euk'
euk = pd.read_csv("eukaryotes.tsv", sep="\t")

# Export the DataFrame to an Excel file
# This saves the DataFrame 'euk' to an Excel file named 'eukaryotes.xlsx' without the index column
euk.to_excel('eukaryotes.xlsx', index=False)

# Print the shape of the DataFrame
# 'euk.shape' provides the number of rows and columns in the DataFrame
print("\neuk.shape", euk.shape)

# Print the first 5 rows of the DataFrame
# 'euk.head()' returns the first 5 rows, giving a preview of the data
print("\neuk.head()", euk.head())

# Print the last 2 rows of the DataFrame
# 'euk.last(2)' returns the first 2 rows, giving a preview of the data
print("\neuk.head()", euk.head(2))

# Print a summary of the DataFrame's structure
# 'euk.info()' provides information such as the number of entries, column names, data types, and memory usage
print("\neuk.info()", euk.info())

# Print summary statistics of numerical columns
# 'euk.describe()' returns statistical information like count, mean, min, max for numeric columns
print("\neuk.describe()", euk.describe())

# Print the default data types of each column
# 'euk.dtypes' returns the data type for each column as detected by pandas
print("\neuk.dtypes in default", euk.dtypes)

# Define data types for specific columns
# A dictionary named 'my_types' is created to specify the desired data types for columns
my_types = {
    "Species": "string",          # Set 'Species' column type to string
    "Kingdom": "string",          # Set 'Kingdom' column type to string
    "Class": "string",            # Set 'Class' column type to string
    "Assembly status": "string",  # Set 'Assembly status' column type to string
    "Number of genes": "Int64",   # Set 'Number of genes' column type to Int
    "Number of proteins": "Int64" # Set 'Number of proteins' column type to Int
}

# Load the data again, with specified column data types
# 'dtype=my_types' ensures that pandas reads the specified columns with the correct data types
#  na_values=["-"] tells pandas dash symbol “-” means missing data
euk = pd.read_csv("eukaryotes.tsv", sep="\t",
    dtype=my_types, na_values=["-"])

# Print the data types after specifying them explicitly
print("\neuk.dtypes", euk.dtypes)

# Generates summary statistics and rounds the output to one decimal place
print(euk.describe().round(1))


