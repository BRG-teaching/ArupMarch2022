import compas
from compas.datastructures import Mesh
from compas.geometry import Point, Plane, Circle
from compas.geometry import Cylinder
from compas.artists import Artist
from compas.colors import Color


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))


start = 123, 68
loop = mesh.edge_loop(start)

edge_color = {}
for u, v in loop:
    edge_color[u, v] = Color.pink()

face_color = {}
for u, v in loop[::2]:
    for u, v in mesh.halfedge_strip((u, v)):
        face = mesh.halfedge_face(u, v)
        if face is not None:
            face_color[face] = Color.pink().lightened(50)
for u, v in loop[1::2]:
    for u, v in mesh.halfedge_strip((v, u)):
        face = mesh.halfedge_face(u, v)
        if face is not None:
            face_color[face] = Color.pink().darkened(50)


Artist.clear()

artist = Artist(mesh)

artist.draw_faces(color=face_color)

for u, v in loop:
    a = Point(* mesh.vertex_coordinates(u))
    b = Point(* mesh.vertex_coordinates(v))
    ab = b - a
    radius = 0.05
    height = ab.length
    pipe = Cylinder(Circle(Plane(a + ab * 0.5, ab.unitized()), radius), height)
    Artist(pipe).draw(color=edge_color[u, v])

Artist.redraw()
