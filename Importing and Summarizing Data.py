#Read and explore your data

# Import pandas 
import pandas as pd
# Use pandas to read in recent_grads_url
recent_grads = pd.read_csv(recent_grads_url)
# Print the shape
print(recent_grads.shape)


#Exploring Your Data

# Print .dtypes
print(recent_grads.dtypes)
# Output summary statistics
print(recent_grads.describe())
# Exclude data of type object
print(recent_grads.describe(exclude=['object']))


#Replacing Missing Values

# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']
# Take a look at the dtypes
print(recent_grads[columns].dtypes)
# Find how missing values are represented
print(recent_grads["median"].unique())
# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan


#Select a Column

# Select sharewomen column
sw_col = recent_grads["sharewomen"]
# Output first five rows
print(sw_col.head(5))


#Column Maximum Value

# Import numpy
import numpy as np
# Use max to output maximum values
max_sw = np.max(sw_col)
# Print column max
print(max_sw)


#Selecting a Row

# Output the row containing the maximum percentage of women
print(recent_grads[sw_col == max_sw])


#Converting a DataFrame to Numpy Array
import numpy as np
# Convert to numpy array
recent_grads_np = recent_grads[['unemployed','low_wage_jobs']].as_matrix()
# Print the type of recent_grads_np
print(type(recent_grads_np))


#Correlation Coefficient
print(np.corrcoef(recent_grads_np[:,0], recent_grads_np[:,1] ))