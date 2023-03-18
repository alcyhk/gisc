from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator

def main():
	inputA = 0b0000

	for x in range(16):

		simulator = QasmSimulator()

		circuit = QuantumCircuit(4, 4)

		if(inputA & 0b1 != 0):circuit.x(0)
		if(inputA & 0b10 != 0):circuit.x(1)
		if(inputA & 0b100 != 0):circuit.x(2)
		if(inputA & 0b1000 != 0):circuit.x(3)

		circuit.mcx([0,1,2],3)
		circuit.mcx([0,1],2)
		circuit.cx(0,1)
		circuit.x(0)

		circuit.measure(0,0)
		circuit.measure(1,1)
		circuit.measure(2,2)
		circuit.measure(3,3)

		compiled_circuit = transpile(circuit, simulator)

		job = simulator.run(compiled_circuit, shots=1)

		result = job.result()

		counts = result.get_counts(compiled_circuit)
		
		for val in counts:
			pass

		outputB = int(val[3]) + int(val[2])*2 + int(val[1])*4 + int(val[0])*8
		print(bin(inputA) +","+ val +","+ str(outputB))
		inputA = outputB

main()
