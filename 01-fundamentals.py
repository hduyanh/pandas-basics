import pandas as pd

users = pd.DataFrame(columns=['age','gender','hobby'], data=[[30,'Male','coding'],[18,'Male','reading'],[30,'Female','writing'],[23,'Female','travelling']])

type(users) # DataFrame
type(users['age']) # Series

# apply to DataFrame object
users.drop_duplicates() 

# apply to Series object
users['age'].drop_duplicates()
