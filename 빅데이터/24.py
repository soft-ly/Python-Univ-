import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('dust_info.xlsx',index_col='area')
print(data.head())

temp_data = data.loc['Seoul':'Ulsan', '2015_good':'2020_good']
print(temp_data)

index = np.arange(7)
plt.figure(figsize=(20, 4))
for year in range(2015,2021): #2015~2020
    year = str(year) + '_good'
    chartdata = temp_data[year]
    plt.bar(index, chartdata, width=0.15, label = 'year')
    index = index + 0.15

plt.xlabel('Area')
plt.ylabel('Micrometer')
plt.xticks(index-0.53, 
           ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan'])
plt.title('2015~2020 Fine Dust(pm10) Good Group Bar Graph')
plt.legend()
plt.show()