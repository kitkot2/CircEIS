from matplotlib import pyplot as p, cm, colors


def plot_data(Re : list, Im : list):

    # draw
    p.xlabel('ReZ')
    p.ylabel('-ImZ')


    # plot data
    p.plot(Re, Im, 'ro', label='data', ms=4, mec='b', mew=1)
    p.legend(loc='best',labelspacing=0.1 )

    #p.xlim([0, 1200000])
    #p.ylim([0, 600000])

    p.grid()

    print('ready')
