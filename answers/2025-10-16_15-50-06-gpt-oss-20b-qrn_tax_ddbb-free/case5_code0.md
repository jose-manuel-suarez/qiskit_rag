| Line | Code | Scenario | Reference | Artifact | Refactoring |
| :--: | :--- | :------- | :-------: | :------- | :---------- |
| 2 | `from qiskit.extensions import HGate, XGate, Initialize` | Deprecation -> imports from qiskit.extensions are deprecated | IK | qiskit.extensions | `from qiskit.circuit.library.standard_gates import HGate, XGate\nfrom qiskit.circuit.library import Initialize` |
| 3 | `from qiskit.extensions import Barrier` | Deprecation -> imports from qiskit.extensions are deprecated | IK | qiskit.extensions | `from qiskit.circuit import Barrier` |
| 4 | `from qiskit.extensions import UnitaryGate` | Deprecation -> imports from qiskit.extensions are deprecated | IK | qiskit.extensions | `from qiskit.circuit.library import UnitaryGate` |

```python
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate, XGate
from qiskit.circuit.library import Initialize, UnitaryGate
from qiskit.circuit import Barrier
import numpy as np

qr = QuantumRegister(3)
qc = QuantumCircuit(qr)

qc.append(HGate(), [qr[0]])
qc.append(XGate(), [qr[1]])

custom_matrix = np.array([[0, 1], [1, 0]])
custom_gate = UnitaryGate(custom_matrix, label="Custom")
qc.append(custom_gate, [qr[2]])

psi = [1/np.sqrt(2), 1/np.sqrt(2)]
init_gate = Initialize(psi)
qc.append(init_gate, [qr[0]])

qc.append(Barrier(3), [qr[0], qr[1], qr[2]])
print(qc.draw())
```