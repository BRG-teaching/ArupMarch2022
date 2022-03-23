from math import radians

from compas.geometry import Pointcloud, Box, Polygon
from compas.geometry import Translation, Rotation
from compas.colors import Color

from compas_view2.app import App

cloud = Pointcloud.from_bounds(8, 5, 3, 1000)
box = Box.from_width_height_depth(1, 1, 1)

T = Translation.from_vector(cloud.centroid)
R = Rotation.from_axis_and_angle([0, 0, 1], radians(30))

box.transform(T * R)

viewer = App(width=1600, height=1000)
viewer.view.camera.target = cloud.centroid
viewer.view.camera.position = cloud.centroid + [0, -8, 1]

viewer.add(box, show_faces=False, opacity=0.3)
viewer.add(Polygon([box.points[index] for index in box.back]))
viewer.add(Polygon([box.points[index] for index in box.right]))
viewer.add(Polygon([box.points[index] for index in box.bottom]))

for point in cloud:
    color = Color.from_hex('#0092d2')
    size = 10

    if box.contains(point):
        color = Color.pink()
        size = 20

    viewer.add(point, color=color, size=size)

viewer.show()
