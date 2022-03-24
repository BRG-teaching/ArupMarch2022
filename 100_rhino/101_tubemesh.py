import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))


Artist.clear()

artist = Artist(mesh)

artist.draw_vertices()
artist.draw_edges()
artist.draw_edgelabels()

Artist.redraw()
