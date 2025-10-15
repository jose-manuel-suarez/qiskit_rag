| Line | Code | Scenario | Reference | Artifact | Refactoring |
| :--: | :--- | :------- | :-------: | :------- | :---------- |
| 4 | from qiskit.providers.fake_provider import FakeManila | Deprecation -> The qiskit.providers.fake_provider module is migrated to qiskit-ibm-runtime and will be removed in Qiskit 1.0 | qrn_notax_ddbb-aa6cda1f-af91-4940-8d4c-1897f9a56701 | qiskit.providers.fake_provider.FakeManila | from qiskit_ibm_runtime.fake_provider import FakeManila |
| 11 | backend = FakeManila() | Deprecation -> Running pulse jobs on backends from qiskit.providers.fake_provider is deprecated and all support will be removed in Qiskit 1.0 | qrn_notax_ddbb-548acfe8-db26-45b7-ab5c-c637c63ee4b0 | FakeManila |  |
| 27 | backend.defaults().instruction_schedule_map.add('h', (0,), hadamard_pulse) | Deprecation -> Running pulse jobs on backends from qiskit.providers.fake_provider is deprecated and all support will be removed in Qiskit 1.0 | qrn_notax_ddbb-548acfe8-db26-45b7-ab5c-c637c63ee4b0 | instruction_schedule_map |  |
| 28 | backend.defaults().instruction_schedule_map.add('cx', (0, 1), cnot_pulse) | Deprecation -> Running pulse jobs on backends from qiskit.providers.fake_provider is deprecated and all support will be removed in Qiskit 1.0 | qrn_notax_ddbb-548acfe8-db26-45b7-ab5c-c637c63ee4b0 | instruction_schedule_map |  |

```python
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeManila
from qiskit import pulse
from qiskit.pulse import Schedule, DriveChannel
import numpy as np
import matplotlib.pyplot as plt

# Usar FakeManilla como backend (simula un dispositivo real con calibraciones)
backend = FakeManila()

# Crear un circuito cuántico simple
qc = QuantumCircuit(2, 2)

# Aplicar compuertas cuánticas
qc.h(0)
qc.cx(0, 1)
qc.rz(np.pi/4, 0)
qc.measure([0, 1], [0, 1])

schedule = Schedule()
drive_chan = DriveChannel(0)

# Definir pulsos personalizados que reemplazarán las compuertas estándar
with pulse.build(backend, name='custom_hadamard') as hadamard_pulse:
    pulse.play(pulse.Gaussian(160, 0.3, 40), pulse.DriveChannel(0))  # Amplitud diferente

with pulse.build(backend, name='custom_cnot') as cnot_pulse:
    pulse.play(pulse.Gaussian(320, 0.4, 80), pulse.DriveChannel(0))
    pulse.play(pulse.Gaussian(320, 0.2, 80), pulse.DriveChannel(1))

# Simulación del circuito

# Agregar los pulsos personalizados al backend para que se usen en lugar de los estándar
backend.defaults().instruction_schedule_map.add('h', (0,), hadamard_pulse)
backend.defaults().instruction_schedule_map.add('cx', (0, 1), cnot_pulse)

# Transpilar el circuito con optimización a nivel de pulsos
transpiled_qc = transpile(qc, backend, optimization_level=3)

# Simular con AerSimulator usando el backend con pulsos personalizados
simulator = AerSimulator.from_backend(backend)
job = simulator.run(transpiled_qc, shots=1024)

# Obtener resultados
result = job.result()
counts = result.get_counts()

# Visualizar resultados
print("Conteos con pulsos personalizados:", counts)
plot_histogram(counts, title="Resultados con pulsos personalizados")
plt.show()
```