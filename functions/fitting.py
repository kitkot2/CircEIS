import numpy as np
from scipy import optimize
from functions import preparation

def least_square_fitting(Re : list, Im : list, x_left, x_right):
    X, Y = preparation.data_slicing(Re, Im, x_left, x_right)
    x_m = np.mean(X)
    y_m = np.mean(Y)

    def calc_R1(xc, yc):
        return np.sqrt((X-xc)**2 + (Y-yc)**2)

    def f_1(c):
        Ri = calc_R1(*c)
        return Ri - Ri.mean()

    center_estimate = x_m, y_m
    center_1, ier = optimize.leastsq(f_1, center_estimate)

    xc_1, yc_1 = center_1
    Ri_1       = calc_R1(*center_1)
    R_1        = Ri_1.mean()
    residu_1   = sum((Ri_1 - R_1)**2)
    return xc_1, yc_1, R_1