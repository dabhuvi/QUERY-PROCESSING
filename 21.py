import pandas as pd
data = {
    "Name": ["Alice", "bOB", "ChARlie", "davE"],
    "Age": [25, 30, 35, 40],
    "City": ["new york", "LONDON", "PaRiS", "TOKYO"]
}
df = pd.DataFrame(data)
df["Name"] = df["Name"].str.swapcase()

print("DataFrame after swapping cases in 'Name' column:")
print(df)
