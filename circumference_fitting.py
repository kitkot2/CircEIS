import pandas as pd
from functions import circ_for_analysis, show, fitting

def circumference_fit(Re, Im):
    
    print('Enter number of circumferences:')
    circ_number = int(input())
    data_for_fitting = circ_for_analysis.select_regions(Re, Im, circ_number)

    circumferences_data = []

    for elem in data_for_fitting:
        x, y, R = fitting.least_square_fitting(Re, Im, elem[0], elem[1])
        circumferences_data.append([x,y,R])

    show.plot_data_with_circumferences(Re, Im, circumferences_data)

    show.circuferences_p(circumferences_data)
