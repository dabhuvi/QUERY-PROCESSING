import pandas as pd
data = {
    'Date': ['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03'],
    'Item': ['Item A', 'Item B', 'Item A', 'Item B', 'Item A', 'Item B'],
    'Sale Value': [100, 200, 150, 250, 50, 300]
}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(values='Sale Value', index='Item', aggfunc=['max', 'min'])
print(pivot_table)
