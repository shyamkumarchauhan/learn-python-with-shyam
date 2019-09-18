#Script to find the passenges who spent more than 200 USD
import pandas as pd
abs_path = r'https://python-lab-scripts.s3.ap-south-1.amazonaws.com/titanic/titanic.csv'
titanic = pd.read_csv(abs_path)
fare_mask = titanic['Fare'] > 200
titanic_fare = titanic[fare_mask]
print(titanic_fare['Fare'].count())