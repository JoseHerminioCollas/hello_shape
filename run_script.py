import time
from madrid.natural import natural

item_scale = 1.1    
group_scale = 10000
data_path = 'data/Madrid-shp/shape/natural.shp'
file = open('madrid/style.css', 'r', encoding='utf-8') 
t=time.strftime('%X', time.localtime())
destination_path = '__generated/madrid_parks_11_20{}.svg'.format(t)

svg_tag=natural(item_scale,group_scale,data_path,file.read())

file = open(destination_path, 'w')
file.write(svg_tag)
print('File created: ', file)