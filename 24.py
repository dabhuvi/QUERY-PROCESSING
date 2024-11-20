import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Date": ["10-03-16", "10-04-16", "10-05-16", "10-06-16", "10-07-16"],
    "Open": [774.25, 776.03, 779.31, 779.0, 779.66],
    "High": [776.07, 778.71, 782.07, 780.48, 779.66],
    "Low": [769.5, 772.89, 775.65, 775.54, 770.75],
    "Close": [772.56, 776.43, 776.47, 776.86, 775.08],
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
plt.plot(df['Date'], df['Open'], label="Open", marker='o')
plt.plot(df['Date'], df['High'], label="High", marker='o')
plt.plot(df['Date'], df['Low'], label="Low", marker='o')
plt.xlabel("Date")
plt.ylabel("Price (in USD)")
plt.title("Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)")
plt.legend()
plt.xticks(rotation=45)
plt.show()
