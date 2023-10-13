def get_text_svg_element(a,b,c,font_size):
 s='<text font-size="{}" x="{}" y="{}" fill="black" stroke="none">{}</text>'
 return s.format(font_size,a,b,c)
