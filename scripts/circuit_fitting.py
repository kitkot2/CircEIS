import impedance.models.circuits as circuits
import matplotlib.pyplot as plt
from impedance.visualization import plot_nyquist

#Work in progress
def circuit_fit(frequencies, Z):
    
    print('Enter your circuit name: ')
    circuit_name = str(input())
    
    # loading from circuits
    circuit = circuits.CustomCircuit()
    circuit.load(f'circuits/{circuit_name}.json')

    # Fitting
    circuit.fit(frequencies, Z)
    # For better fit attemp 
    # circuit.fit(frequencies, Z, circuit, global_opt=True)
    
    
    # Fitted circuit info
    print(circuit)

    # circuit.plot(f_data=frequencies, Z_data=Z)
    
    circuit.plot(f_data=frequencies, Z_data=Z, kind='nyquist')
    plt.show()
    
    circuit.plot(f_data=frequencies, Z_data=Z, kind='bode')
    plt.show()
    # plt.legend(['Data', 'Fit'])
    