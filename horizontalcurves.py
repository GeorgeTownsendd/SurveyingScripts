import numpy as np
import pandas as pd


def curve_by_deflection(R, TP1, chainage_increment, n_points, chainage_start=0, curve_direction='clockwise',angle_output='D', precision=3):
    curve_points = pd.DataFrame(columns=['Chainage', 'Arc_Distance', 'Angle', 'Distance', 'Easting', 'Northing'])

    for chainage in range(chainage_start, chainage_start + (chainage_increment * (n_points+1)), chainage_increment):
        angle_radians = (chainage / (2 * R))
        angle_degrees = angle_radians * (180 / np.pi)
        distance = (2 * R) * np.sin(angle_radians)

        easting = TP1[0] + (distance * np.cos(angle_radians))
        northing = TP1[1] - (distance * np.sin(angle_radians)) if curve_direction == 'clockwise' else TP1[1] + (distance * np.sin(angle_radians))

        row = [chainage, chainage-chainage_start, angle_degrees if angle_output == 'D' else angle_radians, distance, easting, northing]
        curve_points.loc[len(curve_points)] = row

    curve_points = curve_points.round(3)
    return curve_points

R = 30
TP1 = (379071.331, 6360472.938)

x = curve_by_deflection(R, TP1, 5, 10, chainage_start=345)