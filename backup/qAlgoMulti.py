from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit import QuantumRegister, ClassicalRegister

r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

inA0 = 0
inA1 = 1
inA2 = 2

inB0 = 3
inB1 = 4
inB2 = 5

v0 = 6
v1 = 7
v2 = 8
v3 = 9
v4 = 10
v5 = 11

inputA = int(input("inputA(0-7):"))
inputB = int(input("inputB(0-7):"))

for x in range(1):

	simulator = QasmSimulator()

	circuit = QuantumCircuit()

	qr = QuantumRegister(1,'inA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'inA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'inA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'inB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'inB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'inB2')
	circuit.add_register( qr )


	qr = QuantumRegister(1,'v0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'v1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'v2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'v3')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'v4')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'v5')
	circuit.add_register( qr )
	
	cr = ClassicalRegister(6,'cr0')
	circuit.add_register( cr )

	if(inputA & 0b1 != 0):circuit.x(inA0)
	if(inputA & 0b10 != 0):circuit.x(inA1)
	if(inputA & 0b100 != 0):circuit.x(inA2)

	if(inputB & 0b1 != 0):circuit.x(inB0)
	if(inputB & 0b10 != 0):circuit.x(inB1)
	if(inputB & 0b100 != 0):circuit.x(inB2)

	#v0
	circuit.mcx([inA0,inB0], v0)

	#v1
	circuit.mcx([inA1,inB0], v1)
	circuit.mcx([inA0,inB1], v1)

	#v2
	circuit.mcx([inA1,inB0,inA0,inB1], v2)
	circuit.mcx([inA2,inB0], v2)
	circuit.mcx([inA1,inB1], v2)
	circuit.mcx([inA0,inB2], v2)

	#v3
	circuit.mcx([inA2,inB1], v3)
	circuit.mcx([inA1,inB2], v3)
	circuit.mcx([inA2,inB0,inA1,inB1], v3)
	circuit.mcx([inA1,inB1,inA0,inB2], v3)
	circuit.mcx([inA2,inB0,inA0,inB2], v3)

	circuit.mcx([inA2,inB0,inA1,inA0,inB1], v3)
	circuit.mcx([inA1,inB1,inB0,inA0], v3)
	circuit.mcx([inA0,inB2,inA1,inB0,inB1], v3)

	#v4
	circuit.mcx([inA2,inB2], v4)
	circuit.mcx([inA2,inB1,inA1,inB2], v4)

	circuit.mcx([inA2,inB1,inB0,inA1], v4)
	circuit.mcx([inA2,inB1,inA1,inA0,inB2], v4)
	circuit.mcx([inA2,inB1,inB0,inA0,inB2], v4)

	circuit.mcx([inA2,inB1,inB0,inA1,inA0], v4)
	circuit.mcx([inA2,inB1,inA1,inB0,inA0], v4)
	circuit.mcx([inA2,inB1,inA0,inB2,inA1,inB0], v4)


	circuit.mcx([inA1,inB2,inA2,inB0,inB1], v4)
	circuit.mcx([inA1,inB2,inB1,inA0], v4)
	circuit.mcx([inA1,inB2,inA2,inB0,inA0], v4)

	circuit.mcx([inA1,inB2,inA2,inB0,inA0,inB1], v4)
	circuit.mcx([inA1,inB2,inB1,inB0,inA0], v4)
	circuit.mcx([inA1,inB2,inA0,inB0,inB1], v4)

	circuit.mcx([inA2,inB0,inA1,inB1,inA0,inB2], v4)

	#v5
	circuit.mcx([inA2,inB2,inB1,inA1], v5)

	circuit.mcx([inA2,inB2,inB1,inB0,inA1], v5)
	circuit.mcx([inA2,inB2,inB1,inA1,inA0], v5)
	circuit.mcx([inA2,inB2,inB1,inB0,inA0], v5)

	circuit.mcx([inA2,inB2,inB1,inB0,inA1,inA0], v5)
	circuit.mcx([inA2,inB2,inB1,inA1,inB0,inA0], v5)
	circuit.mcx([inA2,inB2,inB1,inA0,inA1,inB0], v5)


	circuit.mcx([inA2,inB2,inA1,inB0,inB1], v5)
	circuit.mcx([inA2,inB2,inA1,inB1,inA0], v5)
	circuit.mcx([inA2,inB2,inA1,inB0,inA0], v5)

	circuit.mcx([inA2,inB2,inA1,inB0,inA0,inB1], v5)
	circuit.mcx([inA2,inB2,inA1,inB1,inB0,inA0], v5)
	circuit.mcx([inA2,inB2,inA1,inA0,inB0,inB1], v5)

	circuit.mcx([inA2,inB2,inB0,inA1,inB1,inA0], v5)
	circuit.mcx([inA2,inB1,inA1,inB0,inA0], v5)

	circuit.measure(v0,0)
	circuit.measure(v1,1)
	circuit.measure(v2,2)
	circuit.measure(v3,3)
	circuit.measure(v4,4)
	circuit.measure(v5,5)

	compiled_circuit = transpile(circuit, simulator)

	job = simulator.run(compiled_circuit, shots=1)

	result = job.result()

	counts = result.get_counts(compiled_circuit)
	
	for val in counts:
		pass
	print(val)
	a = 1

r0 = val[5]
r1 = val[4]
r2 = val[3]
r3 = val[2]
r4 = val[1]
r5 = val[0]

result = int(r0) + int(r1)*2 + int(r2)*4 + int(r3)*8 + int(r4)*16 + int(r5)*32

print(result)