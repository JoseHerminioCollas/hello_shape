def get_svg_text_element(name,x,y,font_size=1,color='rgba(3,3,3,0.5)'):
 svg_text='<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
 return svg_text.format(font_size,x,y,color,name)
