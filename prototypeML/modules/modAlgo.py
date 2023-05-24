import sys,os
sys.path.append('../')
from param import *

def qcAlgoAssign(circuit):
	
	circuit.x(qreg_inputS1)
	circuit.x(qreg_inputS2)
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_flipS)
	circuit.x(qreg_inputS1)
	circuit.x(qreg_inputS2)
	
	circuit.x(qreg_inputS0)
	circuit.x(qreg_inputS2)
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_maskS)
	circuit.x(qreg_inputS0)
	circuit.x(qreg_inputS2)
	
	circuit.x(qreg_inputS2)
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_shiftS)
	circuit.x(qreg_inputS2)
	
	circuit.x(qreg_inputS0)
	circuit.x(qreg_inputS1)
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_equalS)
	circuit.x(qreg_inputS0)
	circuit.x(qreg_inputS1)

	circuit.x(qreg_inputS1)
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_greaterS)
	circuit.x(qreg_inputS1)

	circuit.x(qreg_inputS0)
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_addS)
	circuit.x(qreg_inputS0)
	
	circuit.mcx([qreg_inputS0,qreg_inputS1,qreg_inputS2],algo_mulS)
	

	
	
	circuit.cx(qreg_inputA0,algo_flipA0)
	circuit.cx(qreg_inputA1,algo_flipA1)
	circuit.cx(qreg_inputA2,algo_flipA2)
	circuit.cx(qreg_inputB0,algo_flipB0)
	circuit.cx(qreg_inputB1,algo_flipB1)
	circuit.cx(qreg_inputB2,algo_flipB2)

	
	circuit.cx(qreg_inputA0,algo_maskA0)
	circuit.cx(qreg_inputA1,algo_maskA1)
	circuit.cx(qreg_inputA2,algo_maskA2)
	circuit.cx(qreg_inputB0,algo_maskB0)
	circuit.cx(qreg_inputB1,algo_maskB1)
	circuit.cx(qreg_inputB2,algo_maskB2)

	
	circuit.cx(qreg_inputA0,algo_shiftA0)
	circuit.cx(qreg_inputA1,algo_shiftA1)
	circuit.cx(qreg_inputA2,algo_shiftA2)
	circuit.cx(qreg_inputB0,algo_shiftB0)
	circuit.cx(qreg_inputB1,algo_shiftB1)
	circuit.cx(qreg_inputB2,algo_shiftB2)

	
	circuit.cx(qreg_inputA0,algo_equalA0)
	circuit.cx(qreg_inputA1,algo_equalA1)
	circuit.cx(qreg_inputA2,algo_equalA2)
	circuit.cx(qreg_inputB0,algo_equalB0)
	circuit.cx(qreg_inputB1,algo_equalB1)
	circuit.cx(qreg_inputB2,algo_equalB2)

	
	circuit.cx(qreg_inputA0,algo_greaterA0)
	circuit.cx(qreg_inputA1,algo_greaterA1)
	circuit.cx(qreg_inputA2,algo_greaterA2)
	circuit.cx(qreg_inputB0,algo_greaterB0)
	circuit.cx(qreg_inputB1,algo_greaterB1)
	circuit.cx(qreg_inputB2,algo_greaterB2)
	
	circuit.cx(qreg_inputA0,algo_addA0)
	circuit.cx(qreg_inputA1,algo_addA1)
	circuit.cx(qreg_inputA2,algo_addA2)
	circuit.cx(qreg_inputB0,algo_addB0)
	circuit.cx(qreg_inputB1,algo_addB1)
	circuit.cx(qreg_inputB2,algo_addB2)
	
	
	circuit.cx(qreg_inputA0,algo_mulA0)
	circuit.cx(qreg_inputA1,algo_mulA1)
	circuit.cx(qreg_inputA2,algo_mulA2)
	circuit.cx(qreg_inputB0,algo_mulB0)
	circuit.cx(qreg_inputB1,algo_mulB1)
	circuit.cx(qreg_inputB2,algo_mulB2)



def qcAlgoFlip(circuit):
	
	circuit.cx(algo_flipA0,algo_flipC0)
	circuit.cx(algo_flipA1,algo_flipC1)
	circuit.cx(algo_flipA2,algo_flipC2)	
	
	circuit.cx(algo_flipB0,algo_flipC0)
	circuit.cx(algo_flipB1,algo_flipC1)
	circuit.cx(algo_flipB2,algo_flipC2)

	circuit.cswap(algo_flipS,algo_flipC0,qreg_outputCL0)
	circuit.cswap(algo_flipS,algo_flipC1,qreg_outputCL1)
	circuit.cswap(algo_flipS,algo_flipC2,qreg_outputCL2)

	
