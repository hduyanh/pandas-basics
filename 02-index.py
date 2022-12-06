import pandas as pd
import matplotlib.pyplot as plt

users = pd.DataFrame(columns=['age','gender','hobby'], data=[['30','Male','coding'],['18','Male','reading'],['30','Female','writing'],['23','Female','travelling']])

# set 'age' as index
users.set_index('age')

# sort value based on ages
users.sort_values('age', inplace=True) # inplace=True is used depending on if we want to make changes to the original df or not

# reset index, but will create a new column with old index
users.reset_index(inplace=True) 

# accidentally created ages as string, change 'age' objects to float for visualization
users['age'] = users['age'].astype(float) 

# visualization with matplotlib
users['age'].plot()
plt.show()