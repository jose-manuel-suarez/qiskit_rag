| Line | Code | Scenario | Reference | Artifact | Refactoring |
| :--: | :--- | :------- | :-------: | :------- | :---------- |
| 2 | `from qiskit.extensions import UnitaryGate` | Deprecation -> UnitaryGate moved to qiskit.circuit.library | qrn_tax_ddbb--0ef4f925-2e1f-4821-a64d-9edcfaacc1c0 | qiskit.extensions | `from qiskit.circuit.library import UnitaryGate` |
| 3 | `from qiskit.extensions.exceptions import ExtensionError` | Deprecation -> ExtensionError moved to qiskit.exceptions | qrn_tax_ddbb--0ef4f925-2e1f-4821-a64d-9edcfaacc1c0 | qiskit.extensions.exceptions | `from qiskit.exceptions import ExtensionError` |

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.exceptions import ExtensionError
import numpy as np

def apply_custom_gate(qc, matrix, qubit):
    try:
        if matrix.shape[0] != matrix.shape[1]:
            raise ExtensionError("La matriz debe ser cuadrada")
        custom_gate = UnitaryGate(matrix)
        qc.append(custom_gate, [qubit])
    except ExtensionError as e:
        print(f"Error en extensión: {e}")

qc = QuantumCircuit(1)

print("\nMatriz no cuadrada...")
apply_custom_gate(qc, np.array([[1, 0, 0], [0, 1, 0]]), 0)
```