def qcAlgoMask(circuit):
	
	circuit.mcx([qreg_inputB0,qreg_inputA0],algo_maskC0)
	circuit.mcx([qreg_inputB1,qreg_inputA1],algo_maskC1)
	circuit.mcx([qreg_inputB2,qreg_inputA2],algo_maskC2)

	circuit.cswap(algo_maskS,algo_maskC0,qreg_outputCL0)
	circuit.cswap(algo_maskS,algo_maskC1,qreg_outputCL1)
	circuit.cswap(algo_maskS,algo_maskC2,qreg_outputCL2)
	

def qcAlgoShift(circuit):

	circuit.cx(algo_shiftA0,algo_shiftC0)
	circuit.cx(algo_shiftA1,algo_shiftC1)
	circuit.cx(algo_shiftA2,algo_shiftC2)


	circuit.x(algo_shiftB0)
	circuit.x(algo_shiftB1)
	circuit.x(algo_shiftB2)

	circuit.mcx([algo_shiftB2,algo_shiftB1,algo_shiftB0],algo_shiftD0)

	circuit.cswap(algo_shiftD0,algo_shiftC1,algo_shiftC2)
	circuit.cswap(algo_shiftD0,algo_shiftC0,algo_shiftC1)
	circuit.cswap(algo_shiftD0,algo_shiftD1,algo_shiftC0)

	circuit.mcx([algo_shiftB2,algo_shiftB1,algo_shiftB0],algo_shiftD0)
	circuit.x(algo_shiftB0)
	circuit.x(algo_shiftB1)
	circuit.x(algo_shiftB2)



	#----------------------------

	
	circuit.x(algo_shiftB1)
	circuit.x(algo_shiftB2)

	circuit.mcx([algo_shiftB2,algo_shiftB1,algo_shiftB0],algo_shiftD0)
	circuit.cswap(algo_shiftD0,algo_shiftC0,algo_shiftD1)
	circuit.cswap(algo_shiftD0,algo_shiftC1,algo_shiftC0)
	circuit.cswap(algo_shiftD0,algo_shiftC2,algo_shiftC1)


	circuit.mcx([algo_shiftB2,algo_shiftB1,algo_shiftB0],algo_shiftD0)
	circuit.x(algo_shiftB1)
	circuit.x(algo_shiftB2)
	
	#----------------------------
	circuit.cswap(algo_shiftS,algo_shiftC0,qreg_outputCL0)
	circuit.cswap(algo_shiftS,algo_shiftC1,qreg_outputCL1)
	circuit.cswap(algo_shiftS,algo_shiftC2,qreg_outputCL2)
	
def qcAlgoEqual(circuit):
	
	circuit.x(algo_equalA0)
	circuit.mcx([algo_equalA0,algo_equalB0],algo_equalC0)
	circuit.x(algo_equalA0)

	circuit.x(algo_equalB0)
	circuit.mcx([algo_equalA0,algo_equalB0],algo_equalC0)
	circuit.x(algo_equalB0)

	# -------

	circuit.x(algo_equalA1)
	circuit.mcx([algo_equalA1,algo_equalB1],algo_equalC1)
	circuit.x(algo_equalA1)

	circuit.x(algo_equalB1)
	circuit.mcx([algo_equalA1,algo_equalB1],algo_equalC1)
	circuit.x(algo_equalB1)

	#--------

	circuit.x(algo_equalA2)
	circuit.mcx([algo_equalA2,algo_equalB2],algo_equalC2)
	circuit.x(algo_equalA2)

	circuit.x(algo_equalB2)
	circuit.mcx([algo_equalA2,algo_equalB2],algo_equalC2)
	circuit.x(algo_equalB2)
	

	circuit.x(algo_equalC0)
	circuit.x(algo_equalC1)
	circuit.x(algo_equalC2)

	circuit.mcx([algo_equalC0,algo_equalC1,algo_equalC2],algo_equalD0)

	circuit.swap(algo_equalC0,algo_equalD0)

	
	circuit.cswap(algo_equalS,algo_equalC0,qreg_outputCL0)


