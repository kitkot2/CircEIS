from functions import show
from scipy.signal import lfilter

def simple(Re: list, Im : list):
    x, y=[], []
    ReM = 0
    for i in range(len(Re)):
        if (Re[i] > 0 and Im[i] > 0) and (abs(Im[i] - Im[i-1]) < 100000) and (abs(Re[i] - Re[i-1]) < 100000) and (ReM < Re[i]):
            x.append(Re[i])
            y.append(Im[i])
            ReM = Re[i]
    
    print('Cleaned_data:')
    show.plot_data(x,y)
    return x, y

# Not working
def lfilter_scipy(x: list, y : list):
    n = 10  # the larger n is, the smoother curve will be
    b = [1.0 / n] * n
    a = 1
    yy = lfilter(b, a, y)
    print('Cleaned_data:')
    show.plot_data(x,yy)
    return x, yy

def clean_hub(Re: list, Im : list):
    print('To clean data enter 1, else enter 0')
    fl = int(input())
    if fl == 1:
        return simple(Re, Im)
    elif fl == 2:
        return lfilter_scipy(Re, Im)
    else:
        return Re, Im