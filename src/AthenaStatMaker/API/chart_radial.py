# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import attrs
import math

# Athena Packages

# Local Imports
from AthenaStatMaker.math import calc_point_on_circle_edge

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@attrs.define(unsafe_hash=True, frozen=True)
class ChartRadialAxis:
    name:str = "undefined"
    short:str = "U"
    value:float = 0

@attrs.define()
class ChartRadial:
    data:list[ChartRadialAxis] = attrs.field(factory=lambda: [ChartRadialAxis()])
    positions:dict[ChartRadialAxis, tuple[float,float]] = attrs.field(factory=dict)
    divisions:int = 4
