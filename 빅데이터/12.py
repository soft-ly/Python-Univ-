import pandas as pd

df1 = pd.DataFrame({'id': [1,2,3,4],
                    'name': ['AAA', 'BBB', 'CCC', 'DDD'],
                    'price': [1000, 2000, 3000, 4000],
                    'value': [500, 1000, 1500, 2000]})

df2 = pd.DataFrame({'id': [1,2,3,5],
                    'product_name': ['AAA','BBB','CCC','EEE'],
                    'day':['0708','0709', '0710']})

## merge, and join 함수 학습 해놓기

