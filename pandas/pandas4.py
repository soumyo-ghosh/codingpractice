import pandas as pd

ds=pd.Series(["100", "200", "python", "300.12", "400"])

print("Original series")
print(ds)

n_ds=pd.to_numeric(ds, errors = 'coerce')

print("New series converted to numerical only")
print(n_ds)