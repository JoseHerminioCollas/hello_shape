from shape_to_svg import shape_to_svg

def svg(a,s,d,f):
    return 'X'
class A():
    svg=svg

shapely_mock=A()
def test_shape_to_svg():
    assert isinstance(shape_to_svg(shapely_mock),str)