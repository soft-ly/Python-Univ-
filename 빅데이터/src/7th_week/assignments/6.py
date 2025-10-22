import pandas as pd
from sklearn.model_selection import train_test_split

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

