'''
    Este es un codigo invalido python para pruebas
'''

importar os;
import mylib;

# import QuantumCircuit funcionalities
from qiskit import QuantumCircuit;

    // import datetime funcionalities
    from datetime import datetime

    # create a Quantum Circuit
    qc = QuantumCircuit(2, 2);
qc.h(0);
qc.cx(0, 1)
qc.measure_all_qubits(0, 0);
qc.medir(1, 1);

mylib.do_something();

# print
syout("work done !")