import pandas as pd

# Replace 'your_input_file.xlsx' and 'your_output_file.csv' with the actual filenames
input_file_path = 'NIFTY 50.xlsx'
output_file_path = 'NIFTY 50.csv'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("NIFTY 50.xlsx")

# Write the DataFrame to a CSV file
df.to_csv("NIFTY 50.csv", index=False)

df = pd.read_csv("NIFTY 50.CSV")
print(df)

print(df.columns)

df.sort_values(by='Date ', inplace=True)

df['Daily Returns'] = df['Close '].pct_change()

daily_volatility = df['Daily Returns'].std()

annualized_volatility = daily_volatility * (252 ** 0.5)  # Assuming 252 trading days in a year

print("Daily Returns Series:")
print(df['Daily Returns'])

print("\nDaily Volatility:")
print(daily_volatility)

print("\nAnnualized Volatility:")
print(annualized_volatility)

df['Daily Volatility'] = daily_volatility
df['Annualized Volatility'] = annualized_volatility

for index, row in df.iterrows():
    print(row)



