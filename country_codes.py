from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    # return the pygal 2 digit country code for the given country.
    for code, name in COUNTRIES.items():
        # if name is found then the country code is returned
        if name == country_name:
            return code
        # If country name not found
        return None