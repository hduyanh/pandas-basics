import pandas as pd

users = pd.DataFrame(columns=['age','gender','hobby'], data=[[30,None,'coding'],[18,'Male','reading'],[30,'Female','writing'],[23,'Female','travelling']])

# shell
# users[]

# condition
users['gender'] == 'Female' # return booleans in gender

users[users['gender'] == 'Female'] # return all 3 columns, where gender is 'Female'

# Built-in function, for none values
users[users['gender'].isna()]

# for not none values
users[~users['gender'].isna()]

# return values where ages in the [30, 40] list
users[users['age'].isin([30, 40])]

# combining condition, and
users[(users['hobby'] == 'coding') & (users['age'].isin([30, 40]))]

# combining condition, or
users[(users['hobby'] == 'coding') | (users['age'].isin([30, 40]))]
