# example of ucatof py.sh
# ./py.sh adrid.natural natural 2 3 data/Madrid-shp/shape/natural.shp __generated/file.svg
# package function item_scale group_scale data_path style_sheet_path destination

#  make this into a single line, strip out returns
f=`cat ./madrid/style.css`
g="${f//[$'\t\r\n']}"
echo $g


s="from $1 import $2;"
s+="svg = $2($3,$4,'$5','$g');";
s+="print(svg)"
echo $s
python3 -c "${s}" > $7

