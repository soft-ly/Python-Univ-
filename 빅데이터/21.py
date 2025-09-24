import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('dust_info.xlsx', index_col='area')
print(data.head())

data2020_good = data['2020_good']
print(data2020_good)

plt.figure(figsize=(20,4))
plt.plot(data2020_good, color = 'b', marker = 'o')
plt.xlabel('Area')
plt.ylabel('Micrometer')
plt.title('2020 Fine Dust(pm10) Good Line Graph')
plt.grid()
plt.show()