def get_svg_document(inner_contents):
# -50 -50 100 200" width="200" height="200"
    content='<svg viewBox="-300 -300 600 600" width="600" height="600" stroke="green" stroke-width="1" transform="scale(1,1) rotate(0) translate(0,0)">'
    content+='<rect x="0" y="0" width="290" height="290" fill="green" />'
    content+='<g transform="scale(1,1) rotate(0) translate(0,0)">'
    content+=inner_contents
    content+='</g></svg>'
    return content

# <svg viewBox="0 0 600 600" width="500" height="500" stroke="green" stroke-width="1"
#     transform="scale(0.25,0.25) rotate(-90) translate(-900,1100)">