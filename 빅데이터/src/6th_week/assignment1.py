import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('train.csv')

plt.figure(figsize=(10,6))
sns.countplot(data=data, x='Sex', hue='Embarked') 
plt.xlabel('Sex')
plt.ylabel('Boarding')
plt.title('성별과 탑승 항구별 빈도수')
plt.show()
