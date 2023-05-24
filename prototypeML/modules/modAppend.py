import sys,os
sys.path.append('../')
from param import *

def modAppendPrintISA(curr_isa):
	opcode = curr_isa[0] + curr_isa[1] 
	opvalA = curr_isa[2] + curr_isa[3] + curr_isa[4]
	opvalB = curr_isa[5] + curr_isa[6] + curr_isa[7]
	print("ISA: ",end = '')
	if(opcode == OP_FLY):print("OP_FLY ",end = '')
	elif(opcode == OP_SET):print("OP_SET ",end = '')
	elif(opcode == OP_CPY):print("OP_CPY ",end = '')
	elif(opcode == OP_PHY):print("OP_PHY ",end = '')

	if(opvalA == QUB_REGA):print("QUB_REGA ",end = '')
	elif(opvalA == QUB_REGB):print("QUB_REGB ",end = '')
	elif(opvalA == QUB_SG):print("QUB_SG ",end = '')
	elif(opvalA == QUB_INPUTA):print("QUB_INPUTA ",end = '')#QUB_F_CON
	elif(opvalA == QUB_INPUTB):print("QUB_INPUTB ",end = '')#QUB_F_POS
	elif(opvalA == QUB_INPUTS):print("QUB_INPUTS ",end = '')
	elif(opvalA == QUB_OUTPUTCL):print("QUB_OUTPUTCL ",end = '')
	elif(opvalA == QUB_OUTPUTCU):print("QUB_OUTPUTCU ",end = '')

	if(opvalB == VAL_ZERO):print("VAL_ZERO ")
	elif(opvalB == VAL_ONE):print("VAL_ONE ")
	elif(opvalB == VAL_TWO):print("VAL_TWO ")
	elif(opvalB == VAL_THREE):print("VAL_THREE ")
	elif(opvalB == VAL_FOUR):print("VAL_FOUR ")
	elif(opvalB == VAL_FIVE):print("VAL_FIVE ")
	elif(opvalB == VAL_SIX):print("VAL_SIX ")
	elif(opvalB == VAL_SEVEN):print("VAL_SEVEN ")