def qcAlgoGreater(circuit):
	circuit.x(algo_greaterB2)
	circuit.mcx([algo_greaterA2,algo_greaterB2],algo_greaterC0)
	circuit.x(algo_greaterB2)
	
	circuit.x(algo_greaterB1)
	circuit.mcx([algo_greaterA2,algo_greaterB2,algo_greaterA1,algo_greaterB1],algo_greaterC0)
	circuit.x(algo_greaterB1)


	circuit.x(algo_greaterA2)
	circuit.x(algo_greaterB2)
	circuit.x(algo_greaterB1)
	circuit.mcx([algo_greaterA2,algo_greaterB2,algo_greaterA1,algo_greaterB1],algo_greaterC0)

	circuit.x(algo_greaterA2)
	circuit.x(algo_greaterB2)
	circuit.x(algo_greaterB1)
	
	
	circuit.x(algo_greaterB0)
	circuit.mcx([algo_greaterA2,algo_greaterB2,algo_greaterA1,algo_greaterB1,algo_greaterA0,algo_greaterB0],algo_greaterC0)
	circuit.x(algo_greaterB0)

	circuit.x(algo_greaterA1)
	circuit.x(algo_greaterB1)
	circuit.x(algo_greaterB0)
	circuit.mcx([algo_greaterA2,algo_greaterB2,algo_greaterA1,algo_greaterB1,algo_greaterA0,algo_greaterB0],algo_greaterC0)
	circuit.x(algo_greaterA1)
	circuit.x(algo_greaterB1)
	circuit.x(algo_greaterB0)


	circuit.x(algo_greaterA2)
	circuit.x(algo_greaterB2)
	circuit.x(algo_greaterB0)

	circuit.mcx([algo_greaterA2,algo_greaterB2,algo_greaterA1,algo_greaterB1,algo_greaterA0,algo_greaterB0],algo_greaterC0)

	circuit.x(algo_greaterA2)
	circuit.x(algo_greaterB2)
	circuit.x(algo_greaterB0)


	circuit.x(algo_greaterA2)
	circuit.x(algo_greaterA1)
	circuit.x(algo_greaterB2)
	circuit.x(algo_greaterB1)
	circuit.x(algo_greaterB0)

	circuit.mcx([algo_greaterA2,algo_greaterB2,algo_greaterA1,algo_greaterB1,algo_greaterA0,algo_greaterB0],algo_greaterC0)

	circuit.x(algo_greaterA2)
	circuit.x(algo_greaterA1)
	circuit.x(algo_greaterB2)
	circuit.x(algo_greaterB1)
	circuit.x(algo_greaterB0)

	circuit.cswap(algo_greaterS,algo_greaterC0,qreg_outputCL0)
	circuit.cswap(algo_greaterS,algo_greaterC1,qreg_outputCL1)
	circuit.cswap(algo_greaterS,algo_greaterC2,qreg_outputCL2)

	
def qcAlgoAdd(circuit):
	circuit.cx(algo_addA0,algo_addC0)
	circuit.cx(algo_addB0,algo_addC0)

	circuit.cx(algo_addA1,algo_addC1)
	circuit.cx(algo_addB1,algo_addC1)
	circuit.mcx([algo_addA0,algo_addB0],algo_addC1)

	circuit.cx(algo_addA2,algo_addC2)
	circuit.cx(algo_addB2,algo_addC2)

	circuit.mcx([algo_addA1,algo_addB1],algo_addC2)
	circuit.mcx([algo_addA1,algo_addA0,algo_addB0],algo_addC2)
	circuit.mcx([algo_addA0,algo_addB0,algo_addB1],algo_addC2)

	circuit.mcx([algo_addA2,algo_addB2],algo_addC3)

	circuit.mcx([algo_addA2,algo_addA1,algo_addB1],algo_addC3)
	circuit.mcx([algo_addA2,algo_addA1,algo_addA0,algo_addB0],algo_addC3)
	circuit.mcx([algo_addA2,algo_addA0,algo_addB0,algo_addB1],algo_addC3)


	circuit.mcx([algo_addA1,algo_addB1,algo_addB2],algo_addC3)
	circuit.mcx([algo_addA1,algo_addA0,algo_addB0,algo_addB2],algo_addC3)
	circuit.mcx([algo_addA0,algo_addB0,algo_addB1,algo_addB2],algo_addC3)


	circuit.cswap(algo_addS,algo_addC0,qreg_outputCL0)
	circuit.cswap(algo_addS,algo_addC1,qreg_outputCL1)
	circuit.cswap(algo_addS,algo_addC2,qreg_outputCL2)
	circuit.cswap(algo_addS,algo_addC3,qreg_outputCU0)

