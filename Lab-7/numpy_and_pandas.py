import numpy as np
A = np.random.randn(5, 3)
print(A, type(A))

import pandas as pd
dfA = pd.DataFrame(A)
print(dfA,type(dfA))