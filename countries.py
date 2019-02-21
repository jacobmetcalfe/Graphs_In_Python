# Necessary library for mapping the world
from pygal_maps_world.i18n import COUNTRIES

# Sorts keys in order
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
