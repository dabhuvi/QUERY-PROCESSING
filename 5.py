import yfinance as yf
import matplotlib.pyplot as plt
ticker = "GOOGL"
start_date = "2023-01-01"
end_date = "2023-12-31"

print("Downloading data...")
data = yf.download(ticker, start=start_date, end=end_date)
print("Data fetched: \n", data.head())
if data is None or data.empty:
    print("No data found for the specified ticker or date range.")
else:
    plt.figure(figsize=(12, 6))
    plt.bar(data.index, data["Volume"], color="green", width=1, label="Volume")

    plt.title(f"Alphabet Inc. Trading Volume ({start_date} to {end_date})", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Volume", fontsize=12)
    plt.xticks(rotation=45) 
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
