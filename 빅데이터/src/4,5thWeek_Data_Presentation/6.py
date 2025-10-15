from sklearn.datasets import make_classification
from collections import Counter

from imblearn.over_sampling import SMOTE

x, y = make_classification(n_samples=10000, n_features=5, weights=[0.99], flip_y=0)
print(Counter(y))

smote = SMOTE(sampling_strategy='minority')
x_sm, y_sm = smote.fit_resample(x,y)
print(Counter(y_sm))

oversample = SMOTE(sampling_strategy=0.4)
x_sm, y_sm = smote.fit_resample(x,y)
print(Counter(y_sm))