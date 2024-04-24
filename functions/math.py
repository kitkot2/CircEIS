import math

def right_intersection_with_ox(xc, yc, R):
    if yc <= 0 and yc + R < 0: 
        return 0
    elif yc >= 0 and yc - R > 0:
        return 0
    else:
        right_intersection_x = xc + math.sqrt(R**2 - (yc)**2)
        return right_intersection_x