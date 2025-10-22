import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = datasets.load_diabetes()
df = pd.DataFrame(data['data'], index=data['target'], columns=data['feature_names'])
print(df)

x = df.loc[:, ['bmi', 'age']].values
y = df.index.values
print(x)

y = y.reshape(-1, 1)

lr = LinearRegression()
lr.fit(x, y)

y_pred = lr.predict(x)

print(r2_score(y, y_pred))
