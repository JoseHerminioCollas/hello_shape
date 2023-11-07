class SVGTag:
    name = 'SVGTag'

    def __init__(self):
        self.doc = ''

    def render(self):
        svg_doc = '<svg viewBox="-300 -300 600 600" width="600" height="600" stroke="green" stroke-width="1">'
        svg_doc += self.doc
        svg_doc += '</svg>'
        return svg_doc

    def set_text_element(self, name, x, y, font_size=1, color='rgba(3,3,113,0.5)'):
        svg_text = '<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
        self.doc += svg_text.format(font_size, x, y, color, name)

    def set_polygon(self, doc_str):
        self.doc += doc_str
        return True
