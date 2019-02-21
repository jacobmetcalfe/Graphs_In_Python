import pygal
import pygal.maps.world
worldMap = pygal.maps.world.World()
worldMap.title = 'North, Central, and South America'
worldMap.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
worldMap.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
worldMap.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])
worldMap.render_to_file('na_populations.svg')
