import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weather_data = pd.read_csv('(2000-2010) weather.csv')
weather_data.head()

weather_data['날짜']= pd.to_datetime(weather_data['날짜'])
print(weather_data.info())

weather_data['year'] = weather_data['날짜'].dt.year
weather_data['month'] = weather_data['날짜'].dt.month
weather_data['day'] = weather_data['날짜'].dt.day

weather_data.drop('지점', axis=1, inplace=True)

weather_data.rename(columns={'날짜':'date', '평균기온(℃)':'temp'}, inplace=True)