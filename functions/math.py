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
    
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def get_CPE_alpha(xc, yc, left_intersection):
    angle = getAngle((xc, yc),(left_intersection, 0),(xc,0))
    
    # angle = 0 => alpha = 1
    # angle = 45 => alpha = 0.5
    # angle = 90 => alpha = 0
    
    if angle < 0 or angle > 90:
        return None
    else:
        alpha = 1 - (angle/90)
        return alpha