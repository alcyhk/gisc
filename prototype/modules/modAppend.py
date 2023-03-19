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
	if(curr_isa[7] == '1'):circuit.x(isa0)
	if(curr_isa[6] == '1'):circuit.x(isa1)
	if(curr_isa[5] == '1'):circuit.x(isa2)
	if(curr_isa[4] == '1'):circuit.x(isa3)

	if(curr_isa[3] == '1'):circuit.x(isa4)
	if(curr_isa[2] == '1'):circuit.x(isa5)
	if(curr_isa[1] == '1'):circuit.x(isa6)
	if(curr_isa[0] == '1'):circuit.x(isa7)

	circuit.barrier()
	#------------------------------------------------
	if(cregs[c_opaddr0] == '1'):circuit.x(opaddr0)
	if(cregs[c_opaddr1] == '1'):circuit.x(opaddr1)
	if(cregs[c_opaddr2] == '1'):circuit.x(opaddr2)

	if(cregs[c_qreg_a0] == '1'):circuit.x(qreg_a0)
	if(cregs[c_qreg_a1] == '1'):circuit.x(qreg_a1)
	if(cregs[c_qreg_a2] == '1'):circuit.x(qreg_a2)

	if(cregs[c_qreg_b0] == '1'):circuit.x(qreg_b0)
	if(cregs[c_qreg_b1] == '1'):circuit.x(qreg_b1)
	if(cregs[c_qreg_b2] == '1'):circuit.x(qreg_b2)

	if(cregs[c_qreg_sg0] == '1'):circuit.x(qreg_sg0)
	if(cregs[c_qreg_sg1] == '1'):circuit.x(qreg_sg1)
	if(cregs[c_qreg_sg2] == '1'):circuit.x(qreg_sg2)

	if(cregs[c_qreg_inputA0] == '1'):circuit.x(qreg_inputA0)
	if(cregs[c_qreg_inputA1] == '1'):circuit.x(qreg_inputA1)
	if(cregs[c_qreg_inputA2] == '1'):circuit.x(qreg_inputA2)

	if(cregs[c_qreg_inputB0] == '1'):circuit.x(qreg_inputB0)
	if(cregs[c_qreg_inputB1] == '1'):circuit.x(qreg_inputB1)
	if(cregs[c_qreg_inputB2] == '1'):circuit.x(qreg_inputB2)

	if(cregs[c_qreg_inputS0] == '1'):circuit.x(qreg_inputS0)
	if(cregs[c_qreg_inputS1] == '1'):circuit.x(qreg_inputS1)
	if(cregs[c_qreg_inputS2] == '1'):circuit.x(qreg_inputS2)

	if(cregs[c_qreg_outputCL0] == '1'):circuit.x(qreg_outputCL0)
	if(cregs[c_qreg_outputCL1] == '1'):circuit.x(qreg_outputCL1)
	if(cregs[c_qreg_outputCL2] == '1'):circuit.x(qreg_outputCL2)

	if(cregs[c_qreg_outputCU0] == '1'):circuit.x(qreg_outputCU0)
	if(cregs[c_qreg_outputCU1] == '1'):circuit.x(qreg_outputCU1)
	if(cregs[c_qreg_outputCU2] == '1'):circuit.x(qreg_outputCU2)

	if(cregs[c_qreg_phy_a0] == '1'):circuit.x(qreg_phy_a0)
	if(cregs[c_qreg_phy_a1] == '1'):circuit.x(qreg_phy_a1)
	if(cregs[c_qreg_phy_a2] == '1'):circuit.x(qreg_phy_a2)

	if(cregs[c_qreg_phy_b0] == '1'):circuit.x(qreg_phy_b0)
	if(cregs[c_qreg_phy_b1] == '1'):circuit.x(qreg_phy_b1)
	if(cregs[c_qreg_phy_b2] == '1'):circuit.x(qreg_phy_b2)

	if(cregs[c_qreg_phy_c0] == '1'):circuit.x(qreg_phy_c0)
	if(cregs[c_qreg_phy_c1] == '1'):circuit.x(qreg_phy_c1)
	if(cregs[c_qreg_phy_c2] == '1'):circuit.x(qreg_phy_c2)

	if(cregs[c_qreg_phy_d0] == '1'):circuit.x(qreg_phy_d0)
	if(cregs[c_qreg_phy_d1] == '1'):circuit.x(qreg_phy_d1)
	if(cregs[c_qreg_phy_d2] == '1'):circuit.x(qreg_phy_d2)

	if(cregs[c_qreg_phy_e0] == '1'):circuit.x(qreg_phy_e0)
	if(cregs[c_qreg_phy_e1] == '1'):circuit.x(qreg_phy_e1)
	if(cregs[c_qreg_phy_e2] == '1'):circuit.x(qreg_phy_e2)

	if(cregs[c_qreg_phy_f0] == '1'):circuit.x(qreg_phy_f0)
	if(cregs[c_qreg_phy_f1] == '1'):circuit.x(qreg_phy_f1)
	if(cregs[c_qreg_phy_f2] == '1'):circuit.x(qreg_phy_f2)

	if(cregs[c_qreg_phy_g0] == '1'):circuit.x(qreg_phy_g0)
	if(cregs[c_qreg_phy_g1] == '1'):circuit.x(qreg_phy_g1)
	if(cregs[c_qreg_phy_g2] == '1'):circuit.x(qreg_phy_g2)

	if(cregs[c_qreg_phy_h0] == '1'):circuit.x(qreg_phy_h0)
	if(cregs[c_qreg_phy_h1] == '1'):circuit.x(qreg_phy_h1)
	if(cregs[c_qreg_phy_h2] == '1'):circuit.x(qreg_phy_h2)



	circuit.barrier()

