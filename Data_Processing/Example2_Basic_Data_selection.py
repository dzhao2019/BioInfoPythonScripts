import pandas as pd

# Define custom data types for columns
# 'Int64' allows null values in integer columns (useful for handling missing data)
my_types = {
    "Species": "string",
    "Kingdom": "string",
    "Class": "string",
    "Assembly status": "string",
    "Number of genes": "Int64",
    "Number of proteins": "Int64"
}

# Load the data from a TSV file
# Use 'na_values=["-"]' to specify that '-' should be considered as NaN (missing value)
euk = pd.read_csv("eukaryotes.tsv", sep="\t", dtype=my_types, na_values=["-"])

# Isolate a Single Column
# Isolate the 'Species' column and print it
species_column = euk['Species']
print("\nSpecies column:")
print(species_column)

# Isolate Two or More Columns
# Isolate the 'Species' and 'Kingdom' columns and print them
species_kingdom_columns = euk[['Species', 'Kingdom']]
print("\nSpecies and Kingdom columns:")
print(species_kingdom_columns)

# Isolate the row where the index is 1
# Filtering based on the index value
df_index_1 = euk.loc[[1]]  # Using .loc[] is more efficient for indexing by label
print("\nRow with index 1:")
print(df_index_1)

# Isolate a Range of Rows
# Isolate rows with index between 2 and 9 (inclusive of 2 but not 10)
rows_range = euk.iloc[2:10]  # Using iloc for integer-location indexing
print("\nRows with index from 2 to 9:")
print(rows_range)

# Example of filtering based on a condition
# Find all genomes where 'Size (Mb)' is greater than 500
large_genomes = euk[euk["Size (Mb)"] > 500]
print("\nFiltered euk with Size > 500 Mb:")
print(large_genomes.head())

# Find genomes belonging to a specific species (e.g., 'Penicillium expansum')
Penicillium = euk[euk["Species"] == "Penicillium expansum"]
print("\nFind Penicillium expansum genomes:")
print(Penicillium.head())

# Find all genomes that are not classified as 'Fishes'
not_fish = euk[euk["Class"] != "Fishes"]
print("\nAll genomes that are not classified as fish:")
print(not_fish.head())

# Find all genomes being either 'Birds' or 'Fish'
bird_fish = euk[euk["Class"].isin(["Birds", "Fish"])]
print("\nGenomes being either 'Birds' or 'Fish':")
print(bird_fish.head())

# Find genomes for species starting with the letter 'Q'
species_Q = euk[euk["Species"].str.startswith("Q")]
print("\nGenomes for species starting with the letter 'Q':")
print(species_Q.head())

# Filter rows where the "Species" column contains "Blastocystis"
blastocystis = euk[euk["Species"].str.contains("Blastocystis")]
print("\nGenomes that contain 'Blastocystis' in their Species name:")
print(blastocystis.head())

# Find genomes between a hundred and a thousand megabases using two approaches
# Using logical conditions
filtered = euk[(euk["Size (Mb)"] > 100) & (euk["Size (Mb)"] < 1000)]
print("\nGenomes between a hundred and a thousand megabases (using logical conditions):")
print(filtered.head())

# Using the between() function
filtered2 = euk[euk["Size (Mb)"].between(100, 1000)]
print("\nGenomes between a hundred and a thousand megabases (using between()):")
print(filtered2.head())

# Find genomes that are not birds or fishes, or have a GC% below 40
filtered8 = euk[~euk["Class"].isin(["Birds", "Fishes"]) | (euk["GC%"] < 40)]
print("\nGenomes that are not birds or fishes, or have low GC%:")
print(filtered8.head())

# Find the sizes of all human genomes (Species = 'Homo sapiens')
human_genome_size = euk[euk["Species"] == "Homo sapiens"]["Size (Mb)"]
print("\nThe sizes of all the human genomes:")
print(human_genome_size.head())

# Find the mean sizes of all bird genomes (Class = 'Birds')
Mean = euk[euk["Class"] == "Birds"]["Size (Mb)"].mean()
print("\nThe mean sizes of all the bird genomes:")
print(Mean)

# Find the median number of genes for genomes with low GC (< 50%)
median = euk[euk["GC%"] < 50]["Number of genes"].median()
print("\nThe median number of genes for genomes with low GC (< 50%):")
print(median)

# Count the number of genomes sequenced for each kingdom in the year 2010
value = euk[euk["Publication year"] == 2010]["Kingdom"].value_counts()
print("\nNumber of genomes sequenced for each kingdom in 2010:")
print(value)

# Find the largest number of proteins for fish genomes from the year 2017
largest = euk[(euk["Class"] == "Fishes") & (euk["Publication year"] == 2017)]["Number of proteins"].max()
print("\nLargest number of proteins for fish genomes from 2017:")
print(largest)

# Filter rows where the "Kingdom" column is 'Animals'
animals = euk[euk["Kingdom"] == "Animals"]
print("\nGenomes of the Kingdom 'Animals':")
print(animals.head())



# Aggregating data with .groupby()
# Group genomes by 'Kingdom' and calculate the mean size for each kingdom
grouped_kingdom = euk.groupby("Kingdom")[["Size (Mb)"]].mean()
print("\nMean size of genomes by Kingdom:")
print(grouped_kingdom)

# Group by 'Class' and count the number of genomes in each class
grouped_class_count = euk.groupby("Class").size()
print("\nNumber of genomes in each Class:")
print(grouped_class_count)

# Group by 'Publication year' and calculate the maximum number of genes for each year
grouped_year_max_genes = euk.groupby("Publication year")["Number of genes"].max()
print("\nMaximum number of genes by Publication year:")
print(grouped_year_max_genes)

# Group by 'Assembly status' and calculate the median GC percentage for each status
grouped_assembly_gc = euk.groupby("Assembly status")["GC%"].median()
print("\nMedian GC% by Assembly status:")
print(grouped_assembly_gc)