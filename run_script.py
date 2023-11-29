import time
from madrid.natural_2 import natural_2

item_scale = 2
group_scale = 300
data_path = 'data/Madrid-shp/shape/natural.shp'
file = open('madrid/style.css', 'r', encoding='utf-8')
# extent = (-4.0699641, -3.2300143, 40.170042, 40.6499669)
# generate the series here
t = time.strftime('%X', time.localtime())
destination_path = '__generated/madrid_2023_11_29{}.svg'.format('-b')
svg_tag = natural_2(
    item_scale, group_scale,
    data_path, file.read(),
    -4.0, 40.3,
    0.2,
    True, True
)
file = open(destination_path, 'w')
file.write(svg_tag)
print('File created: ', file)
