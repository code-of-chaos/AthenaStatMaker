# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import enum
import attrs
import math

# Athena Packages
from AthenaColor import ForeNest as Fore

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
data:dict = {
    "stat1": 1,
    "stat2": 2,
    "stat3": 0
}

class DisplayType(enum.StrEnum):
    CONSOLE: enum.auto
    RADIAL:enum.auto

def render_console_bar_length(val:int, name:str, size_bar:int=16) -> str:
    # stupid and simple
    return f"{name} : {Fore.Red('❚'*val)}{Fore.DimGray('❚'*(size_bar-val))}"

@attrs.define
class RadialChart:
    total_axis:int
    center:tuple[float, float] = (0,0)
    data:dict = attrs.field(factory=dict)

    def calculate_pos(self, axis:int, val:float|int) -> tuple[float, float]:
        theta = math.radians(360/self.total_axis)*axis
        # the "radius" of this formula is the val
        x = self.center[0] + (val * math.cos(theta))
        y = self.center[1] + (val * math.sin(theta))
        return x,y

def api(display_type:DisplayType, input_data:dict):
    if display_type is DisplayType.CONSOLE:
        rendered_lines = []
        for stat_name, stat_val in input_data.items():
            stat_rendered:str = render_console_bar_length(val=stat_val, name=stat_name, size_bar=16)
            rendered_lines.append(stat_rendered)
            return # done with application

    elif display_type is DisplayType.RADIAL:
        radial_chart = RadialChart(total_axis = len(input_data))

        for i, (stat_name, stat_val) in enumerate(input_data.items()):
            pos:tuple[float, float] = radial_chart.calculate_pos(axis=i, val=stat_val)
            radial_chart.data[stat_name] = pos # can be done in one go

        return radial_chart


def gui():
    # create gui etc..
    # dpg should be setup correctly

    data_prepared = api(display_type=DisplayType.RADIAL, input_data=data)
    dpg.plot.something(data_prepared)




