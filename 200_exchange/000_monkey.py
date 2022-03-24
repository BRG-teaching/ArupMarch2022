import os
import compas
from compas_blender.conversions import BlenderMesh
from compas.artists import Artist


FILE = os.path.join(os.path.expanduser('~'), 'Code', 'ArupMarch2022', '200_exchange', 'data.json')


mesh = BlenderMesh.from_monkey().to_compas()
mesh = mesh.subdivide(k=1)


data = {'monkey': mesh}
compas.json_dump(data, FILE)


Artist.clear()
artist = Artist(mesh)
artist.draw()
