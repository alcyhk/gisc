from qiskit.providers.aer import QasmSimulator
from qiskit import QuantumCircuit,transpile
from mlParam import *
from math import pi


def mlLearning(mlState,mlTrainStatus,gIndex,mlModel,weight,nPx):
	print("State: Training\n")
	mts = mlTrainStatus[mlModel]
	if(mts == 0):#first run
		#0 == idle, 1 == group 1, 2 == group 2, 3 == group 3, 4 == group, 5 == calculate weight, 6 == done, 7 == error
		if(mlState >= 0 and mlState < 4):# 0,1,2,3
			print("Training Group: ",mlState)
			n = mlState

			#-----state start-----------------------------------------------------------
			
			simulator = QasmSimulator()

			circuit = QuantumCircuit(ML_numQUBITS, ML_numCLBITS)#21 xyz + 4 training pixel
			for px in range(ML_NUM_PX):

				circuit.rx(nPx[n][px][ML_r],px)	

				
				for i in range(ML_NUM_DINDEX):
					circuit.rx(-pi*i/ML_MAX_DINDEX,px)
					circuit.crx(pi/ML_NUM_PX,px,i+ML_xStep)
					circuit.rx(pi*i/ML_MAX_DINDEX,px)

				circuit.rx(-nPx[n][px][ML_r],px)	
				
				
				circuit.rx(nPx[n][px][ML_g],px)	

				for i in range(ML_NUM_DINDEX):
					#y
					circuit.rx(-pi*i/ML_MAX_DINDEX,px)
					circuit.crx(pi/ML_NUM_PX,px,i+ML_xStep + ML_yStep)
					circuit.rx(pi*i/ML_MAX_DINDEX,px)

				circuit.rx(-nPx[n][px][ML_g],px)	
				circuit.rx(nPx[n][px][ML_b],px)

				for i in range(ML_NUM_DINDEX):
					#z
					circuit.rx(-pi*i/ML_MAX_DINDEX,px)
					circuit.crx(pi/ML_NUM_PX,px,i+ML_xStep + ML_yStep + ML_zStep)
					circuit.rx(pi*i/ML_MAX_DINDEX,px)
					#px1----------------------------------------------------
				circuit.rx(-nPx[n][px][ML_b],px)

			circuit.measure_all()



			#--------wrap up
			compiled_circuit = transpile(circuit, simulator)

			job = simulator.run(compiled_circuit, memory=True,shots=MLL_SHOTS)

			result = job.result()
			memory = result.get_memory(compiled_circuit)  # prints ['00', '00', '11', '00'] 

			shotsX = [0]*ML_NUM_DINDEX
			shotsY = [0]*ML_NUM_DINDEX
			shotsZ = [0]*ML_NUM_DINDEX
			
			for s in range(len(shotsX)):
				for l in range(len(memory)):
					if(memory[l][ML_numQUBITS-1-(ML_x0+s)] == '1'): 
						shotsX[s] = shotsX[s] + 1
			print("\nr: ",shotsX)


			for s in range(len(shotsY)):
				for l in range(len(memory)):
					if(memory[l][ML_numQUBITS-1-(ML_y0+s)] == '1'): 
						shotsY[s] = shotsY[s] + 1
			print("g: ",shotsY)


			for s in range(len(shotsZ)):
				for l in range(len(memory)):
					if(memory[l][ML_numQUBITS-1-(ML_z0+s)] == '1'): 
						shotsZ[s] = shotsZ[s] + 1
			print("b: ",shotsZ)

			#index of max possiblily
			indexR = shotsX.index(min(shotsX))
			indexG = shotsY.index(min(shotsY))
			indexB = shotsZ.index(min(shotsZ))
			print("\nindex of desired r,g,b: ",indexR,indexG,indexB )
			gIndex[n]= [indexR,indexG,indexB]

			#print(index)
			#-----state end-----------------------------------------------------------



			mlState = mlState + 1
			c_qreg_phy_b0 = 1

		elif(mlState == 4):#calculate weight 4
			print("Calculating the weight ...")
			#calculate state == 4	
			gIndexR, gIndexG, gIndexB = 0,0,0
			for i in range(len(gIndex)):
				gIndexR = gIndexR + gIndex[i][ML_r]	
				gIndexG = gIndexG + gIndex[i][ML_g]
				gIndexB = gIndexB + gIndex[i][ML_b]	

			gIndexR = gIndexR / len(gIndex) 
			gIndexG = gIndexG / len(gIndex) 
			gIndexB = gIndexB / len(gIndex) 

			nw = [pi*gIndexR/ML_MAX_DINDEX,pi*gIndexG/ML_MAX_DINDEX,pi*gIndexB/ML_MAX_DINDEX]
			print("The weight for the Target Model are",f'{nw[ML_r]:.2f}',f'{nw[ML_g]:.2f}',f'{nw[ML_b]:.2f}')
			weight[mlModel] = nw

			mlTrainStatus[mlModel] = 1
			mlState = 0
		

	return mlState		


