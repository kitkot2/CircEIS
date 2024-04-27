import pandas as pd
from functions import circ_for_analysis, show, preparation, clean, fitting

#temperature = '105'
#file_name = 'Ag3VO4-2-2M-'+temperature+'-3-Start1'

print('Enter file name without .txt or .csv:')
file_name = input()

preparation.correct_path(file_name)
preparation.EIS_txt_to_csv(file_name)

f, Re, Im, Z = preparation.read_from_CSV(file_name)

show.plot_data(Re,Im)
Re, Im = clean.clean_hub(Re,Im)

print('Enter number of circumferences:')
circ_number = int(input())
data_for_fitting = circ_for_analysis.select_regions(Re, Im, circ_number)

circumferences_data = []

for elem in data_for_fitting:
    x, y, R = fitting.least_square_fitting(Re, Im, elem[0], elem[1])
    circumferences_data.append([x,y,R])

show.plot_data_with_circumferences(Re, Im, circumferences_data)

show.circuferences_p(circumferences_data)