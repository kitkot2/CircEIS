import pandas as pd
from numpy import *
from functions import show, preparation, clean


temperature = '105'
file_name = 'Ag3VO4-2-2M-'+temperature+'-3-Start1'

preparation.correct_path(file_name)
preparation.EIS_txt(file_name)

data = pd.read_csv("data/"+file_name+".csv", delimiter=",")
Re = list(data['Re. Ом'])
Im = list(data['Im. Ом'])
f = list(data['Частота. Гц'])

show.plot_data(Re,Im)
Re, Im = clean.clean_hub(Re,Im)
print('Cleaned data:')
show.plot_data(Re,Im)

print('Enter number of circumferences:')
circ_number = int(input())
circ_data = []

for i in range(circ_number):
    print('Choose data for '+str(i+1)+'-th circumference:')