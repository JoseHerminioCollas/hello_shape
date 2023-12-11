from madrid.natural import natural

data_path = 'data/Madrid-shp/shape/natural.shp'


def test_natural():
    n = natural(1, 2000, data_path, '', -4.0, 40.3, 0.2)
    assert n
