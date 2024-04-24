from matplotlib import pyplot as plt


def plot_data(Re : list, Im : list):
    # draw
    plt.xlabel('ReZ')
    plt.ylabel('-ImZ')

    
    # plot data
    plt.plot(Re, Im, 'ro', label='data', ms=4, mec='b', mew=1)
    plt.legend(loc='best',labelspacing=0.1 )
    size=(10,5)
    plt.gcf().set_size_inches(size)

    plt.grid()
    
    def close_plot(event):
        if event.inaxes is not None:
            plt.close()

    # Connect the mouse click event
    plt.gcf().canvas.mpl_connect('button_press_event', close_plot)

    plt.show()