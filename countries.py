import pygal
from pygal_maps_world.i18n import COUNTRIES
# from pygal.maps.world import COUNTRIES
# from pygal_maps_world import i18n

for country_code in COUNTRIES.keys():
    print(country_code, COUNTRIES[country_code])