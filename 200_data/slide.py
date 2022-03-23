import compas

from compas.geometry import Point, Frame, Vector, Transformation
from compas.geometry import Polyline, NurbsCurve
from compas_view2.app import App

curve = NurbsCurve.from_points([Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)])
frames = [curve.frame_at(t) for t in curve.space(50)]
xforms = [Transformation.from_frame_to_frame(frames[0], frame) for frame in frames]

monkey = compas.json_load('monkey.json')
monkeyworld = Frame(Point(0, 0, 0), Vector(0, -1, 0), Vector(-1, 0, 0))

X = Transformation.from_frame_to_frame(monkeyworld, frames[0])

monkey.transform(X)

viewer = App(width=1600, height=900)
viewer.view.camera.position = Point(-10, 0, 2)
viewer.view.camera.target = Point(5, 0, 0)

viewer.add(Polyline(curve.locus()))

viewer.add(frames[0])

monkeyobj = viewer.add(monkey, opacity=1.0)

@viewer.on(interval=100, frames=len(frames), record=True, record_path='recording.gif')
def move(f):
   viewer.add(frames[f])
   monkeyobj.matrix = xforms[f].matrix
   monkeyobj.update()

viewer.show()
