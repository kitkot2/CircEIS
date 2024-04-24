from matplotlib import pyplot as plt


def plot_data(Re : list, Im : list):
    # draw
    plt.xlabel('ReZ')
    plt.ylabel('-ImZ')


    # plot data
    plt.plot(Re, Im, 'ro', label='data', ms=4, mec='b', mew=1)
    plt.legend(loc='best',labelspacing=0.1 )
    size=(6,3)
    plt.gcf().set_size_inches(size)

    plt.grid()