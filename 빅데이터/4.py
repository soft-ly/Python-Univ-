from sklearn.datasets import make_classification
from collections import Counter

from imblearn.under_sampling import RandomUnderSampler

x, y = make_classification(n_samples=10000, n_features=5, weights=[0.99], flip_y=0)
print(Counter(y))

undersample = RandomUnderSampler(sampling_strategy='majority')
x_under, y_under = undersample.fit_resample(x,y)
print(Counter(y_under))

undersample = RandomUnderSampler(sampling_strategy=0.4)
x_under, y_under = undersample.fit_resample(x,y)
print(Counter(y_under))