"""
Code for Ramsey Circuit simulation using Qiskit
Homework 2
Author: Rohan Singh
"""

# imports
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from numpy import pi

# setting up the circuit
qreg_q = QuantumRegister(1, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# adding the gates to the circuit (using T^4)
circuit.reset(qreg_q[0])
circuit.h(qreg_q[0])
circuit.t(qreg_q[0])
circuit.t(qreg_q[0])
circuit.t(qreg_q[0])
circuit.t(qreg_q[0])
circuit.h(qreg_q[0])

# measuring the circuit
circuit.measure(qreg_q[0], creg_c[0])

# executing the circuit
backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend, shots=8192)
result = job.result()

# getting the measurement value
counts = result.get_counts(circuit)
print("Measurement result:", counts)
