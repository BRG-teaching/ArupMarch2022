from compas.geometry import Pointcloud, Line, Point
from compas.datastructures import Network
from compas.utilities import pairwise
from compas.colors import Color
from compas_view2.app import App


cloud = Pointcloud.from_bounds(8, 5, 3, 83)
network = Network.from_pointcloud(cloud)

start, end = network.node_sample(size=2)
path = network.shortest_path(start, end)


viewer = App(width=1600, height=1000)
viewer.view.camera.target = cloud.centroid
viewer.view.camera.position = cloud.centroid + [0, -8, 1]

viewer.add(network)

for u, v in pairwise(path):
    a = network.node_coordinates(u)
    b = network.node_coordinates(v)
    viewer.add(Line(a, b), linewidth=20, color=Color.green())

viewer.add(Point(* network.node_coordinates(start)), size=30, color=Color.red())
viewer.add(Point(* network.node_coordinates(end)), size=30, color=Color.red())

viewer.show()