# Data grabbed from http://data.okfn.org/
import json
from country_codes import get_country_code
import pygal
import pygal.maps.world

# Load data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

    # dictionary for population data
    cc_populations = {}
    # 2010's pop data
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            # JSON always converts to string so we have to convert to int and then float for rounding
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                # associating the code with the population
                cc_populations[code] = population

worldMap = pygal.maps.world.World()
worldMap.title = 'World Population in 2010, by Country'
worldMap.add('2010', cc_populations)

worldMap.render_to_file('world_population.svg')
