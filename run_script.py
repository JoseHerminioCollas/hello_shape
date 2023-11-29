import time
from madrid.natural_2 import natural_2

item_scale = 2
group_scale = 600
data_path = 'data/Madrid-shp/shape/natural.shp'
file = open('madrid/style.css', 'r', encoding='utf-8') 
t = time.strftime('%X', time.localtime())
destination_path = '__generated/madrid_2023_11_28{}.svg'.format('')

svg_tag=natural_2(item_scale,group_scale,data_path,file.read())

file = open(destination_path, 'w')
file.write(svg_tag)
print('File created: ', file)
