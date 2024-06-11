from extensions import extract, clean, transform

# Extract Data from CSV and Load it into DataFrame
df = extract('financial-year-provisional-size-bands.csv')

# Remove rows with missing values and drop duplicates
new_df = clean(df)

transformed = transform(new_df)
print(transformed.to_string())

# Save the transformed data to a new CSV file if needed
transformed.to_csv('transformed_data.csv', index=False)
