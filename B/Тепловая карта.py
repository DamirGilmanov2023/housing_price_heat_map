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

op=list[len(list)-1][0]-list[0][0]
op4=op/4
i=0
x1=[]
s1=[]
d1=[]
x2=[]
s2=[]
d2=[]
x3=[]
s3=[]
d3=[]
x4=[]
s4=[]
d4=[]
a1=list[0][0]+op4
a2=list[0][0]+op4*2
a3=list[0][0]+op4*3
a4=list[0][0]+op4*4
while i<=len(list)-1:
    if list[i][0]<=a1:
        x1.append(list[i][0])
        s1.append(list[i][1])
        d1.append(list[i][2])
    if a1<list[i][0]<=a2:
        x2.append(list[i][0])
        s2.append(list[i][1])
        d2.append(list[i][2])
    if a2<list[i][0]<=a3:
        x3.append(list[i][0])
        s3.append(list[i][1])
        d3.append(list[i][2])
    if a3<list[i][0]<=a4:
        x4.append(list[i][0])
        s4.append(list[i][1])
        d4.append(list[i][2])
    i=i+1



map=folium.Map(location=[55.154,61.4291],zoom_start=12,control_scale=True)
min_x=x1[0]
max_x=x1[len(x1)-1]
color_map= branca.colormap.LinearColormap(colors=['#88f5ff','blue'],index=[min_x,max_x],vmin=min_x,vmax=max_x)
color_map.caption = f'Стоимость квартир от {min_x} до {max_x} руб./кв.м'
color_map.add_to(map)
min_x=x2[0]
max_x=x2[len(x2)-1]
color_map= branca.colormap.LinearColormap(colors=['#88ff90','green'],index=[min_x,max_x],vmin=min_x,vmax=max_x)
color_map.caption = f'Стоимость квартир от {min_x} до {max_x} руб./кв.м'
color_map.add_to(map)
min_x=x3[0]
max_x=x3[len(x3)-1]
color_map= branca.colormap.LinearColormap(colors=['#fff846','yellow'],index=[min_x,max_x],vmin=min_x,vmax=max_x)
color_map.caption = f'Стоимость квартир от {min_x} до {max_x} руб./кв.м'
color_map.add_to(map)
min_x=x4[0]
max_x=x4[len(x4)-1]
color_map= branca.colormap.LinearColormap(colors=['#ff4646','red'],index=[min_x,max_x],vmin=min_x,vmax=max_x)
color_map.caption = f'Стоимость квартир от {min_x} до {max_x} руб./кв.м'
color_map.add_to(map)

gradient_map={0.1:'#88f5ff',1:'blue'}
HeatMap(zip(s1, d1, x1),gradient=gradient_map).add_to(map)
gradient_map={0.1:'#88ff90',1:'green'}
HeatMap(zip(s2, d2, x2),gradient=gradient_map).add_to(map)
gradient_map={0.1:'#fff846',1:'yellow'}
HeatMap(zip(s3, d3, x3),gradient=gradient_map).add_to(map)
gradient_map={0.1:'#ff4646',1:'red'}
HeatMap(zip(s4, d4, x4),gradient=gradient_map).add_to(map)
map.save('Тепловая_карта.html')