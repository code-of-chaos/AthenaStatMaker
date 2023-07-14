# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import attrs
import math

# Athena Packages
from AthenaColor import HtmlColorObjects as HCO

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@attrs.define(unsafe_hash=True, frozen=True)
class ChartRadialAxis:
    name:str = "undefined"
    value:float = 1
    color:tuple = HCO.WHITE
    pos:tuple = (0,0)

@attrs.define()
class ChartRadial:
    data:list[ChartRadialAxis] = attrs.field(factory=lambda: [ChartRadialAxis()])
    positions:dict[ChartRadialAxis, tuple[float,float]] = attrs.field(factory=dict)
    divisions:int = 4
    color:tuple = (*HCO.WHITE, 16)

    _divisions_radius:list[float] = attrs.field(init=False)
    def __attrs_post_init__(self):
        self._divisions_radius = []

    def calculate_positions(self) -> None:

        total_axis = len(self.data)

        for i, axis in enumerate(self.data):
            theta = math.radians(360/total_axis*i)

            # the "radius" of this formula is the val
            x = axis.value * math.cos(theta)
            y = axis.value * math.sin(theta)

            self.positions[axis] = x,y

        return
