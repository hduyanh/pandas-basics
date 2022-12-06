import pandas as pd

users = pd.DataFrame(columns=['age','gender','hobby'], data=[[30,None,'coding'],[18,'Male','reading'],[30,'Female','writing'],[23,'Female','travelling']])

# new series: age in 10 years
users['age in 10 years'] = users['age'] + 10

# new series: genders in binary
users['gender in binary'] = users['gender'].apply(lambda x: 1 if x=='Male' else (0 if x=='Female' else None))

# fill empty values
users.fillna('this used to be empty', inplace=True)
