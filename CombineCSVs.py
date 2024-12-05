import pandas as pd

# Load the two CSVs
csv1 = pd.read_csv('gaia_matched\DESY_NotMDwarfs_Crossmatch.csv')
csv2 = pd.read_csv('gaia_matched\JOHNSTON_MDwarfs_Crossmatch.csv')
csv3 = pd.read_csv('gaia_matched\DESY_MDwarfs_Crossmatch.csv')
csv4 = pd.read_csv('gaia_matched\JOHNSTON_MDwarfs_Crossmatch.csv')

# Add a new column to distinguish the source
csv1['source'] = 'B'  # Replace 'csv1' with your desired label
csv2['source'] = 'M'  # Replace 'csv2' with your desired label
csv3['source'] = 'B'  # Replace 'csv2' with your desired label
csv4['source'] = 'M'  # Replace 'csv2' with your desired label

# Combine the two CSVs using concat
combined_df = pd.concat([csv1, csv2, csv3, csv4], ignore_index=True)

# Save the combined dataframe to a new CSV (optional)
combined_df.to_csv('ALL_M&NotMDwarfs.csv', index=False)
