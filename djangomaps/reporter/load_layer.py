import os
from django.contrib.gis.utils import LayerMapping
from .models import Countie

# Auto-generated `LayerMapping` dictionary for Countie model
countie_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/counties.shp'))

def run(verbose=True):
    lm = LayerMapping(
        Countie, county_shp, countie_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)