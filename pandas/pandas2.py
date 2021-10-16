#Convert a pandas module series to python list 

import pandas as pd

ds=pd.Series([34,56,72,32,1])

ls=ds.tolist()

print("This is a series:")
print(ds)
print(type(ds))

print("This is a list")
print(ls)
print(type(ls))