import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score

x=[[2], [4], [6], [8], [10]]
y=[[81], [93], [90], [97], [100]]

plt.scatter(x, y)
plt.show()

model = LR()
model.fit(x, y)

result = model.predict([[7]])
print("Predicted value for input 7:", result)