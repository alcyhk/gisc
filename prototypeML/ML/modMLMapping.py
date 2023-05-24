import sys,os
sys.path.append('../')
#from mlMapParam import *
from mlMapSample import *
from mlParam import *

from param import *
from math import pi,acos
from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator




def mlMapping(repo,sample,weight):
	print("State: Mapping\n")
	simulator = AerSimulator(method='matrix_product_state')	
	circuit = QuantumCircuit(ML_MAP_QUBITS,ML_MAP_CLBITS)

	

	nPx = np.zeros((ML_NUM_PX,ML_NUM_COE))
	nw = np.zeros(ML_NUM_COE)

	mlSample = int(''.join(str(int(i)) for i in repo[REPO_ML_SAMPLE][::-1]),2)
	mlModel = int(''.join(str(int(i)) for i in repo[REPO_ML_MODEL][::-1]),2)
	
	nPx = sample[mlSample]
	print(nPx)

	nw = weight[mlModel]
	
	print(nw)


	circuit.rx(nPx[0][ML_r],ML_px0)
	circuit.rx(-nw[ML_r],ML_px0)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px0,ML_a)

	circuit.rx(nPx[0][ML_g],ML_px0)
	circuit.rx(-nw[ML_g],ML_px0)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px0,ML_a)

	circuit.rx(nPx[0][ML_b],ML_px0)
	circuit.rx(-nw[ML_b],ML_px0)

	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px0,ML_a)

	
	circuit.rx(nPx[1][ML_r],ML_px1)
	circuit.rx(-nw[ML_r],ML_px1)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px1,ML_a)

	circuit.rx(nPx[1][ML_g],ML_px1)
	circuit.rx(-nw[ML_g],ML_px1)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px1,ML_a)

	circuit.rx(nPx[1][ML_b],ML_px1)
	circuit.rx(-nw[ML_b],ML_px1)

	#circuit.x(px1)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px1,ML_a)


	#------
	circuit.rx(nPx[2][ML_r],ML_px2)
	circuit.rx(-nw[ML_r],ML_px2)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px2,ML_a)

	circuit.rx(nPx[2][ML_g],ML_px2)
	circuit.rx(-nw[ML_g],ML_px2)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px2,ML_a)

	circuit.rx(nPx[2][ML_b],ML_px2)
	circuit.rx(-nw[ML_b],ML_px2)

	#circuit.x(px2)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px2,ML_a)


	#------
	circuit.rx(nPx[3][ML_r],ML_px3)
	circuit.rx(-nw[ML_r],ML_px3)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px3,ML_a)

	circuit.rx(nPx[3][ML_g],ML_px3)
	circuit.rx(-nw[ML_g],ML_px3)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px3,ML_a)

	circuit.rx(nPx[3][ML_b],ML_px3)
	circuit.rx(-nw[ML_b],ML_px3)

	#circuit.x(px3)
	circuit.crx(pi/(ML_NUM_PX*ML_NUM_COE),ML_px3,ML_a)


	#------

	circuit.measure(ML_a,ML_c4)

	compiled_circuit = transpile(circuit, simulator)

	job = simulator.run(compiled_circuit, shots=MLM_SHOTS)

	result = job.result()

	counts = result.get_counts(compiled_circuit)
	print(counts)
	prob = counts[max(counts,key=counts.get)]/MLM_SHOTS
	t = pi/acos(1-2*prob)
	dp = 1/t

	if(max(counts,key=counts.get).find('1') == -1):#no 1s, all zeros
		if(dp >= ML_P_RATE_7):#no 1s, all zeros
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 99%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 1,1,1
		elif(dp >= ML_P_RATE_6):#no 1s, all zeros
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 95%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 1,1,0
		elif(dp >= ML_P_RATE_5):#rare rate
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 90%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 1,0,1
		elif(dp >= ML_P_RATE_4):#rare rate
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 85%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 1,0,0
		elif(dp >= ML_P_RATE_3):#rare rate
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 80%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 0,1,1
		elif(dp >= ML_P_RATE_2):#rare rate
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 70%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 0,1,0
		elif(dp >= ML_P_RATE_1):#rare rate
			print("\nProbability of Matching",f'{dp*100:.2f}',"%")
			print("\nMatched: 60%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 0,0,1
		else:
			print("\nFailure: Under 60%") 
			c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 0,0,0
	else:
		print("\nFailure: Not even closed")
		c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = 0,0,0
		print(c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0)
			
	
