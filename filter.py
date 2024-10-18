import pandas as pd

# Load the dataset (assuming the file is named 'data.csv')
df = pd.read_csv('./assets/Quotes.csv', sep=';')

# Filter rows where the length of the string in the 'QUOTE' column is less than or equal to 170
filtered_df = df[df['QUOTE'].str.len() <= 110]

# Save the filtered data to a new CSV file (optional)
filtered_df.to_csv('filtered_data.csv', sep=';', index=False)

# Print the first few rows to verify
print(len(filtered_df))
