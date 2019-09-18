#Script to find the Male and Female passenges who survived in the ship
import pandas as pd
abs_path = r'https://python-lab-scripts.s3.ap-south-1.amazonaws.com/titanic/titanic.csv'
titanic = pd.read_csv(abs_path)
survival_mask = titanic['Survival'] == 0
titanic_survival = titanic[survival_mask]
print(titanic_survival['Gender'].value_counts())