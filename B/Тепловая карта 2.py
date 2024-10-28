from operator import itemgetter
import branca
import folium
import pandas
from folium.plugins import HeatMap

excel_data=pandas.read_excel('Тепловая карта.xlsx',sheet_name='зонирование')
d=excel_data['Долгота'].tolist()
s=excel_data['Широта'].tolist()
x=excel_data['цена, руб./кв.м'].tolist()

list=[]
i=0
j=len(x)-1
while i<=j:
    list.append([x[i],s[i],d[i]])
    i=i+1
list=sorted(list,key=itemgetter(0))

map=folium.Map(location=[55.154,61.4291],zoom_start=12,control_scale=True)

HeatMap(zip(s, d, x)).add_to(map)
gradient_map={0.1:'#88ff90',1:'green'}
map.save('Тепловая_карта2.html')