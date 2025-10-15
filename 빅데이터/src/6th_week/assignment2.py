import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

sibsp_x = data['SibSp']
parch_y = data['Parch']

plt.figure(figsize=(10,6))
plt.scatter(sibsp_x, parch_y, alpha=0.5)
plt.xlabel('Siblings/Spouses')
plt.ylabel('Parents/Children')
plt.title('SibSp vs Parch')
plt.show()