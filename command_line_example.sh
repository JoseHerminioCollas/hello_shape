s="from $FUNC_NAME import $FUNC_NAME;"
s+="f=open('${STYLE_PATH}','r',encoding='utf-8');"
s+="style=f.read();"
s+="svg=$FUNC_NAME(${ITEM_SCALE},${GROUP_SCALE},'${DATA_PATH}',style);"
s+="f=open('${DEST_PATH}','w');f.write(svg)"
echo $s

python3 -c "${s}"
echo "file written to: ${DEST_PATH} "
