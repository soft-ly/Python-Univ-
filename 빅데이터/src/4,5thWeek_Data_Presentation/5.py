from sklearn.datasets import make_classification
from collections import Counter

from imblearn.over_sampling import RandomOverSampler

x, y = make_classification(n_samples=10000, n_features=5, weights=[0.99], flip_y=0)
print(Counter(y))

oversample = RandomOverSampler(sampling_strategy='minority')
x_over, y_over = oversample.fit_resample(x,y)
print(Counter(y_over))

oversample = RandomOverSampler(sampling_strategy=0.4)
x_over, y_over = oversample.fit_resample(x,y)
print(Counter(y_over))