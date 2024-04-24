
def simple(Re: list, Im : list):
    x, y=[], []
    ReM = 0
    for i in range(len(Re)):
        if (Re[i] > 0 and Im[i] > 0) and (abs(Im[i] - Im[i-1]) < 100000) and (abs(Re[i] - Re[i-1]) < 100000) and (ReM < Re[i]):
            x.append(Re[i])
            y.append(Im[i])
            ReM = Re[i]
    return x, y

def clean_hub(Re: list, Im : list):
    print('To clean data enter 1, else enter 0')
    if int(input()):
        return simple(Re, Im)
    else:
        return Re, Im
