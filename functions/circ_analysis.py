import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

def select_regions(x, y, num_of_circ):
    # Plotting
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(x, y, 'ro', label='data', ms=4, mec='b', mew=1)
    ax.set_xlim()
    ax.set_xlabel('ReZ')
    ax.set_ylabel('-ImZ')
    
    size=(10,5)
    plt.gcf().set_size_inches(size)
    ax.grid()

    # Variables to store the selected region
    x_left = None
    x_right = None
    boundaries = []
    opened = True  # Flag to track if the plot is open

    # Cursor
    cursor = Cursor(ax, horizOn=False, vertOn=True, useblit=True, color='r', linewidth=1)

    # Function to handle mouse clicks
    def onclick(event):
        nonlocal x_left, x_right, boundaries, opened, size
        if event.inaxes is not None:
            if opened:
                if len(boundaries) < num_of_circ:
                    if x_left is None:
                        x_left = event.xdata
                        #print(f'Left boundary: {x_left}')
                        ax.axvline(x_left, color='red', linestyle='--')
                        plt.draw()
                    else:
                        x_right = event.xdata
                        #print(f'Right boundary: {x_right}')
                        # Plot the selected region
                        ax.axvline(x_right, color='red', linestyle='--')
                        ax.axvspan(float(x_left), float(x_right), color='red', alpha=0.3, clip_on=False)
                        plt.draw()

                        # Saving boundaries
                        boundaries.append((float(x_left), float(x_right)))

                        # Reset boundaries for further selections
                        x_left = None
                        x_right = None

                        if len(boundaries) == num_of_circ:
                            opened = False
            else:
                plt.close()

    # Connect the mouse click event
    fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()

    #print("Selected boundaries:")
    #print(boundaries)
    return boundaries