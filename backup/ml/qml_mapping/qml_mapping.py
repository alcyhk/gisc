from qiskit import QuantumCircuit,Aer, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram
from math import pi,acos,cos
from mlSample import *
from mlParam import *

simulator = QasmSimulator()

circuit = QuantumCircuit(5, 5)

PIC_QUALITY = KINDA0

print("Purple Image finder ")

print("Description: Check if the image is purple")

imagePx = sample[PIC_QUALITY]

print("\nOriginal Image:")
print("px0 [",imagePx[0][r],imagePx[0][g],imagePx[0][b],"]")
print("px1 [",imagePx[1][r],imagePx[1][g],imagePx[1][b],"]")
print("px2 [",imagePx[2][r],imagePx[2][g],imagePx[2][b],"]")
print("px3 [",imagePx[3][r],imagePx[3][g],imagePx[3][b],"]")

nPx = np.zeros((NUM_PX, NUM_COE))

nPx[0] = [pi*imagePx[0][r]/255,pi*imagePx[0][g]/255,pi*imagePx[0][b]/255]
nPx[1] = [pi*imagePx[1][r]/255,pi*imagePx[1][g]/255,pi*imagePx[1][b]/255]
nPx[2] = [pi*imagePx[2][r]/255,pi*imagePx[2][g]/255,pi*imagePx[2][b]/255]
nPx[3] = [pi*imagePx[3][r]/255,pi*imagePx[3][g]/255,pi*imagePx[3][b]/255]

print("\nNormalized Image:")
print("px0 [",f'{nPx[0][r]:.2f}',f'{nPx[0][g]:.2f}',f'{nPx[0][b]:.2f}',"]")
print("px1 [",f'{nPx[1][r]:.2f}',f'{nPx[1][g]:.2f}',f'{nPx[1][b]:.2f}',"]")
print("px2 [",f'{nPx[2][r]:.2f}',f'{nPx[2][g]:.2f}',f'{nPx[2][b]:.2f}',"]")
print("px3 [",f'{nPx[3][r]:.2f}',f'{nPx[3][g]:.2f}',f'{nPx[3][b]:.2f}',"]")

wr = (imagePx[0][r] + imagePx[1][r] + imagePx[2][r] + imagePx[3][r])/4
wg = (imagePx[0][g] + imagePx[1][g] + imagePx[2][g] + imagePx[3][g])/4
wb = (imagePx[0][b] + imagePx[1][b] + imagePx[2][b] + imagePx[3][b])/4




print("\nOriginal Weight [",f'{wr:.2f}',f'{wg:.2f}',f'{wb:.2f}',"]")

purplePx0 = [128,0,128]
purplePx1 = [102,2,60]
purplePx2 = [120,81,169]
purplePx3 = [199,21,133]

w = [0,0,0]

w[r] = (purplePx0[r] + purplePx1[r] + purplePx2[r] + purplePx3[r])/4
w[g] = (purplePx0[g] + purplePx1[g] + purplePx2[g] + purplePx3[g])/4
w[b] = (purplePx0[b] + purplePx1[b] + purplePx2[b] + purplePx3[b])/4

nw = [0,0,0]
nw[r] = pi*w[r]/255
nw[g] = pi*w[g]/255
nw[b] = pi*w[b]/255

print("\nNormalized Weight [",f'{nw[r]:.2f}',f'{nw[g]:.2f}',f'{nw[b]:.2f}',"]")

circuit.rx(nPx[0][r],px0)
circuit.rx(-nw[r],px0)
circuit.ry(nPx[0][g],px0)
circuit.ry(-nw[g],px0)
circuit.rz(nPx[0][b],px0)
circuit.rz(-nw[b],px0)

circuit.crx(pi/NUM_PX,px0,a)


circuit.rx(nPx[1][r],px1)
circuit.rx(-nw[r],px1)
circuit.ry(nPx[1][g],px1)
circuit.ry(-nw[g],px1)
circuit.rz(nPx[1][b],px1)
circuit.rz(-nw[b],px1)

circuit.crx(pi/NUM_PX,px1,a)


circuit.rx(nPx[2][r],px2)
circuit.rx(-nw[r],px2)
circuit.ry(nPx[2][g],px2)
circuit.ry(-nw[g],px2)
circuit.rz(nPx[2][b],px2)
circuit.rz(-nw[b],px2)

circuit.crx(pi/NUM_PX,px2,a)

circuit.rx(nPx[3][r],px3)
circuit.rx(-nw[r],px3)
circuit.ry(nPx[3][g],px3)
circuit.ry(-nw[g],px3)
circuit.rz(nPx[3][b],px3)
circuit.rz(-nw[b],px3)

circuit.crx(pi/NUM_PX,px3,a)

circuit.measure(a,c4)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=SHOTS)

result = job.result()

counts = result.get_counts(compiled_circuit)

circuit.draw(output='mpl',filename='qml_mapping')

prob = counts[max(counts,key=counts.get)]/SHOTS

t = pi/acos(1-2*prob)
dp = 1/t


if(max(counts,key=counts.get).find('1') == -1):
	if(dp >= P_RATE):
		print("\nProbability of Matching",f'{dp*100:.2f}',"%")
		print("\nMatched: Perfect")
	elif(dp >= S_RATE):
		print("\nProbability of Matching",f'{dp*100:.2f}',"%")
		print("\nMatched: Good")
	elif(dp >= K_RATE):
		print("\nProbability of Matching",f'{dp*100:.2f}',"%")
		print("\nMatched: Kinda")
	elif(dp >= B_RATE):
		print("\nProbability of Matching",f'{dp*100:.2f}',"%")
		print("\nMatched: Bad")
	else:
		print("\nFailure: Not even closed")
else:
	print("\nFailure: Not even closed")
