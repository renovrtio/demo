import pygal.maps.world

wm = pygal.maps.world.World()

wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('亚洲', {'cn' : 12348966, 'jp' : 1694, 'tw' : 126})

wm.render_to_file('americas.svg')