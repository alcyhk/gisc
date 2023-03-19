from qiskit import transpile
from qiskit.visualization import plot_histogram
import sys,os
sys.path.append('../')
from param import *


from collections import OrderedDict


def ModSimMetaStart():
	print('start')

def ModSimRunHeader(numOfRuns):
	print("----------------------------")
	print('run ',numOfRuns+1)

def simRunFooterPrintTop(cregs):
	print('opaddr ', int(cregs[c_opaddr2] + cregs[c_opaddr1] + cregs[c_opaddr0],2),'|', \
		cregs[c_opaddr2],cregs[c_opaddr1],cregs[c_opaddr0])
	print('isa ',cregs[c_isa7],cregs[c_isa6],cregs[c_isa5],cregs[c_isa4],cregs[c_isa3],cregs[c_isa2],cregs[c_isa1],cregs[c_isa0]) #q3 opvalA1
	print('fly,set,cpy,phy ',cregs[c_op_fly],cregs[c_op_set],cregs[c_op_cpy],cregs[c_op_phy]) 

def simRunFooterPrintBin(cregs):
	print('dmy2,dmy1,dmy0 ',cregs[c_dmy2],cregs[c_dmy1],cregs[c_dmy0]) 
	print('regA ',cregs[c_qreg_a2],cregs[c_qreg_a1],cregs[c_qreg_a0]) 
	print('regB ',cregs[c_qreg_b2],cregs[c_qreg_b1],cregs[c_qreg_b0]) 
	print('regSG ',cregs[c_qreg_sg2],cregs[c_qreg_sg1],cregs[c_qreg_sg0]) 
	print('regInputA ',cregs[c_qreg_inputA2],cregs[c_qreg_inputA1],cregs[c_qreg_inputA0]) 
	print('regInputB ',cregs[c_qreg_inputB2],cregs[c_qreg_inputB1],cregs[c_qreg_inputB0]) 
	print('regInputS ',cregs[c_qreg_inputS2],cregs[c_qreg_inputS1],cregs[c_qreg_inputS0]) 
	print('regOutputCL ',cregs[c_qreg_outputCL2],cregs[c_qreg_outputCL1],cregs[c_qreg_outputCL0]) 
	print('regOutputCU ',cregs[c_qreg_outputCU2],cregs[c_qreg_outputCU1],cregs[c_qreg_outputCU0]) 

def simRunFooterPrintDec(cregs):
	print('regA ',int(cregs[c_qreg_a2]+cregs[c_qreg_a1]+cregs[c_qreg_a0],2)) 
	print('regB ',int(cregs[c_qreg_b2]+cregs[c_qreg_b1]+cregs[c_qreg_b0],2)) 
	print('regSG ',int(cregs[c_qreg_sg2]+cregs[c_qreg_sg1]+cregs[c_qreg_sg0],2)) 
	print('regInputA ',int(cregs[c_qreg_inputA2]+cregs[c_qreg_inputA1]+cregs[c_qreg_inputA0],2)) 
	print('regInputB ',int(cregs[c_qreg_inputB2]+cregs[c_qreg_inputB1]+cregs[c_qreg_inputB0],2))
	print('regInputS ',int(cregs[c_qreg_inputS2]+cregs[c_qreg_inputS1]+cregs[c_qreg_inputS0],2))
	print('regOutputCL ',int(cregs[c_qreg_outputCL2]+cregs[c_qreg_outputCL1]+cregs[c_qreg_outputCL0],2)) 
	print('regOutputCU ',int(cregs[c_qreg_outputCU2]+cregs[c_qreg_outputCU1]+cregs[c_qreg_outputCU0],2))

def ModSimRunFooter(circuit,simulator,cregs):
	
	compiled_circuit = transpile(circuit, simulator)

	job = simulator.run(compiled_circuit, shots=1)

	result = job.result()

	counts = result.get_counts(compiled_circuit)
	print("\nResult:",counts)
	for cregs in counts:
		pass
	initFlag = 1

	cregs = cregs[::-1]

	
	simRunFooterPrintTop(cregs)
	#simRunFooterPrintBin(cregs)
	simRunFooterPrintDec(cregs)
	print("----------------------------\n")
	return cregs


def simMetaEndPrint(circuit):
	print("Type of gates")
	for i in circuit.count_ops():
	    print("\t",i, circuit.count_ops()[i])

	print('Non-local gates: ',circuit.num_nonlocal_gates())
	simNumOfQbits = circuit.width() - NUM_OF_CREGS
	simNumOfCbits = NUM_OF_CREGS

	print('Number of Quantum bits: ',simNumOfQbits)
	print('Number of Classical bits: ',simNumOfCbits)
	print('Depth: ',circuit.depth())
	#print('Depth(basis gates): ',transpile(circuit, basis_gates=['u','cx','x','cswap','swap']).depth())
	print("End")

def simMetaEndDraw(circuit):
	circuit.draw(output='text',filename='blueprint')

def ModSimMetaEnd(circuit):
	simMetaEndPrint(circuit)
	simMetaEndDraw(circuit)

	
	

