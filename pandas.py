import pandas as pd
import numpy as np
df=pd.DataFrame({'A':pd.Timestamp('20200101'),
                 'B':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'C':np.array([3]*4,dtype='int32'),
                 'D':pd.Categorical(['test','train','test','train']),
                 'E':'Foo'})
print(df)