def qcAlgoMul(circuit):
	circuit.mcx([algo_mulA0,algo_mulB0], algo_mulC0)

	circuit.mcx([algo_mulA1,algo_mulB0], algo_mulC1)
	circuit.mcx([algo_mulA0,algo_mulB1], algo_mulC1)

	circuit.mcx([algo_mulA1,algo_mulB0,algo_mulA0,algo_mulB1], algo_mulC2)
	circuit.mcx([algo_mulA2,algo_mulB0], algo_mulC2)
	circuit.mcx([algo_mulA1,algo_mulB1], algo_mulC2)
	circuit.mcx([algo_mulA0,algo_mulB2], algo_mulC2)

	circuit.mcx([algo_mulA2,algo_mulB1], algo_mulC3)
	circuit.mcx([algo_mulA1,algo_mulB2], algo_mulC3)
	circuit.mcx([algo_mulA2,algo_mulB0,algo_mulA1,algo_mulB1], algo_mulC3)
	circuit.mcx([algo_mulA1,algo_mulB1,algo_mulA0,algo_mulB2], algo_mulC3)
	circuit.mcx([algo_mulA2,algo_mulB0,algo_mulA0,algo_mulB2], algo_mulC3)

	circuit.mcx([algo_mulA2,algo_mulB0,algo_mulA1,algo_mulA0,algo_mulB1], algo_mulC3)
	circuit.mcx([algo_mulA1,algo_mulB1,algo_mulB0,algo_mulA0], algo_mulC3)
	circuit.mcx([algo_mulA0,algo_mulB2,algo_mulA1,algo_mulB0,algo_mulB1], algo_mulC3)


	circuit.mcx([algo_mulA2,algo_mulB2], algo_mulC4)
	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulA1,algo_mulB2], algo_mulC4)

	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulB0,algo_mulA1], algo_mulC4)
	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulA1,algo_mulA0,algo_mulB2], algo_mulC4)
	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulB0,algo_mulA0,algo_mulB2], algo_mulC4)

	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulB0,algo_mulA1,algo_mulA0], algo_mulC4)
	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulA1,algo_mulB0,algo_mulA0], algo_mulC4)
	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulA0,algo_mulB2,algo_mulA1,algo_mulB0], algo_mulC4)


	circuit.mcx([algo_mulA1,algo_mulB2,algo_mulA2,algo_mulB0,algo_mulB1], algo_mulC4)
	circuit.mcx([algo_mulA1,algo_mulB2,algo_mulB1,algo_mulA0], algo_mulC4)
	circuit.mcx([algo_mulA1,algo_mulB2,algo_mulA2,algo_mulB0,algo_mulA0], algo_mulC4)

	circuit.mcx([algo_mulA1,algo_mulB2,algo_mulA2,algo_mulB0,algo_mulA0,algo_mulB1], algo_mulC4)
	circuit.mcx([algo_mulA1,algo_mulB2,algo_mulB1,algo_mulB0,algo_mulA0], algo_mulC4)
	circuit.mcx([algo_mulA1,algo_mulB2,algo_mulA0,algo_mulB0,algo_mulB1], algo_mulC4)

	circuit.mcx([algo_mulA2,algo_mulB0,algo_mulA1,algo_mulB1,algo_mulA0,algo_mulB2], algo_mulC4)



	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulA1], algo_mulC5)

	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulB0,algo_mulA1], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulA1,algo_mulA0], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulB0,algo_mulA0], algo_mulC5)

	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulB0,algo_mulA1,algo_mulA0], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulA1,algo_mulB0,algo_mulA0], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB1,algo_mulA0,algo_mulA1,algo_mulB0], algo_mulC5)


	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulA1,algo_mulB0,algo_mulB1], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulA1,algo_mulB1,algo_mulA0], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulA1,algo_mulB0,algo_mulA0], algo_mulC5)

	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulA1,algo_mulB0,algo_mulA0,algo_mulB1], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulA1,algo_mulB1,algo_mulB0,algo_mulA0], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulA1,algo_mulA0,algo_mulB0,algo_mulB1], algo_mulC5)

	circuit.mcx([algo_mulA2,algo_mulB2,algo_mulB0,algo_mulA1,algo_mulB1,algo_mulA0], algo_mulC5)
	circuit.mcx([algo_mulA2,algo_mulB1,algo_mulA1,algo_mulB0,algo_mulA0], algo_mulC5)

	circuit.cswap(algo_mulS,algo_mulC0,qreg_outputCL0)
	circuit.cswap(algo_mulS,algo_mulC1,qreg_outputCL1)
	circuit.cswap(algo_mulS,algo_mulC2,qreg_outputCL2)

	circuit.cswap(algo_mulS,algo_mulC3,qreg_outputCU0)
	circuit.cswap(algo_mulS,algo_mulC4,qreg_outputCU1)
	circuit.cswap(algo_mulS,algo_mulC5,qreg_outputCU2)



def ModAlgo(circuit):
	qcAlgoAssign(circuit)

	qcAlgoFlip(circuit)
	qcAlgoMask(circuit)
	qcAlgoShift(circuit)
	qcAlgoEqual(circuit)
	qcAlgoGreater(circuit)
	qcAlgoAdd(circuit)
	qcAlgoMul(circuit)

