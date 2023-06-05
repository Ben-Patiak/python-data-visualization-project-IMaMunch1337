'''
Thrishath
'''
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("C:/Users/682024/Downloads/netflix.csv")

# Frequency Distribution
freq_dis = pd.crosstab(index=df['ratingDescription'],columns="Frequency")
freq_dis["Relative Frequency"]=round(freq_dis['Frequency']/freq_dis['Frequency'].sum()*100,2)
freq_dis.loc["Total"]=freq_dis[['Frequency', 'Relative Frequency']].sum()
freq_dis.tail()

print("---------------------------------------------")
print("     DISTRIBUTION OF RATING BY DESCRIPTION")
print("---------------------------------------------")
print(freq_dis)

State = df.groupby('ratingDescription').size().reset_index(name = 'Rating')

State.plot.bar(x='ratingDescription',
               y='Rating')
plt.show()
