from operator import itemgetter
import branca
import folium
import pandas
from folium.plugins import HeatMap

excel_data=pandas.read_excel('Тепловая карта.xlsx',sheet_name='зонирование')
d=excel_data['Долгота'].tolist()
s=excel_data['Широта'].tolist()
x=excel_data['цена, руб./кв.м'].tolist()
adr=excel_data['Адрес'].tolist()
stoim=excel_data['Стоимость квартиры, руб.'].tolist()

l=[]
i=0
j=len(x)-1
while i<=j:
    l.append([x[i],s[i],d[i],adr[i],stoim[i]])
    i=i+1
l=sorted(l,key=itemgetter(0))

map=folium.Map(location=[55.154,61.4291],zoom_start=12,control_scale=True)

HeatMap(zip(s, d, x)).add_to(map)
r=l[len(l)-1][0]-l[0][0]
i=0
st=l[0][0]
stm=l[len(l)-1][0]

while i<=len(l)-1:
    m=l[i][0]
    radius=(m-st)*5/stm
    loc = (l[i][1], l[i][2])
    folium.CircleMarker(location=loc, radius=4+radius, popup=f'{l[i][3]},\n Стоимость {l[i][4]} руб,\n1кв.м={l[i][0]}руб.', fill_color='white', color='blue',
                    fill_opacity=0.9).add_to(map)
    i=i+1
map.save('Тепловая_карта3.html')