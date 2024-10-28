import folium
import pandas
from folium.plugins import HeatMap

excel_data=pandas.read_excel('Тепловая карта.xlsx',sheet_name='зонирование')
d=excel_data['Долгота'].tolist()
s=excel_data['Широта'].tolist()

map=folium.Map(location=[55.154,61.4291],zoom_start=12,control_scale=True)

HeatMap(list(zip(s, d))).add_to(map)

map.save('Концентрация.html')