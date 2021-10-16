# Covert a numpy array to pandas series

import numpy as np
import pandas as pd

x=np.array([10, 20, 30, 40, 50])

print("This is a numpy array")
print(x)

ds=pd.Series(x)

print("This is a pandas series")
print(ds)