def ModAppend(circuit,cregs,codeprint):
	curr_addr = int(cregs[c_opaddr2] + cregs[c_opaddr1] + cregs[c_opaddr0],2)
	print('Current Addr: ', curr_addr)
	
	curr_isa = codeprint[curr_addr]
	modAppendPrintISA(curr_isa)
	
	circuit.prepare_state(curr_isa[7],qubits=isa0)
	circuit.prepare_state(curr_isa[6],qubits=isa1)
	circuit.prepare_state(curr_isa[5],qubits=isa2)
	circuit.prepare_state(curr_isa[4],qubits=isa3)

	circuit.prepare_state(curr_isa[3],qubits=isa4)
	circuit.prepare_state(curr_isa[2],qubits=isa5)
	circuit.prepare_state(curr_isa[1],qubits=isa6)
	circuit.prepare_state(curr_isa[0],qubits=isa7)

	circuit.prepare_state(cregs[c_opaddr0],qubits=opaddr0)
	circuit.prepare_state(cregs[c_opaddr1],qubits=opaddr1)
	circuit.prepare_state(cregs[c_opaddr2],qubits=opaddr2)

	circuit.prepare_state(cregs[c_qreg_a0],qubits=qreg_a0)
	circuit.prepare_state(cregs[c_qreg_a1],qubits=qreg_a1)
	circuit.prepare_state(cregs[c_qreg_a2],qubits=qreg_a2)

	circuit.prepare_state(cregs[c_qreg_b0],qubits=qreg_b0)
	circuit.prepare_state(cregs[c_qreg_b1],qubits=qreg_b1)
	circuit.prepare_state(cregs[c_qreg_b2],qubits=qreg_b2)

	circuit.prepare_state(cregs[c_qreg_sg0],qubits=qreg_sg0)
	circuit.prepare_state(cregs[c_qreg_sg1],qubits=qreg_sg1)
	circuit.prepare_state(cregs[c_qreg_sg2],qubits=qreg_sg2)

	
	circuit.prepare_state(cregs[c_qreg_inputA0],qubits=qreg_inputA0)
	circuit.prepare_state(cregs[c_qreg_inputA1],qubits=qreg_inputA1)
	circuit.prepare_state(cregs[c_qreg_inputA2],qubits=qreg_inputA2)

	circuit.prepare_state(cregs[c_qreg_inputB0],qubits=qreg_inputB0)
	circuit.prepare_state(cregs[c_qreg_inputB1],qubits=qreg_inputB1)
	circuit.prepare_state(cregs[c_qreg_inputB2],qubits=qreg_inputB2)

	circuit.prepare_state(cregs[c_qreg_inputS0],qubits=qreg_inputS0)
	circuit.prepare_state(cregs[c_qreg_inputS1],qubits=qreg_inputS1)
	circuit.prepare_state(cregs[c_qreg_inputS2],qubits=qreg_inputS2)

	circuit.prepare_state(cregs[c_qreg_outputCL0],qubits=qreg_outputCL0)
	circuit.prepare_state(cregs[c_qreg_outputCL1],qubits=qreg_outputCL1)
	circuit.prepare_state(cregs[c_qreg_outputCL2],qubits=qreg_outputCL2)

	circuit.prepare_state(cregs[c_qreg_outputCU0],qubits=qreg_outputCU0)
	circuit.prepare_state(cregs[c_qreg_outputCU1],qubits=qreg_outputCU1)
	circuit.prepare_state(cregs[c_qreg_outputCU2],qubits=qreg_outputCU2)

	
	circuit.prepare_state(cregs[c_qreg_phy_a0],qubits=qreg_phy_a0)
	circuit.prepare_state(cregs[c_qreg_phy_a1],qubits=qreg_phy_a1)
	circuit.prepare_state(cregs[c_qreg_phy_a2],qubits=qreg_phy_a2)

	circuit.prepare_state(cregs[c_qreg_phy_b0],qubits=qreg_phy_b0)
	circuit.prepare_state(cregs[c_qreg_phy_b1],qubits=qreg_phy_b1)
	circuit.prepare_state(cregs[c_qreg_phy_b2],qubits=qreg_phy_b2)

	circuit.prepare_state(cregs[c_qreg_phy_c0],qubits=qreg_phy_c0)
	circuit.prepare_state(cregs[c_qreg_phy_c1],qubits=qreg_phy_c1)
	circuit.prepare_state(cregs[c_qreg_phy_c2],qubits=qreg_phy_c2)

	circuit.prepare_state(cregs[c_qreg_phy_d0],qubits=qreg_phy_d0)
	circuit.prepare_state(cregs[c_qreg_phy_d1],qubits=qreg_phy_d1)
	circuit.prepare_state(cregs[c_qreg_phy_d2],qubits=qreg_phy_d2)

	circuit.prepare_state(cregs[c_qreg_phy_e0],qubits=qreg_phy_e0)
	circuit.prepare_state(cregs[c_qreg_phy_e1],qubits=qreg_phy_e1)
	circuit.prepare_state(cregs[c_qreg_phy_e2],qubits=qreg_phy_e2)

	circuit.prepare_state(cregs[c_qreg_phy_f0],qubits=qreg_phy_f0)
	circuit.prepare_state(cregs[c_qreg_phy_f1],qubits=qreg_phy_f1)
	circuit.prepare_state(cregs[c_qreg_phy_f2],qubits=qreg_phy_f2)

	circuit.prepare_state(cregs[c_qreg_phy_g0],qubits=qreg_phy_g0)
	circuit.prepare_state(cregs[c_qreg_phy_g1],qubits=qreg_phy_g1)
	circuit.prepare_state(cregs[c_qreg_phy_g2],qubits=qreg_phy_g2)

	circuit.prepare_state(cregs[c_qreg_phy_h0],qubits=qreg_phy_h0)
	circuit.prepare_state(cregs[c_qreg_phy_h1],qubits=qreg_phy_h1)
	circuit.prepare_state(cregs[c_qreg_phy_h2],qubits=qreg_phy_h2)


	circuit.barrier()

