# example of use of py.sh
# ./py.sh madrid.natural natural 2 3 data/Madrid-shp/shape/natural.shp > file.svg

s="from $1 import $2;"
s+="svg=$2(${3},${4},'${5}','');"
s+="print(svg)"

python3 -c "${s}"
