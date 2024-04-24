import pandas as pd
from numpy import *

temperature = '120'
file_name = 'Ag3VO4-2-2M-'+temperature+'-3-Start1 copy'

from functions import preparation

preparation.EIS_txt(file_name)

data = pd.read_csv("data/"+file_name+".csv", delimiter=",")
Re = list(data['Re. Ом'])
Im = list(data['Im. Ом'])#Im
f = list(data['Частота. Гц'])

from functions import show

show.plot_data(Re,Im)
