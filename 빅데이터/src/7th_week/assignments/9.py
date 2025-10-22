import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

manhattan_data = pd.read_csv('manhattan.csv')
manhattan_data.head()

x = manhattan_data[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway','floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = manhattan_data['rent']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, train_size=0.7)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

my_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]
my_predict = model.predict(my_apartment)
print("Predicted rent for my apartment:", my_predict)

y_pred = model.predict(x_test)
print("Predicted rents for test set:", y_pred)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,7))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.title('Actual vs Predicted Rent')
plt.xlabel('Actual Rent')
plt.ylabel('Predicted Rent')
plt.show()

print(r2_score(y_test, y_pred))