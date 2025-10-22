import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

seoul = pd.read_excel('(2010-2020) weather.xlsx')
seoul = seoul.drop(labels=['지점'], axis=1)
seoul.columns = ['날짜', '평균기온', '최저기온', '최고기온']
seoul = seoul.dropna(axis=0)
seoul['년도'] = seoul['날짜'].dt.year
conditions = (seoul['날짜'].dt.month == 8) & (seoul['날짜'].dt.day == 15)
seoul_8_15 = seoul[conditions]

model = LR()
X = seoul_8_15.loc[:, ['년도']]
Y = seoul_8_15.loc[:, ['평균기온']]
model.fit(X, Y)
result = model.predict([[2022]])
print("Predicted average temperature in Seoul on August 15, 2022:", result)

x =seoul_8_15['년도']
y =seoul_8_15['평균기온']
func_ = model.coef_[0][0]*x + model.intercept_

plt.figure(figsize=(15,7))
plt.scatter(x, y)
plt.plot(x, func_, color='red', ls='dashed')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Temperature in Seoul on August 15 (2010-2020)')
plt.show()