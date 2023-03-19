import sys,os
sys.path.append('../')
from param import *

def ModMeasure(circuit):
	circuit.measure(opaddr0,c_opaddr0)
	circuit.measure(opaddr1,c_opaddr1)
	circuit.measure(opaddr2,c_opaddr2)

	circuit.measure(isa0,c_isa0)
	circuit.measure(isa1,c_isa1)
	circuit.measure(isa2,c_isa2)
	circuit.measure(isa3,c_isa3)

	circuit.measure(isa4,c_isa4)
	circuit.measure(isa5,c_isa5)
	circuit.measure(isa6,c_isa6)
	circuit.measure(isa7,c_isa7)

	circuit.measure(op_set,c_op_set)
	circuit.measure(op_cpy,c_op_cpy)
	circuit.measure(op_phy,c_op_phy)
	circuit.measure(op_fly,c_op_fly)

	circuit.measure(dmy0,c_dmy0)
	circuit.measure(dmy1,c_dmy1)
	circuit.measure(dmy2,c_dmy2)


	circuit.measure(qreg_a0,c_qreg_a0)
	circuit.measure(qreg_a1,c_qreg_a1)
	circuit.measure(qreg_a2,c_qreg_a2)

	circuit.measure(qreg_b0,c_qreg_b0)
	circuit.measure(qreg_b1,c_qreg_b1)
	circuit.measure(qreg_b2,c_qreg_b2)

	circuit.measure(qreg_sg0,c_qreg_sg0)
	circuit.measure(qreg_sg1,c_qreg_sg1)
	circuit.measure(qreg_sg2,c_qreg_sg2)

	circuit.measure(qreg_inputA0,c_qreg_inputA0)
	circuit.measure(qreg_inputA1,c_qreg_inputA1)
	circuit.measure(qreg_inputA2,c_qreg_inputA2)

	circuit.measure(qreg_inputB0,c_qreg_inputB0)
	circuit.measure(qreg_inputB1,c_qreg_inputB1)
	circuit.measure(qreg_inputB2,c_qreg_inputB2)

	circuit.measure(qreg_inputS0,c_qreg_inputS0)
	circuit.measure(qreg_inputS1,c_qreg_inputS1)
	circuit.measure(qreg_inputS2,c_qreg_inputS2)

	circuit.measure(qreg_outputCL0,c_qreg_outputCL0)
	circuit.measure(qreg_outputCL1,c_qreg_outputCL1)
	circuit.measure(qreg_outputCL2,c_qreg_outputCL2)

	circuit.measure(qreg_outputCU0,c_qreg_outputCU0)
	circuit.measure(qreg_outputCU1,c_qreg_outputCU1)
	circuit.measure(qreg_outputCU2,c_qreg_outputCU2)


