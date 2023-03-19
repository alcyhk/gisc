import sys,os
sys.path.append('../')
from param import *


def ModISA(circuit):
	#opvalB: {isa2,isa1,isa0}
	#opvalA: {isa5,isa4,isa3}
	#opcode: {isa7,isa6}

	#command 0 0b00 op_fly
	circuit.x(isa7) 
	circuit.x(isa6)
	circuit.mcx([isa7,isa6],op_fly)
	circuit.x(isa7)
	circuit.x(isa6)

	#command 0 0b01 op_set
	circuit.x(isa7)
	circuit.mcx([isa7,isa6],op_set)
	circuit.x(isa7)

	#command 0 0b10 op_cpy
	circuit.x(isa6) 
	circuit.mcx([isa7,isa6],op_cpy)
	circuit.x(isa6)

	#command 0 0b11 op_phy
	circuit.mcx([isa7,isa6],op_phy)

		
	#-------------------------------------
	#get opvalA for set
	#000 0
	circuit.x(isa5) 
	circuit.x(isa4) 
	circuit.x(isa3) 
	circuit.mcx([isa5,isa4,isa3],opa_regA) # repo Addr
	circuit.x(isa5) 
	circuit.x(isa4) 
	circuit.x(isa3) 

	#001 1
	circuit.x(isa5) 
	circuit.x(isa4) 
	circuit.mcx([isa5,isa4,isa3],opa_regB) # repo data
	circuit.x(isa5) 
	circuit.x(isa4) 

	#010 2
	circuit.x(isa5) 
	circuit.x(isa3) 
	circuit.mcx([isa5,isa4,isa3],opa_SG)
	circuit.x(isa5) 
	circuit.x(isa3) 

	#011 3
	circuit.x(isa5) 
	circuit.mcx([isa5,isa4,isa3],opa_inputA)# fly_cond
	circuit.x(isa5) 

	#100 4
	circuit.x(isa4) 
	circuit.x(isa3) 
	circuit.mcx([isa5,isa4,isa3],opa_inputB)# fly_pos
	circuit.x(isa4) 
	circuit.x(isa3) 

	#101 5
	circuit.x(isa4) 
	circuit.mcx([isa5,isa4,isa3],opa_inputS)
	circuit.x(isa4)

	#110 6
	circuit.x(isa3) 
	circuit.mcx([isa5,isa4,isa3],opa_outputCL)
	circuit.x(isa3) 

	#111 7
	circuit.mcx([isa5,isa4,isa3],opa_outputCU)

	
	#get opvalb for cpy
	#000 0
	circuit.x(isa2) 
	circuit.x(isa1) 
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_regA) # repo Addr
	circuit.x(isa2) 
	circuit.x(isa1) 
	circuit.x(isa0) 

	#001 1
	circuit.x(isa2) 
	circuit.x(isa1) 
	circuit.mcx([isa2,isa1,isa0],opb_regB) # repo data
	circuit.x(isa2) 
	circuit.x(isa1) 

	#010 2
	circuit.x(isa2) 
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_SG)
	circuit.x(isa2) 
	circuit.x(isa0) 

	#011 3
	circuit.x(isa2) 
	circuit.mcx([isa2,isa1,isa0],opb_inputA)# fly_cond
	circuit.x(isa2) 

	#100 4
	circuit.x(isa1) 
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_inputB)# fly_pos
	circuit.x(isa1) 
	circuit.x(isa0) 

	#101 5
	circuit.x(isa1) 
	circuit.mcx([isa2,isa1,isa0],opb_inputS)
	circuit.x(isa1)

	#110 6
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_outputCL)
	circuit.x(isa0) 

	#111 7
	circuit.mcx([isa2,isa1,isa0],opb_outputCU)


	#get opvalb for phy
	#000 0
	circuit.x(isa2) 
	circuit.x(isa1) 
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regA) # repo Addr
	circuit.x(isa2) 
	circuit.x(isa1) 
	circuit.x(isa0) 

	#001 1
	circuit.x(isa2) 
	circuit.x(isa1) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regB) # repo data
	circuit.x(isa2) 
	circuit.x(isa1) 

	#010 2
	circuit.x(isa2) 
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regC)
	circuit.x(isa2) 
	circuit.x(isa0) 

	#011 3
	circuit.x(isa2) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regD)# fly_cond
	circuit.x(isa2) 

	#100 4
	circuit.x(isa1) 
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regE)# fly_pos
	circuit.x(isa1) 
	circuit.x(isa0) 

	#101 5
	circuit.x(isa1) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regF)
	circuit.x(isa1)

	#110 6
	circuit.x(isa0) 
	circuit.mcx([isa2,isa1,isa0],opb_phy_regG)
	circuit.x(isa0) 

	#111 7
	circuit.mcx([isa2,isa1,isa0],opb_phy_regH)

	


	#set
	circuit.mcx([op_set,isa0],dmy0)
	circuit.mcx([op_set,isa1],dmy1)
	circuit.mcx([op_set,isa2],dmy2)



	#cpy
	circuit.mcx([op_cpy,opb_regA,qreg_a0],dmy0)
	circuit.mcx([op_cpy,opb_regA,qreg_a1],dmy1)
	circuit.mcx([op_cpy,opb_regA,qreg_a2],dmy2)

	circuit.mcx([op_cpy,opb_regB,qreg_b0],dmy0)
	circuit.mcx([op_cpy,opb_regB,qreg_b1],dmy1)
	circuit.mcx([op_cpy,opb_regB,qreg_b2],dmy2)

	circuit.mcx([op_cpy,opb_SG,qreg_sg0],dmy0)
	circuit.mcx([op_cpy,opb_SG,qreg_sg1],dmy1)
	circuit.mcx([op_cpy,opb_SG,qreg_sg2],dmy2)

	circuit.mcx([op_cpy,opb_inputA,qreg_inputA0],dmy0)
	circuit.mcx([op_cpy,opb_inputA,qreg_inputA1],dmy1)
	circuit.mcx([op_cpy,opb_inputA,qreg_inputA2],dmy2)

	circuit.mcx([op_cpy,opb_inputB,qreg_inputB0],dmy0)
	circuit.mcx([op_cpy,opb_inputB,qreg_inputB1],dmy1)
	circuit.mcx([op_cpy,opb_inputB,qreg_inputB2],dmy2)

	circuit.mcx([op_cpy,opb_inputS,qreg_inputS0],dmy0)
	circuit.mcx([op_cpy,opb_inputS,qreg_inputS1],dmy1)
	circuit.mcx([op_cpy,opb_inputS,qreg_inputS2],dmy2)

	circuit.mcx([op_cpy,opb_outputCL,qreg_outputCL0],dmy0)
	circuit.mcx([op_cpy,opb_outputCL,qreg_outputCL1],dmy1)
	circuit.mcx([op_cpy,opb_outputCL,qreg_outputCL2],dmy2)

	circuit.mcx([op_cpy,opb_outputCU,qreg_outputCU0],dmy0)
	circuit.mcx([op_cpy,opb_outputCU,qreg_outputCU1],dmy1)
	circuit.mcx([op_cpy,opb_outputCU,qreg_outputCU2],dmy2)

	#phy
	circuit.mcx([op_phy,opb_phy_regA,qreg_phy_a0],dmy0)
	circuit.mcx([op_phy,opb_phy_regA,qreg_phy_a1],dmy1)
	circuit.mcx([op_phy,opb_phy_regA,qreg_phy_a2],dmy2)

	circuit.mcx([op_phy,opb_phy_regB,qreg_phy_b0],dmy0)
	circuit.mcx([op_phy,opb_phy_regB,qreg_phy_b1],dmy1)
	circuit.mcx([op_phy,opb_phy_regB,qreg_phy_b2],dmy2)

	circuit.mcx([op_phy,opb_phy_regC,qreg_phy_c0],dmy0)
	circuit.mcx([op_phy,opb_phy_regC,qreg_phy_c1],dmy1)
	circuit.mcx([op_phy,opb_phy_regC,qreg_phy_c2],dmy2)

	circuit.mcx([op_phy,opb_phy_regD,qreg_phy_d0],dmy0)
	circuit.mcx([op_phy,opb_phy_regD,qreg_phy_d1],dmy1)
	circuit.mcx([op_phy,opb_phy_regD,qreg_phy_d2],dmy2)

	circuit.mcx([op_phy,opb_phy_regE,qreg_phy_e0],dmy0)
	circuit.mcx([op_phy,opb_phy_regE,qreg_phy_e1],dmy1)
	circuit.mcx([op_phy,opb_phy_regE,qreg_phy_e2],dmy2)

	circuit.mcx([op_phy,opb_phy_regF,qreg_phy_f0],dmy0)
	circuit.mcx([op_phy,opb_phy_regF,qreg_phy_f1],dmy1)
	circuit.mcx([op_phy,opb_phy_regF,qreg_phy_f2],dmy2)

	circuit.mcx([op_phy,opb_phy_regG,qreg_phy_g0],dmy0)
	circuit.mcx([op_phy,opb_phy_regG,qreg_phy_g1],dmy1)
	circuit.mcx([op_phy,opb_phy_regG,qreg_phy_g2],dmy2)

	circuit.mcx([op_phy,opb_phy_regH,qreg_phy_h0],dmy0)
	circuit.mcx([op_phy,opb_phy_regH,qreg_phy_h1],dmy1)
	circuit.mcx([op_phy,opb_phy_regH,qreg_phy_h2],dmy2)

	

	#set cpy phy
	circuit.mcx([op_set,opa_regA],op_swap_regA)
	circuit.mcx([op_cpy,opa_regA],op_swap_regA)
	circuit.mcx([op_phy,opa_regA],op_swap_regA)

	circuit.mcx([op_set,opa_regB],op_swap_regB)
	circuit.mcx([op_cpy,opa_regB],op_swap_regB)
	circuit.mcx([op_phy,opa_regB],op_swap_regB)


	circuit.mcx([op_set,opa_SG],op_swap_SG)
	circuit.mcx([op_cpy,opa_SG],op_swap_SG)
	circuit.mcx([op_phy,opa_SG],op_swap_SG)

	circuit.mcx([op_set,opa_inputA],op_swap_inputA)
	circuit.mcx([op_cpy,opa_inputA],op_swap_inputA)
	circuit.mcx([op_phy,opa_inputA],op_swap_inputA)

	circuit.mcx([op_set,opa_inputB],op_swap_inputB)
	circuit.mcx([op_cpy,opa_inputB],op_swap_inputB)
	circuit.mcx([op_phy,opa_inputB],op_swap_inputB)


	#circuit.mcx([op_set,op_cpy,op_phy,opa_inputS],op_swap_inputS)
	circuit.mcx([op_set,opa_inputS],op_swap_inputS)
	circuit.mcx([op_cpy,opa_inputS],op_swap_inputS)
	circuit.mcx([op_phy,opa_inputS],op_swap_inputS)

	#circuit.mcx([op_set,op_cpy,op_phy,opa_outputCL],op_swap_outputCL)
	circuit.mcx([op_set,opa_outputCL],op_swap_outputCL)
	circuit.mcx([op_cpy,opa_outputCL],op_swap_outputCL)
	circuit.mcx([op_phy,opa_outputCL],op_swap_outputCL)

	#circuit.mcx([op_set,op_cpy,op_phy,opa_outputCU],op_swap_outputCU)
	circuit.mcx([op_set,opa_outputCU],op_swap_outputCU)
	circuit.mcx([op_cpy,opa_outputCU],op_swap_outputCU)
	circuit.mcx([op_phy,opa_outputCU],op_swap_outputCU)

	circuit.cswap(op_swap_regA,qreg_a0,dmy0)
	circuit.cswap(op_swap_regA,qreg_a1,dmy1)
	circuit.cswap(op_swap_regA,qreg_a2,dmy2)

	circuit.cswap(op_swap_regB,qreg_b0,dmy0)
	circuit.cswap(op_swap_regB,qreg_b1,dmy1)
	circuit.cswap(op_swap_regB,qreg_b2,dmy2)

	circuit.cswap(op_swap_SG,qreg_sg0,dmy0)
	circuit.cswap(op_swap_SG,qreg_sg1,dmy1)
	circuit.cswap(op_swap_SG,qreg_sg2,dmy2)


	circuit.cswap(op_swap_inputA,qreg_inputA0,dmy0)
	circuit.cswap(op_swap_inputA,qreg_inputA1,dmy1)
	circuit.cswap(op_swap_inputA,qreg_inputA2,dmy2)

	circuit.cswap(op_swap_inputB,qreg_inputB0,dmy0)
	circuit.cswap(op_swap_inputB,qreg_inputB1,dmy1)
	circuit.cswap(op_swap_inputB,qreg_inputB2,dmy2)


	circuit.cswap(op_swap_inputS,qreg_inputS0,dmy0)
	circuit.cswap(op_swap_inputS,qreg_inputS1,dmy1)
	circuit.cswap(op_swap_inputS,qreg_inputS2,dmy2)


	circuit.cswap(op_swap_outputCL,qreg_outputCL0,dmy0)
	circuit.cswap(op_swap_outputCL,qreg_outputCL1,dmy1)
	circuit.cswap(op_swap_outputCL,qreg_outputCL2,dmy2)

	circuit.cswap(op_swap_outputCU,qreg_outputCU0,dmy0)
	circuit.cswap(op_swap_outputCU,qreg_outputCU1,dmy1)
	circuit.cswap(op_swap_outputCU,qreg_outputCU2,dmy2)

	#fly
	circuit.mcx([op_fly,qreg_inputA0],op_jmp_swap) #fly-cond

	circuit.mcx([op_jmp_swap,qreg_inputB0],dmy0) #fly-pos
	circuit.mcx([op_jmp_swap,qreg_inputB1],dmy1) #fly-pos
	circuit.mcx([op_jmp_swap,qreg_inputB2],dmy2) #fly-pos

	circuit.cswap(op_jmp_swap,opaddr0,dmy0)
	circuit.cswap(op_jmp_swap,opaddr1,dmy1)
	circuit.cswap(op_jmp_swap,opaddr2,dmy2)
