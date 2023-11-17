s="from madrid_natural import madrid_natural;f=open('style.css','r',encoding='utf-8');style=f.read();svg=madrid_natural(${ITEM_SCALE},${GROUP_SCALE},'${DATA_PATH}',style);f=open('${DEST_PATH}','w');f.write(svg)"
echo $s

python3 -c "${s}"
echo "file written to: ${DEST_PATH} "
