'''
Thrishath
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/682024/Downloads/netflix.csv")

print("-----------------------------------")
print("STATISTICAL SUMMARIES")
print("-----------------------------------")
print(df['release year'].describe())

#Histogram
plt.hist(df['release year'],
         bins = 6)
         
plt.show()

#Boxplot
plt.boxplot(df['release year'])
plt.show()

