import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('dust_info.xlsx',index_col='area')
print(data.head())

plt.figure(figsize=(20, 4))

for year in range(2015,2021): #2015~2020
    year = str(year) + '_good'
    chartdata = data[year]
    plt.plot(chartdata, marker='o', label = 'year')

plt.xlabel('Area')
plt.ylabel('Micrometer')
plt.title('2015~2020 Fine Dust(pm10) Good Line Graph')
plt.legend()
plt.grid()
plt.show()