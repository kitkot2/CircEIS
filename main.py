import pandas as pd
from numpy import *
from functions import show, preparation


temperature = '105'
file_name = 'Ag3VO4-2-2M-'+temperature+'-3-Start1'


preparation.EIS_txt(file_name)

data = pd.read_csv("data/"+file_name+".csv", delimiter=",")
Re = list(data['Re. Ом'])
Im = list(data['Im. Ом'])
f = list(data['Частота. Гц'])


show.plot_data(Re,Im)