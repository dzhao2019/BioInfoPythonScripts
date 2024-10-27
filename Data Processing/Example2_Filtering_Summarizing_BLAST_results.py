# Import pandas for data manipulation
import pandas as pd
import numpy as np  # Import numpy for aggregation functions

# Load the Blast data from a tab-separated file without headers
Blast = pd.read_csv("Blast.txt", sep="\t", header=None)

# Assign column names to the DataFrame
Blast.columns = ['qseqid', 'sseqid', 'evalue', 'pident', 'qcovhsp', 'nident', 'sskingdoms']

# Rename 'qcovhsp' column to 'coverage' (note: rename does not change inplace when using 'inplace=True')
Blast.rename(columns={'qcovhsp': 'coverage'}, inplace=True)

# Convert 'coverage' column to float to ensure proper data type for calculations
Blast['coverage'] = Blast['coverage'].astype(float)

# Sort the DataFrame by 'nident' in descending order to prioritize higher values
Blast = Blast.sort_values(by=['nident'], ascending=False)

# Create a subset of the DataFrame with only 'qseqid' and 'sskingdoms' columns
Blast_subset = Blast[['qseqid', 'sskingdoms']]

# Filter rows where 'nident' is greater than 300
filtered1 = Blast[Blast['nident'] > 300]

# Filter rows where 'sskingdoms' is 'Bacteria' and 'pident' is greater than 80
filtered2 = Blast[(Blast['sskingdoms'] == 'Bacteria') & (Blast['pident'] > 80)]

# Group by 'qseqid' and get the first occurrence of each unique 'qseqid'
filtered3 = Blast.groupby('qseqid').first()

# Replace any NaN values in the 'sskingdoms' column with 'Unknown'
Blast['sskingdoms'] = Blast['sskingdoms'].fillna('Unknown')

# Group by 'qseqid' and calculate the sum of 'nident' for each group
filtered4 = Blast.groupby('qseqid')['nident'].sum()

# Display the counts of each unique value in 'sskingdoms'
print("Counts of each kingdom in 'sskingdoms':")
print(Blast['sskingdoms'].value_counts())

# Display the first few rows of the grouped and summed data
print("First few rows of Blast_filtered4 (sum of 'nident' by 'qseqid'):")
print(Blast_filtered4.head())

# Create a pivot table to show the mean 'nident' values for each 'sskingdoms' by 'qseqid'
df = pd.pivot_table(Blast, values='nident', index='qseqid', 
                    columns='sskingdoms', aggfunc=np.mean)

# Save the pivot table to a new tab-separated file
df.to_csv("Blast_pivot_table.txt", sep='\t', index=True)
