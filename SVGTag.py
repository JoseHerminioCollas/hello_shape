class SVGTag:
    name = 'SVGTag'

    def __init__(self):
        self.doc = ''

    def render(self):
        svg_doc = '<svg viewBox="-300 -300 600 600" width="600" height="600" stroke="green" stroke-width="1">'
        svg_doc += ('<style>'
                    'text {font-family:sans-serif;font-size:3px;fill:rgba(3,3,3,0.5);stroke:blue;stroke-width:0}'
                    'path {fill:gold; stroke:rgba(4,4,4,0.5); stroke-width:1px;}'
                    '</style>')
        svg_doc += self.doc
        svg_doc += '</svg>'
        return svg_doc

    def set_text_element(self, name, x, y, font_size=9, color='rgba(3,3,113,0.5)'):
        svg_text = '<text   x="{}" y="{}" fill="{}" stroke="none" text-anchor="middle">{}</text>'
        self.doc += svg_text.format(x, y, color, name)

    def set_polygon(self, doc_str):
        self.doc += doc_str
        return True
