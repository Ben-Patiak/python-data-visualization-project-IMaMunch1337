'''
Thrishath
'''
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/682024/Downloads/netflix.csv")

print(df.head())
print(df.dtypes)

Gender = df["rating"].value_counts()

Gender.plot(kind="pie")


plt.style.use("dark_background")
colors=["blue","red"]
Gender.plot(kind='pie',
            title = 'Distrubution of Movie rating',
            figsize = (6,6),
            colors = colors,
            autopct='%1.1f%%',
            wedgeprops= {'edgecolor':'yellow'}
            )
plt.legend()
plt.show()