# Import pandas for data manipulation
import pandas as pd

# Load the Blast data from a tab-separated file without headers
Blast = pd.read_csv("Blast.txt", sep="\t", header=None)

# Assign column names to the DataFrame
Blast.columns = ['qseqid', 'sseqid', 'evalue', 'pident', 'qcovhsp', 'nident', 'sskingdoms']

# Convert 'qcovhsp' column to float to ensure proper data type for calculations
Blast['qcovhsp'] = Blast['qcovhsp'].astype(float)

# Sort the DataFrame by 'nident' in descending order to prioritize higher values
Blast = Blast.sort_values(by=['nident'], ascending=False)

# Create a subset of the DataFrame with only 'qseqid' and 'sskingdoms' columns
Blast_subset = Blast[['qseqid', 'sskingdoms']]

# Filter rows where 'nident' is greater than 300
Blast_filtered1 = Blast[Blast['nident'] > 300]

# Filter rows where 'sskingdoms' is 'Bacteria' and 'pident' is greater than 80
Blast_filtered2 = Blast[(Blast['sskingdoms'] == 'Bacteria') & (Blast['pident'] > 80)]

# Group by 'qseqid' and get the first occurrence of 'qseqid' in each group
Blast_filtered3 = Blast.groupby('qseqid').first()

# Replace any N/A values in the 'sskingdoms' column with 'Unknown'
Blast['sskingdoms'] = Blast['sskingdoms'].fillna('Unknown')

# Group by 'qseqid' and calculate the sum of 'nident' for each group
Blast_filtered4 = Blast.groupby('qseqid')['nident'].sum()

# Display the first few rows of the grouped and summed data
print(Blast_filtered4.head())

# Save the grouped and summed data to a new tab-separated file
Blast_filtered4.to_csv("Blast_filtered.txt", sep='\t', index=False)
