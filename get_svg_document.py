def get_svg_document(inner_contents):
    content='<svg viewBox="-200 150 400 300" width="400" height="300" stroke="rgba(3,3,3,0.0)" stroke-width="0.0" transform="scale(1,-1) translate(0, 0)">'
    content+='<rect width="100" height="99" x="-100" y="0" fill="blue" stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="-0" y="0" fill="green"  stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="100" y="-100" fill="red"  stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="-200" y="-100" fill="yellow"  stoke-width="0.25"/>'
    content+=inner_contents
    content+='</svg>'
    return content