from matplotlib import pyplot as plt
import numpy as np
from math import pi

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
    

def plot_circumference(x,y,R,i, theta_fit):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # список цветов
    color_index = i % len(colors)  # выбор цвета в зависимости от значения i

    x_fit = x + R*np.cos(theta_fit)
    y_fit = y + R*np.sin(theta_fit)
    
    plt.plot(x_fit, y_fit, color=colors[color_index], linestyle='--', label='Окружность №'+str(i+1), lw=1)
    plt.plot([x], [y], 'kD', mec='r', mew=1) 



def plot_data_with_circumferences(Re : list, Im : list, circ_data : list):
    plt.xlabel('ReZ')
    plt.ylabel('-ImZ')

    # plot data
    plt.plot(Re, Im, 'ro', label='data', ms=4, mec='b', mew=1)
    
    theta_fit = np.linspace(-pi, pi, 180)
    i = 0
    for elem in circ_data:
        plot_circumference(elem[0], elem[1], elem[2], i, theta_fit)
        i+=1
    
    plt.legend(loc='best',labelspacing=0.1 )
    
    plt.tight_layout()
    plt.axis('equal')
    plt.grid()
    plt.show()