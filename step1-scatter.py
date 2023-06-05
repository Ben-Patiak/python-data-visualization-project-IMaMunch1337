'''
Thrishath
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/682024/Downloads/netflix.csv")
print(df.columns)

#create basic scatterplot
plt.plot(df['ratingDescription'], df['release year'], 'o')


#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(df['ratingDescription'], df['release year'], 1)

#computing correlation coefficient
r = np.corrcoef(df['ratingDescription'], df['release year'])
 
#add linear regression line and r to scatterplot 
plt.plot(df['ratingDescription'], m*df['ratingDescription']+b)

text = 'y = '+ str(round(m,2)) + 'x +'+ str(round(b,2))
plt.text(1300, 280000,text, fontsize=10)

text2 = 'r = '+ str(round(r[0,1],4))
plt.text(1300, 260000,text2, fontsize=10)

plt.show()
