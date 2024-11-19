import pandas as pd
import numpy as np

# Create a DataFrame with 10 rows and 4 columns of random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Apply styling using the updated method
def highlight_negative_positive(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Use map instead of applymap for conditional formatting
styled_df = df.style.map(highlight_negative_positive)

# Display the styled DataFrame
styled_df
