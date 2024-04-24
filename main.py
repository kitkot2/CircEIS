import pandas as pd
from matplotlib import pyplot as p, cm, colors
from numpy import *

temperature = '120'
name = 'Ag3VO4-2-2M-'+temperature+'-3-Start1.csv'

data = pd.read_csv("data/"+name, delimiter=",")


Re = list(data['Re. Ом'])
Im = list(data['Im. Ом'])#Im
f = list(data['Частота. Гц'])

from functions import show

show.plot_data(Re,Im)
