import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Year': [2020, 2021, 2022, 2023],
    'Rainfall_Jan': [5.0, np.nan, 8.2, np.nan],
    'Rainfall_Feb': [7.1, 2.4, np.nan, np.nan],
    'Rainfall_Mar': [5.5, 3.1, 4.6, np.nan]
}

df = pd.DataFrame(data)
print(df)

# Drop rows where any values are null
df_dropped1 = df.dropna(how='any')
print("\ndf_dropped1:",df_dropped1)

# Keep only the rows with at least 2 non-NA values.
df_dropped2 = df.dropna(thresh=2)
print("\ndf_dropped2:",df_dropped2)

# Fill missing values with a specified value (e.g., replace NaN with 0)
df_filled = df.fillna(0)
print("\ndf_filled:",df_filled)