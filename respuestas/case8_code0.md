| Line | Code | Scenario Id | Scenario | Artifact | Refactoring |
| :-: | :- | :-: | :- | :- | :- |
| 2 | `from qiskit.utils import QuantumInstance, algorithm_globals` | * | Deprecation -> `QuantumInstance` class deprecated | qiskit.utils.QuantumInstance | `from qiskit.primitives import Estimator` |
| 2 | `from qiskit.utils import QuantumInstance, algorithm_globals` | * | Deprecation -> `algorithm_globals` deprecated, replace with `numpy.random` and explicit seeds | qiskit.utils.algorithm_globals | |
| 4 | `from qiskit.opflow import Z, I, X` | * | Deprecation -> `qiskit.opflow` module deprecated | qiskit.opflow | `from qiskit.quantum_info import SparsePauliOp` |
| 7 | `hamiltonian = (Z ^ I) + (X ^ X)` | * | Deprecation -> `opflow` operators and classes deprecated | qiskit.opflow.Z | `hamiltonian = SparsePauliOp.from_list([('ZI', 1), ('XX', 1)])` |
| 7 | `hamiltonian = (Z ^ I) + (X ^ X)` | * | Deprecation -> `opflow` operators and classes deprecated | qiskit.opflow.I | `hamiltonian = SparsePauliOp.from_list([('ZI', 1), ('XX', 1)])` |
| 7 | `hamiltonian = (Z ^ I) + (X ^ X)` | * | Deprecation -> `opflow` operators and classes deprecated | qiskit.opflow.X | `hamiltonian = SparsePauliOp.from_list([('ZI', 1), ('XX', 1)])` |
| 10 | `initial_point = algorithm_globals.random.random(ansatz.num_parameters)` | * | Deprecation -> `algorithm_globals.random` deprecated, use `numpy.random` | qiskit.utils.algorithm_globals.random | `rng = np.random.default_rng(seed=1234); initial_point = rng.random(ansatz.num_parameters)` |
| 13 | `quantum_instance = QuantumInstance(` | * | Deprecation -> `QuantumInstance` class deprecated, use `Estimator` | qiskit.utils.QuantumInstance | `estimator = Estimator(` |
| 16 | `seed_simulator=algorithm_globals.random_seed,` | * | Deprecation -> `algorithm_globals.random_seed` deprecated, define seed explicitly | qiskit.utils.algorithm_globals.random_seed | `seed_simulator=1234,` |
| 17 | `seed_transpiler=algorithm_globals.random_seed` | * | Deprecation -> `algorithm_globals.random_seed` deprecated, define seed explicitly | qiskit.utils.algorithm_globals.random_seed | `seed_transpiler=1234` |