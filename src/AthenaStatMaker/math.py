# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import math

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def calc_point_on_circle_edge(origin_x:float, origin_y:float, radius:float, angle:float) -> tuple[float,float]:
    theta = math.radians(angle)

    # the "radius" of this formula is the val
    x = origin_x + (radius * math.cos(theta))
    y = origin_y + (radius * math.sin(theta))

    return x, y

def calc_rounded_corners(polygon:list[tuple[float, float]]) -> list[tuple[float, float]]:
    num_points = len(polygon) // 2

    for i in range(num_points):
        start_index = 2 * i
        end_index = (2 * i + 2) % len(polygon)
        next_index = (2 * i + 4) % len(polygon)

        start_point = complex(polygon[start_index], polygon[start_index + 1])
        end_point = complex(polygon[end_index], polygon[end_index + 1])
        next_point = complex(polygon[next_index], polygon[next_index + 1])

        direction1 = (start_point - end_point) / abs(start_point - end_point)
        direction2 = (next_point - end_point) / abs(next_point - end_point)

        control_point1 = end_point + (direction1 * radius)
        control_point2 = end_point + (direction2 * radius)



        path = ET.SubElement(root, "path")
        path.set("d",
                 f"M {control_point1.real},{control_point1.imag} C {end_point.real},{end_point.imag} {end_point.real},{end_point.imag} {control_point2.real},{control_point2.imag} Z")
        path.set("fill", "none")
        path.set("stroke", "black")