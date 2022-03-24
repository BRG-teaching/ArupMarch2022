import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))


vertex = mesh.vertex_sample(size=1)[0]
nbrs = mesh.vertex_neighbors(vertex)
vertices = [vertex] + nbrs
edges = mesh.vertex_edges(vertex)

vertex_color = {nbr: Color.pink() for nbr in nbrs}
edge_color = {edge: Color.pink() for edge in edges}


Artist.clear()

artist = Artist(mesh)

#artist.draw_faces()
artist.draw_vertices(vertices=vertices, color=vertex_color)
artist.draw_edges(color=edge_color)

Artist.redraw()
