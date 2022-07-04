import numpy as np
import pandas as pd
from utils import *

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def curve_by_deflection(origin=False, TP1=False, intersection_angle_radians=False, R=False, azimuth_IPtoOrigin=False, chainage_increment=5, n_points=10, angle_output='DMS'):
    if origin and TP1 and intersection_angle_radians:
        R = horizontal_distance(origin, TP1)
        total_arc_length = R * intersection_angle_radians
        azimuth_TP1toOrigin = np.arctan2(origin[0] - TP1[0], origin[1] - TP1[1]) % (2 * np.pi)
    else:
        print('Cannot create curve with these inputs!')
        return False

    curve_points = pd.DataFrame(columns=['Chainage', 'Arc_Distance', 'Deflection_Angle', 'Chord_Distance', 'Azimuth', 'Easting', 'Northing'])

    arc_distances = [(n * chainage_increment) for n in range(n_points)] + [total_arc_length]

    for arc_distance in arc_distances:
        deflection_angle_radians = (arc_distance / (2 * R))
        deflection_angle_degrees = deflection_angle_radians * (180 / np.pi)

        azimuth = azimuth_TP1toOrigin + deflection_angle_radians - (np.pi / 2)
        chord_distance = (2 * R) * np.sin(deflection_angle_radians)

        easting = TP1[0] + (chord_distance * np.sin(azimuth))
        northing = TP1[1] + (chord_distance * np.cos(azimuth))

        if angle_output == 'D':
            display_angle = deflection_angle_degrees
            display_azimuth = azimuth * (180/np.pi)
        elif angle_output == 'R':
            display_angle == deflection_angle_radians
            display_azimuth = azimuth
        elif angle_output == 'DMS':
            display_angle = decdeg2dms_string(deflection_angle_degrees)
            display_azimuth = decdeg2dms_string(azimuth * (180/np.pi))

        row = [arc_distance, arc_distance, display_angle, chord_distance, display_azimuth, easting, northing]
        curve_points.loc[len(curve_points)] = row

    curve_points = curve_points.round(3)
    return curve_points


test = 'a'

if test == 'a':
    R = 30
    TP1 = (379071.331, 6360472.938)
    origin = (379066.73, 6360443.293)
    intersection_angle_radians = 89.18 * (np.pi/180)

    x = curve_by_deflection(origin, TP1, intersection_angle_radians, 5, 10)

print(x)