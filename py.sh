# example of use of py.sh
# ./py.sh madrid.natural natural 2 3 data/Madrid-shp/shape/natural.shp __generated/file.svg
# package function item_scale group_scale data_path style_sheet_path destination

s="from $1 import $2;"
s+="svg = $2($3,$4,'$5','$6');";
s+="print(svg)"
python3 -c "${s}" > $7
