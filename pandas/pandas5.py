# Covert the first column of a dataframe as a series

import pandas as pd

df=pd.DataFrame(data={'col1':[1,2,3,4,7,11],'col2':[1,2,3,4,7,11],'col3':[7,5,8,12,1,11]})

print("The dataframe:")
print(df)
col1=df.iloc[:,0]
print("Just the first column")
print(col1)