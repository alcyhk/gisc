from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator

from queue import Queue

import sys,os
import numpy as np
from random import randint

from qiskit.visualization import plot_histogram
from math import pi

sys.path.append('modules')
from param import *
from modAppend import *
from modOpaddr import *
from modISA import *
from modAlgo import *
from modMeasure import *
from modSim import *
from modSG import *

sys.path.append('ML')

from modMLMapping import *
from modMLLearning import *

from mlParam import *
from mlLearnInit import *


def main():

	ModSimMetaStart()
	initFlag = 0
	codeprint = np.loadtxt('code.bin',comments='#', dtype='str')
	#print(codeprint)


	mlState = 0
	repo = np.zeros((REPO_SIZE,REPO_BITS))

	sample = np.zeros((ML_NUM_PICS,ML_NUM_PX,ML_NUM_COE))	
	weight = np.zeros((ML_NUM_MODEL,ML_NUM_COE))

	mlTrainStatus = np.zeros(REPO_SIZE)

	sample = ML_SampleInit()

	gIndex = np.zeros((ML_NUM_PX,ML_NUM_COE))
	trainPx = np.zeros((ML_NUM_MODEL,ML_NUM_GROUP, ML_NUM_PX, ML_NUM_COE))
	trainPx = ML_LearnInit()
	mlMode = 0
	mlState = 0

	nPx = np.zeros((ML_NUM_GROUP, ML_NUM_PX, ML_NUM_COE))
	
	cregs = ['0' for i in range(NUM_OF_CREGS)]
	for numOfRuns in range(maxNumOfRuns):
		
		ModSimRunHeader(numOfRuns)
		simulator = AerSimulator(method='matrix_product_state')	
		circuit = QuantumCircuit()
		ParamQcRegsInit(circuit)
		ModAppend(circuit,cregs,codeprint) 
		ModAlgo(circuit)
		ModOpaddr(circuit) 
		ModISA(circuit)
		ModMeasure(circuit)
		cregs = ModSimRunFooter(circuit,simulator,cregs)
		mlMode = ModSG(cregs,repo,mlMode)
		
		
		#-----ML------------------------------
		mlModel = int(''.join(str(int(i)) for i in repo[REPO_ML_MODEL][::-1]),2)

		for i in range(ML_NUM_GROUP):
			for p in range(ML_NUM_PX):
				nPx[i][p] = [trainPx[mlModel][i][p][ML_r],trainPx[mlModel][i][p][ML_g],trainPx[mlModel][i][p][ML_b]]
	
		if(mlMode == 0):
			c_qreg_phy_b0 = 0
			mlState = 0
			c_qreg_phy_b2,c_qreg_phy_b1,c_qreg_phy_b0 = 0,0,0
			mlMapping(repo,sample,weight)
		elif(mlMode == 1):
			if(mlState == 4):c_qreg_phy_b0 = 0
			mlState = mlLearning(mlState,mlTrainStatus,gIndex,mlModel,weight,nPx)

main()

