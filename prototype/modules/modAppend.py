import sys,os
sys.path.append('../')
from param import *

def modAppendPrintISA(curr_addr):
	if(curr_addr == 0)  :print("ISA: "+"OP_SET "+"QUB_INPUTA "+"VAL_TWO ")
	elif(curr_addr == 1):print("ISA: "+"OP_SET "+"QUB_INPUTB "+"VAL_THREE")
	elif(curr_addr == 2):print("ISA: "+"OP_SET "+"QUB_INPUTS "+"VAL_SEVEN")
	elif(curr_addr == 3):print("ISA: "+"OP_CPY "+"QUB_REGA "+"QUB_OUTPUTCL")
	elif(curr_addr == 4):print("ISA: "+"OP_SET "+"QUB_F_CON "+"VAL_ONE") 
	elif(curr_addr == 5):print("ISA: "+"OP_SET "+"QUB_F_POS "+"VAL_SEVEN")
	elif(curr_addr == 6):print("ISA: "+"OP_FLY "+"VAL_ZERO "+"VAL_ZERO")
	elif(curr_addr == 7):print("ISA: "+"OP_FLY "+"VAL_ZERO "+"VAL_ZERO")

def ModAppend(circuit,cregs):
	curr_addr = int(cregs[c_opaddr2] + cregs[c_opaddr1] + cregs[c_opaddr0],2)
	print('Current Addr: ', curr_addr)
	if(curr_addr == 0)  :curr_isa = OP_SET+QUB_INPUTA+VAL_TWO
	elif(curr_addr == 1):curr_isa = OP_SET+QUB_INPUTB+VAL_THREE
	elif(curr_addr == 2):curr_isa = OP_SET+QUB_INPUTS+VAL_SEVEN
	elif(curr_addr == 3):curr_isa = OP_CPY+QUB_REGA+QUB_OUTPUTCL
	elif(curr_addr == 4):curr_isa = OP_SET+QUB_INPUTA+VAL_ONE 
	elif(curr_addr == 5):curr_isa = OP_SET+QUB_INPUTB+VAL_SEVEN
	elif(curr_addr == 6):curr_isa = OP_FLY+VAL_ZERO+VAL_ZERO
	elif(curr_addr == 7):curr_isa = OP_FLY+VAL_ZERO+VAL_ZERO

	modAppendPrintISA(curr_addr)

	#------------------------------------------------
	circuit.prepare_state(curr_isa[7],qubits=isa0)
	circuit.prepare_state(curr_isa[6],qubits=isa1)
	circuit.prepare_state(curr_isa[5],qubits=isa2)
	circuit.prepare_state(curr_isa[4],qubits=isa3)

	circuit.prepare_state(curr_isa[3],qubits=isa4)
	circuit.prepare_state(curr_isa[2],qubits=isa5)
	circuit.prepare_state(curr_isa[1],qubits=isa6)
	circuit.prepare_state(curr_isa[0],qubits=isa7)
	

	#circuit.barrier()
	#------------------------------------------------

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
