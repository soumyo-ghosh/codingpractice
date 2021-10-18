# Convert a series of lists to a single series

import pandas as pd

s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])

print("Series of list")
print(s)

s=s.apply(pd.Series).stack().reset_index(drop=True)

print("Unified series")
print(s)