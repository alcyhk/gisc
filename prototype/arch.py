from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from queue import Queue

import sys,os
sys.path.append('modules')
from param import *
from modAppend import *
from modOpaddr import *
from modISA import *
from modAlgo import *
from modMeasure import *
from modSim import *
from modSG import *

def main():
	ModSimMetaStart()
	initFlag = 0
	repo = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	fifoTx=Queue(FIFO_TX_SIZE)
	fifoRx=Queue(FIFO_RX_SIZE)
	cregs = ['0' for i in range(NUM_OF_CREGS)]
	for numOfRuns in range(maxNumOfRuns):
		ModSimRunHeader(numOfRuns)
		simulator = AerSimulator(method='matrix_product_state')
		circuit = QuantumCircuit()
		ParamQcRegsInit(circuit)
		ModAppend(circuit,cregs) 
		ModOpaddr(circuit) 
		ModISA(circuit)
		ModAlgo(circuit)
		ModMeasure(circuit)
		cregs = ModSimRunFooter(circuit,simulator,cregs)
		ModSG(cregs,repo,fifoTx,fifoRx)
	ModSimMetaEnd(circuit)

main()
