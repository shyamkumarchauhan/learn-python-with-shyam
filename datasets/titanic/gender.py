#Script to find the Male and Female Passengers Travelled
import pandas as pd
abs_path = r'https://python-lab-scripts.s3.ap-south-1.amazonaws.com/titanic/titanic.csv'
titanic = pd.read_csv(abs_path)
print(titanic['Gender'].value_counts())