import compas
from compas.datastructures import Mesh
from compas.geometry import Point, Plane, Circle
from compas.geometry import Cylinder
from compas.artists import Artist
from compas.colors import Color


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))


start = 68, 123
loop = mesh.edge_loop(start)

edge_color = {}
for u, v in loop:
    edge_color[u, v] = edge_color[v, u] = Color.pink()


Artist.clear()

artist = Artist(mesh)

artist.draw_vertices(vertices=start)
artist.draw_edges(color=edge_color)

for u, v in loop:
    a = Point(* mesh.vertex_coordinates(u))
    b = Point(* mesh.vertex_coordinates(v))
    ab = b - a
    radius = 0.05
    height = ab.length
    pipe = Cylinder(Circle(Plane(a + ab * 0.5, ab.unitized()), radius), height)
    Artist(pipe).draw(color=Color.pink())

Artist.redraw()
