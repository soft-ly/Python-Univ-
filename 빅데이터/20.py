## 선 모양, 그림 범위 지정

## 시각화

import pandas as pd
import matplotlib.pyplot as plt

my_score = [[60,90,95],[65,85,90],[80,75,100],[95,90,85],[85,80,65]]
subject = ['1st','2nd','3rd']
df = pd.DataFrame(my_score,columns=subject)

df.plot(kind='line')
df.plot(kind='box')
df.plot(kind='kde')
plt.show()  