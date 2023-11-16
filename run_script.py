from madrid_natural import madrid_natural

item_scale = 2
group_scale = 10000
data_path = 'data/Madrid-shp/shape/natural.shp'
file = open('style.css', 'r', encoding='utf-8') 

destination_path = '__generated/madrid_parks_11_16-b.svg'

svg_tag=madrid_natural(item_scale,group_scale,data_path,file.read())

file = open(destination_path, 'w')
file.write(svg_tag)
print('File created: ', file)