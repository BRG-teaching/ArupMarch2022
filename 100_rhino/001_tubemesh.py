import compas
from compas.datastructures import Mesh
from compas.artists import Artist


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))


Artist.clear()

artist = Artist(mesh)

artist.draw_faces()
artist.draw_vertices()

Artist.redraw()
