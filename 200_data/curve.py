import os
import compas
import compas_rhino
from compas_rhino.conversions import RhinoCurve

FILE = os.path.join(os.path.expanduser('~'), 'Code', 'ArupMarch2022', 'data.json')

guid = compas_rhino.select_curve()

curve = RhinoCurve.from_guid(guid).to_compas()

data = compas.json_load(FILE)
data['']
