import numpy as np
from qiskit import QuantumCircuit, Aer,transpile
from qiskit.providers.aer import QasmSimulator
from qiskit_aer import AerSimulator

from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
from math import pi,cos,acos,radians
angle = float(input("Rotated Angle: "))
angle = radians(angle)
piVal = pi/angle

dsign = u'\N{DEGREE SIGN}'
#t = 3.9497074101334544 #15%
#t = 15.681708768975515 #1 %
#t = 1.0993051486313747 #98 %

#print("Rotated Angle: ", "{0:.3}\N{DEGREE SIGN}".format(a))
r = 1
h = r - r*cos(pi/piVal)
a = 2*pi*r*h 
s = 4*pi*r
p = a/s

print("\nExpected Measured probablity: ","{0:.3%}".format(p))

t = pi/acos(1-2*p)
#print("t: ",t)

wp = 1/t

#print("Expected Probability:",wp)#wanted prob
print("Expected Normalized Probability:","{0:.3%}".format(wp))#wanted prob

prob = []

prob.append(0)# zero prob
for i in range(1,100):
	prob.append( pi/acos(1-2*(i/100)) )
prob.append(pi)#100 %

d_prob = 15 #desired probability

SHOTS = 100000
q = 0
c = 0

simulator = AerSimulator(method='matrix_product_state')	
circuit = QuantumCircuit(1, 1)
circuit.u(pi/piVal,0,0,q)
circuit.measure(q,c)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=SHOTS)

result = job.result()

counts = result.get_counts(compiled_circuit)
print("Result: ",counts)

circuit.draw(output='mpl',filename='hello')

ap = counts[max(counts,key=counts.get)]/SHOTS

print("\nActual Measured Probability:","{0:.3%}".format(ap))

if ap != 0:
	t = pi/acos(1-2*ap)
#print("t: ",t)

rp = 1/t

print("Actual Normalized Probability:","{0:.3%}".format(rp))



print("Error Rate: ","{0:.3%}".format(abs(wp-rp)/rp))