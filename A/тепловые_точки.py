import branca
import folium
import pandas
from colour import Color

excel_data=pandas.read_excel('Тепловая карта.xlsx',sheet_name='зонирование')
d=excel_data['Долгота'].tolist()
s=excel_data['Широта'].tolist()
x=excel_data['Стоимость квартиры, руб.'].tolist()
a=excel_data['Адрес'].tolist()

max_x=0
min_x=x[0]
mass_x=[]
for xx in x:
    mass_x.append(xx)
    if max_x<xx:
        max_x=xx
    if min_x>xx:
        min_x=xx
max_x=int(max_x)
min_x=int(min_x)
mass_x.sort()

yellow=Color('yellow')
colors=list(yellow.range_to(Color('red'),len(x)))

map=folium.Map(location=[55.154,61.4291],zoom_start=12,control_scale=True)

i=0
while i<len(s):
    j=0
    k=0
    for m in mass_x:
        if m==x[i]:
            k=j
            break
        j=j+1
    s1=float(s[i])
    d1=float(d[i])
    loc=(s1,d1)
    folium.CircleMarker(location=loc, radius = 8, popup=str(a[i]), fill_color=str(colors[k]), color=str(colors[k]), fill_opacity = 0.9).add_to(map)
    i=i+1

colormap = branca.colormap.LinearColormap(colors=['yellow','red'],index=[min_x,max_x],vmin=min_x,vmax=max_x)
colormap.caption = f'Стоимость квартир от {min_x} до {max_x}'
colormap.add_to(map)

map.save('Тепловые точки.html')