# VS Code smoke test for the generated AlibreScript IDE stubs.
# This file is for editor/runtime checking outside Alibre Design.

from __future__ import print_function

import os
import sys
from math import cos, radians, sin

StubPackage = os.path.join(
    os.path.dirname(__file__),
    'Alibre-Script-Stub-Files',
    'generated',
    'package'
)

if os.path.isdir(StubPackage) and StubPackage not in sys.path:
    sys.path.insert(0, StubPackage)

from AlibreScript import (
    CurrentAssemblies,
    CurrentAssembly,
    CurrentPart,
    CurrentParts,
    ScriptFileName,
    ScriptFolder,
)

def create_two_angle_fixture_references():
    p = CurrentPart()

    angle16 = 16.0
    angle30 = -30.0
    axis_length = 100.0

    xy_plane = p.GetPlane('XY-Plane')
    yz_plane = p.GetPlane('YZ-Plane')
    x_axis = p.GetAxis('X-Axis')

    plane16 = p.AddPlane('16 degree', xy_plane, x_axis, angle16)

    angle16_rad = radians(angle16)
    axis_start = [0.0, 0.0, 0.0]
    axis_end = [
        0.0,
        -sin(angle16_rad) * axis_length,
        cos(angle16_rad) * axis_length
    ]
    axis2 = p.AddAxis('Axis<2>', axis_start, axis_end)

    plane30 = p.AddPlane('30 degree', yz_plane, axis2, angle30)

    return p, plane16, axis2, plane30

if __name__ == '__main__':
    part, plane16, axis2, plane30 = create_two_angle_fixture_references()
    assembly = CurrentAssembly()
    parts = CurrentParts()
    assemblies = CurrentAssemblies()
    print('AlibreScript stub smoke test complete.')
    print('ScriptFileName mock:', repr(ScriptFileName))
    print('ScriptFolder mock:', repr(ScriptFolder))
    print('CurrentPart mock type:', type(part).__name__)
    print('CurrentAssembly mock type:', type(assembly).__name__)
    print('CurrentParts first mock type:', type(parts[0]).__name__)
    print('CurrentAssemblies first mock type:', type(assemblies[0]).__name__)
