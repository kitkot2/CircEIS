from impedance.models.circuits import CustomCircuit
import matplotlib.pyplot as plt
from impedance.visualization import plot_nyquist

def circuit_fit(frequencies, Z):
    
    print('Enter your circuit: ')
    circuit = str(input())
    circuit = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
    
    print('Enter your initial guess: ')
    
    #Work in progress
    
    initial_guess = [.01, .01, 100, .01, .05, 100, 1]

    circuit = CustomCircuit(circuit, initial_guess=initial_guess)

    circuit.fit(frequencies, Z)

    print(circuit)

    circuit.plot(f_data=frequencies, Z_data=Z, kind='nyquist')

    plt.legend(['Data', 'Fit'])
    plt.show()