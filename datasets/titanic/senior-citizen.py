#Script to find the Senior Citizens( Age > 58) Travelled
import pandas as pd
abs_path = r'https://python-lab-scripts.s3.ap-south-1.amazonaws.com/titanic/titanic.csv'
titanic = pd.read_csv(abs_path)
age_mask = titanic['Age'] > 58
titanic_age = titanic[age_mask]
print(titanic_age['Age'].count())