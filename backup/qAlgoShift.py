from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator

r0 = 0
r1 = 1
r2 = 2


inA0 = 0
inA1 = 1
inA2 = 2

inB0 = 3
inB1 = 4
inB2 = 5

v0 = 6
v1 = 7
v2 = 8

dmy0 = 9
dmy1 = 10

inputA = int(input("inputA(0-7):"))
inputB = int(input("inputB(0-7):"))

for x in range(1):

	simulator = QasmSimulator()

	circuit = QuantumCircuit(11, 3)

	if(inputA & 0b1 != 0):circuit.x(inA0)
	if(inputA & 0b10 != 0):circuit.x(inA1)
	if(inputA & 0b100 != 0):circuit.x(inA2)

	if(inputB & 0b1 != 0):circuit.x(inB0)
	if(inputB & 0b10 != 0):circuit.x(inB1)
	if(inputB & 0b100 != 0):circuit.x(inB2)

	circuit.cx(inA0,v0)
	circuit.cx(inA1,v1)
	circuit.cx(inA2,v2)


	circuit.x(inB0)
	circuit.x(inB1)
	circuit.x(inB2)

	circuit.mcx([inB2,inB1,inB0],dmy0)
	circuit.cswap(dmy0,v2,dmy1)
	circuit.cswap(dmy0,v1,v2)
	circuit.cswap(dmy0,v0,v1)
	circuit.mcx([inB2,inB1,inB0],dmy0)

	circuit.x(inB0)
	circuit.x(inB1)
	circuit.x(inB2)

	#----------------------------

	circuit.x(inB1)
	circuit.x(inB2)

	circuit.mcx([inB2,inB1,inB0],dmy0)
	circuit.cswap(dmy0,v0,dmy1)
	circuit.cswap(dmy0,v1,v0)
	circuit.cswap(dmy0,v2,v1)
	circuit.mcx([inB2,inB1,inB0],dmy0)

	circuit.x(inB1)
	circuit.x(inB2)
	
	circuit.measure(v0,r0)
	circuit.measure(v1,r1)
	circuit.measure(v2,r2)
	
	compiled_circuit = transpile(circuit, simulator)

	job = simulator.run(compiled_circuit, shots=1)

	result = job.result()

	counts = result.get_counts(compiled_circuit)
	for val in counts:
		pass
	print(val)


result = int(val[2]) + int(val[1])*2 + int(val[0])*4

print(result)
