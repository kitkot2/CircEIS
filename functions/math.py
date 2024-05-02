import math

def intersections_with_ox(xc, yc, R):
    if yc <= 0 and yc + R < 0: 
        return 0, 0
    elif yc >= 0 and yc - R > 0:
        return 0, 0
    else:
        right_intersection_x = xc + math.sqrt(R**2 - (yc)**2)
        left_intersection_x = xc - math.sqrt(R**2 - (yc)**2)
        return left_intersection_x, right_intersection_x