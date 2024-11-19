import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
ticker = "GOOGL"
start_date = "2023-01-01"
end_date = "2023-12-31"
data = yf.download(ticker, start=start_date, end=end_date)
if not data.empty:
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close Price", color="blue")
    plt.title(f"Alphabet Inc. Stock Prices ({start_date} to {end_date})", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Close Price (USD)", fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()
else:
    print("No data found for the specified date range.")
