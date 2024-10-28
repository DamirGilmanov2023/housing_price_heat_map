import branca
import folium
import pandas
from folium.plugins import HeatMap
from pandas._libs.internals import defaultdict

excel_data=pandas.read_excel('Тепловая карта.xlsx',sheet_name='зонирование')
d=excel_data['Долгота'].tolist()
s=excel_data['Широта'].tolist()
x=excel_data['Стоимость квартиры, руб.'].tolist()
steps=len(x)

max_x=0
min_x=x[0]
for xx in x:
    if max_x<xx:
        max_x=xx
    if min_x>xx:
        min_x=xx
max_x=int(max_x)
min_x=int(min_x)

map=folium.Map(location=[55.154,61.4291],zoom_start=12,control_scale=True)

color_map= branca.colormap.LinearColormap(colors=['yellow','red'],index=[min_x,max_x],vmin=min_x,vmax=max_x)
color_map.caption = f'Стоимость квартир от {min_x} до {max_x}'
color_map.add_to(map)

gradient_map=defaultdict(dict)
for i in range(steps):
    gradient_map[1/steps*i] = color_map.rgb_hex_str(1/steps*i)

gradient_map={0.1:'yellow',1:'red'}
print(gradient_map)
HeatMap(list(zip(s, d, x)),gradient=gradient_map, min_opacity=0.5).add_to(map)

map.save('Концентрация_с_тепловыми_точками.html')