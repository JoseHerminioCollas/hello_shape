def get_svg_document(inner_contents):
# -50 -50 100 200" width="200" height="200"
    content='<svg viewBox="-300 -300 600 600" width="600" height="600" stroke="green" stroke-width="1" transform="scale(1,-1) translate(0,-600)">'
    content+='<rect x="0" y="0" width="290" height="290" fill="green" />'
    content+=inner_contents
    content+='</svg>'
    return content