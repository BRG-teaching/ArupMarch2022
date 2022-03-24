import os
import compas
from compas.geometry import Point, Frame, Vector, Transformation
from compas.geometry import Polyline
from compas_view2.app import App


FILE = os.path.join(os.path.dirname(__file__), 'data.json')


data = compas.json_load(FILE)
curve = data['curve']
monkey = data['monkey']


frames = [curve.frame_at(t) for t in curve.space(50)]
xforms = [Transformation.from_frame_to_frame(frames[0], frame) for frame in frames]

monkeyworld = Frame.worldXY()

X = Transformation.from_frame_to_frame(monkeyworld, frames[0])
monkey.transform(X)


viewer = App(width=1600, height=900)
viewer.view.camera.position = Point(25, 0, 5)
viewer.view.camera.target = Point(5, 0, 0)

viewer.add(Polyline(curve.locus()))
viewer.add(frames[0])

monkeyobj = viewer.add(monkey, opacity=1.0)

viewer.show()
