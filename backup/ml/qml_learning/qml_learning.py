import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator

from qiskit.visualization import plot_histogram
from math import pi
from mlLearnParam import *
from mlLearnInit import *

print("Purple Image Trainer ")

print("Description: Find the decent weight")


gIndex = np.zeros((NUM_PX,NUM_COE))

trainPx = np.zeros((NUM_MODEL,NUM_GROUP, NUM_PX, NUM_COE))
ML_LearnInit(trainPx)
mlModel = 0

nPx = np.zeros((NUM_GROUP, NUM_PX, NUM_COE))

for i in range(NUM_GROUP):
	for p in range(NUM_PX):
		nPx[i][p] = [trainPx[mlModel][i][p][r],trainPx[mlModel][i][p][g],trainPx[mlModel][i][p][b]]

print("\nTraining ...")

for n in range(NUM_GROUP):
	simulator = QasmSimulator()

	circuit = QuantumCircuit(numQUBITS, numCLBITS)
	print("\nGroup ",n)
	for px in range(NUM_PX):

		circuit.rx(nPx[n][px][r],px)	

		
		for i in range(NUM_DINDEX):
			circuit.rx(-pi*i/MAX_DINDEX,px)
			circuit.crx(pi/NUM_PX,px,i+xStep)
			circuit.rx(pi*i/MAX_DINDEX,px)

		circuit.rx(-nPx[n][px][r],px)	
		
		
		circuit.rx(nPx[n][px][g],px)	

		for i in range(NUM_DINDEX):
			circuit.rx(-pi*i/MAX_DINDEX,px)
			circuit.crx(pi/NUM_PX,px,i+xStep + yStep)
			circuit.rx(pi*i/MAX_DINDEX,px)

		circuit.rx(-nPx[n][px][g],px)	
		circuit.rx(nPx[n][px][b],px)

		for i in range(NUM_DINDEX):
			circuit.rx(-pi*i/MAX_DINDEX,px)
			circuit.crx(pi/NUM_PX,px,i+xStep + yStep + zStep)
			circuit.rx(pi*i/MAX_DINDEX,px)
		circuit.rx(-nPx[n][px][b],px)

	circuit.measure_all()

	compiled_circuit = transpile(circuit, simulator)

	job = simulator.run(compiled_circuit, memory=True,shots=ML_SHOTS)

	result = job.result()

	memory = result.get_memory(compiled_circuit)

	shotsX = [0]*NUM_DINDEX
	shotsY = [0]*NUM_DINDEX
	shotsZ = [0]*NUM_DINDEX
	
	for s in range(len(shotsX)):
		for l in range(len(memory)):
			if(memory[l][numQUBITS-1-(x0+s)] == '1'):
				shotsX[s] = shotsX[s] + 1
	print("\nr: ",shotsX)


	for s in range(len(shotsY)):
		for l in range(len(memory)):
			if(memory[l][numQUBITS-1-(y0+s)] == '1'):
				shotsY[s] = shotsY[s] + 1
	print("g: ",shotsY)


	for s in range(len(shotsZ)):
		for l in range(len(memory)):
			if(memory[l][numQUBITS-1-(z0+s)] == '1'):
				shotsZ[s] = shotsZ[s] + 1
	print("b: ",shotsZ)

	indexR = shotsX.index(min(shotsX))
	indexG = shotsY.index(min(shotsY))
	indexB = shotsZ.index(min(shotsZ))
	print("\nindex of desired r,g,b: ",indexR,indexG,indexB )
	gIndex[n]= [indexR,indexG,indexB]


gIndexR, gIndexG, gIndexB = 0,0,0
for i in range(len(gIndex)):
	gIndexR = gIndexR + gIndex[i][r]	
	gIndexG = gIndexG + gIndex[i][g]
	gIndexB = gIndexB + gIndex[i][b]	

gIndexR = gIndexR / len(gIndex) 
gIndexG = gIndexG / len(gIndex) 
gIndexB = gIndexB / len(gIndex) 

nw = [pi*gIndexR/MAX_DINDEX,pi*gIndexG/MAX_DINDEX,pi*gIndexB/MAX_DINDEX]
print("Weight for the Target Model are",f'{nw[r]:.2f}',f'{nw[g]:.2f}',f'{nw[b]:.2f}')

# Draw the circuit
#circuit.draw(output='mpl',filename='qml_learning')

