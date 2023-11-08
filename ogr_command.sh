ogrinfo \
data/Madrid-shp/shape/natural.shp \
-sql 'select name from natural where name is not null limit 300' \
-spat -3.25 40.170 -3.2 40.6 \
| grep name