import os
import compas
from compas.artists import Artist


FILE = os.path.join(os.path.dirname(__file__), 'data.json')


data = compas.json_load(FILE)
monkey = data['monkey']


Artist.clear()

artist = Artist(monkey)
artist.draw(disjoint=True)

Artist.redraw()
