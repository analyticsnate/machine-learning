
# Import Required Packages
import pandas as pd
from pandas import Series, DataFrame

import numpy as np

# Read col_names.txt file - this file is section 7. Attribute Information from audiology.standardized.names.txt
DF_audiology_standardized_cols = pd.read_table('col_names.txt',columns=(['Column','Valid Values']),delimiter=':')
print(DF_audiology_standardized_cols)

# Read raw file
DF_audiology_standardized_raw = pd.read_table('audiology.standardized.data.txt')

#print(DF_audiology_standardized_raw.iloc[0])


