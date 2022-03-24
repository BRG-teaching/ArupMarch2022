import os
import compas
import compas_rhino
from compas_rhino.conversions import RhinoCurve


FILE = os.path.join(os.path.dirname(__file__), 'data.json')


guid = compas_rhino.select_curve()
curve = RhinoCurve.from_guid(guid).to_compas()


data = compas.json_load(FILE)
data['curve'] = curve

compas.json_dump(data, FILE)
