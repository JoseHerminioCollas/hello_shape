class SVGTag:
    name = 'SVGTag'
    side = 600

    def __init__(self, style):
        self.style = style
        self.doc = ''

    def render(self):
        svg_doc = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" viewBox="-300 -300 {s} {s}" width="{s}" height="{s}">'.format(
            s=self.side)
        svg_doc += '<style>' + self.style + '</style>'
        svg_doc += self.doc
        svg_doc += '</svg>'
        return svg_doc

    def set_text_element(self, name, x, y, font_size=9, color='rgba(3,3,113,0.5)'):
        svg_text = '<text x="{}" y="{}">{}</text>'
        self.doc += svg_text.format(x, y, color, name)

    def append(self, svg):
        self.doc += svg

    def prepend(self, svg):
        self.doc = svg + self.doc

    def set_style(self, style):
        self.style = style

    # pass an array of Shapely polygon shapes
    def append_shapes(self, shapes, data, class_name='', has_labels=False):
        svg = '<g class="{}">'.format(class_name)
        for i in range(0,len(shapes)):
            if has_labels:
                label = ('<text x="{}" y="{}">{}</text>'.format(
                    shapes[i].centroid.x,
                    shapes[i].centroid.y,
                    data[i]['properties']['name']
                ))
                svg += label
            svg += shapes[i].svg()
        svg += '</g>'
        self.doc += svg
