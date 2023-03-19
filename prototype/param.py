from qiskit import QuantumRegister, ClassicalRegister

def ParamInit():
	global OP_SET,OP_CPY,OP_PHY,OP_FLY, \
	QUB_REGA,QUB_REGB,QUB_SG,QUB_INPUTA,QUB_INPUTB,QUB_INPUTS,QUB_OUTPUTCL,QUB_OUTPUTCU,\
	VAL_ZERO,VAL_ONE,VAL_TWO,VAL_THREE,VAL_FOUR,VAL_FIVE,VAL_SIX,VAL_SEVEN, \
	FIFO_TX_SIZE, FIFO_RX_SIZE

	global maxNumOfRuns, NUM_OF_CREGS,\
		opaddr0,opaddr1,opaddr2, \
		isa0,isa1,isa2,isa3,isa4,isa5,isa6,isa7, \
		dmy0,dmy1,dmy2, \
		op_set,op_cpy,op_phy,op_fly, \
		opa_regA,opa_regB,opa_SG,opa_inputA,opa_inputB,opa_inputS,opa_outputCL,opa_outputCU, \
		opb_regA,opb_regB,opb_SG,opb_inputA,opb_inputB,opb_inputS,opb_outputCL,opb_outputCU, \
		qreg_a0,qreg_a1,qreg_a2, \
		qreg_b0,qreg_b1,qreg_b2, \
		qreg_sg0,qreg_sg1,qreg_sg2, \
		qreg_inputA0,qreg_inputA1,qreg_inputA2, \
		qreg_inputB0,qreg_inputB1,qreg_inputB2, \
		qreg_inputS0,qreg_inputS1,qreg_inputS2, \
		qreg_outputCL0,qreg_outputCL1,qreg_outputCL2, \
		qreg_outputCU0,qreg_outputCU1,qreg_outputCU2, \
		opb_phy_regA,opb_phy_regB,opb_phy_regC,opb_phy_regD,opb_phy_regE,opb_phy_regF,opb_phy_regG,opb_phy_regH, \
		qreg_phy_a0,qreg_phy_a1,qreg_phy_a2, \
		qreg_phy_b0,qreg_phy_b1,qreg_phy_b2, \
		qreg_phy_c0,qreg_phy_c1,qreg_phy_c2, \
		qreg_phy_d0,qreg_phy_d1,qreg_phy_d2, \
		qreg_phy_e0,qreg_phy_e1,qreg_phy_e2, \
		qreg_phy_f0,qreg_phy_f1,qreg_phy_f2, \
		qreg_phy_g0,qreg_phy_g1,qreg_phy_g2, \
		qreg_phy_h0,qreg_phy_h1,qreg_phy_h2, \
		op_swap_regA,op_swap_regB,op_swap_SG,op_swap_inputA,op_swap_inputB,op_swap_inputS,op_swap_outputCL,op_swap_outputCU, \
		op_jmp_swap, \
		c_opaddr0,c_opaddr1,c_opaddr2, \
		c_isa0,c_isa1,c_isa2,c_isa3,c_isa4,c_isa5,c_isa6,c_isa7, \
		c_op_fly,c_op_set,c_op_cpy,c_op_phy, \
		c_dmy0,c_dmy1,c_dmy2, \
		c_qreg_a0,c_qreg_a1,c_qreg_a2, \
		c_qreg_b0,c_qreg_b1,c_qreg_b2, \
		c_qreg_sg0,c_qreg_sg1,c_qreg_sg2, \
		c_qreg_inputA0,c_qreg_inputA1,c_qreg_inputA2, \
		c_qreg_inputB0,c_qreg_inputB1,c_qreg_inputB2, \
		c_qreg_inputS0,c_qreg_inputS1,c_qreg_inputS2, \
		c_qreg_outputCL0,c_qreg_outputCL1,c_qreg_outputCL2, \
		c_qreg_outputCU0,c_qreg_outputCU1,c_qreg_outputCU2, \
		c_qreg_phy_a0,c_qreg_phy_a1,c_qreg_phy_a2, \
		c_qreg_phy_b0,c_qreg_phy_b1,c_qreg_phy_b2, \
		c_qreg_phy_c0,c_qreg_phy_c1,c_qreg_phy_c2, \
		c_qreg_phy_d0,c_qreg_phy_d1,c_qreg_phy_d2, \
		c_qreg_phy_e0,c_qreg_phy_e1,c_qreg_phy_e2, \
		c_qreg_phy_f0,c_qreg_phy_f1,c_qreg_phy_f2, \
		c_qreg_phy_g0,c_qreg_phy_g1,c_qreg_phy_g2, \
		c_qreg_phy_h0,c_qreg_phy_h1,c_qreg_phy_h2 
#---------------------------------
	maxNumOfRuns = 10
	NUM_OF_CREGS = 66
	FIFO_TX_SIZE = 8
	FIFO_RX_SIZE = 8


#---------------------------------

	OP_SET = "01"
	OP_CPY = "10"
	OP_PHY = "11"
	OP_FLY = "00"

	QUB_REGA 	= "000"
	QUB_REGB 	= "001"
	QUB_SG   	= "010"
	QUB_INPUTA 	= "011"
	QUB_INPUTB 	= "100"
	QUB_F_CON 	= "011"
	QUB_F_POS 	= "100"

	QUB_INPUTS 	= "101"
	QUB_OUTPUTCL= "110"
	QUB_OUTPUTCU= "111"

	VAL_ZERO 	= "000"
	VAL_ONE 	= "001"
	VAL_TWO   = "010"
	VAL_THREE 	= "011"
	VAL_FOUR 	= "100"
	VAL_FIVE 	= "101"
	VAL_SIX	= "110"
	VAL_SEVEN	= "111"
#---------------------------------


		
	opaddr0 = 0
	opaddr1 = 1
	opaddr2 = 2

	isa0    = 3
	isa1    = 4
	isa2    = 5
	isa3    = 6

	isa4    = 7
	isa5    = 8
	isa6    = 9
	isa7    = 10

	dmy0    = 11
	dmy1    = 12
	dmy2    = 13

	op_set    = 14
	op_cpy    = 15
	op_phy    = 16
	op_fly    = 17

	opa_regA     = 18
	opa_regB     = 19
	opa_SG       = 20
	opa_inputA   = 21
	opa_inputB   = 22
	opa_inputS   = 23
	opa_outputCL = 24
	opa_outputCU = 25

	opb_regA     = 26
	opb_regB     = 27
	opb_SG       = 28
	opb_inputA   = 29
	opb_inputB   = 30
	opb_inputS   = 31
	opb_outputCL = 32
	opb_outputCU = 33


	qreg_a0          = 34
	qreg_a1          = 35
	qreg_a2          = 36
	qreg_b0          = 37
	qreg_b1          = 38
	qreg_b2          = 39
	qreg_sg0         = 40
	qreg_sg1         = 41
	qreg_sg2         = 42
	qreg_inputA0     = 43
	qreg_inputA1     = 44
	qreg_inputA2     = 45
	qreg_inputB0     = 46
	qreg_inputB1     = 47
	qreg_inputB2     = 48
	qreg_inputS0     = 49
	qreg_inputS1     = 50
	qreg_inputS2     = 51
	qreg_outputCL0   = 52
	qreg_outputCL1   = 53
	qreg_outputCL2   = 54
	qreg_outputCU0   = 55
	qreg_outputCU1   = 56
	qreg_outputCU2   = 57
	opb_phy_regA         = 58
	opb_phy_regB         = 59
	opb_phy_regC         = 60
	opb_phy_regD         = 61
	opb_phy_regE         = 62
	opb_phy_regF         = 63
	opb_phy_regG         = 64
	opb_phy_regH         = 65
	qreg_phy_a0        = 66
	qreg_phy_a1        = 67
	qreg_phy_a2        = 68
	qreg_phy_b0        = 69 
	qreg_phy_b1        = 70
	qreg_phy_b2        = 71
	qreg_phy_c0        = 72
	qreg_phy_c1        = 73
	qreg_phy_c2        = 74
	qreg_phy_d0        = 75
	qreg_phy_d1        = 76
	qreg_phy_d2        = 77
	qreg_phy_e0        = 78
	qreg_phy_e1        = 79
	qreg_phy_e2        = 80
	qreg_phy_f0        = 81
	qreg_phy_f1        = 82
	qreg_phy_f2        = 83
	qreg_phy_g0        = 84
	qreg_phy_g1        = 85
	qreg_phy_g2        = 86
	qreg_phy_h0        = 87
	qreg_phy_h1        = 88
	qreg_phy_h2        = 89
	op_swap_regA     = 90
	op_swap_regB     = 91
	op_swap_SG       = 92
	op_swap_inputA   = 93
	op_swap_inputB   = 94
	op_swap_inputS   = 95
	op_swap_outputCL = 96
	op_swap_outputCU = 97
	op_jmp_swap      = 98

	#classical registers
	c_opaddr0 = 0
	c_opaddr1 = 1
	c_opaddr2 = 2

	c_qreg_a0 = 3
	c_qreg_a1 = 4
	c_qreg_a2 = 5

	c_qreg_b0 = 6
	c_qreg_b1 = 7
	c_qreg_b2 = 8

	c_qreg_sg0 = 9
	c_qreg_sg1 = 10
	c_qreg_sg2 = 11

	c_qreg_inputA0   = 12
	c_qreg_inputA1   = 13
	c_qreg_inputA2   = 14
	c_qreg_inputB0   = 15
	c_qreg_inputB1   = 16
	c_qreg_inputB2   = 17
	c_qreg_inputS0   = 18
	c_qreg_inputS1   = 19
	c_qreg_inputS2   = 20
	c_qreg_outputCL0 = 21
	c_qreg_outputCL1 = 22
	c_qreg_outputCL2 = 23
	c_qreg_outputCU0 = 24
	c_qreg_outputCU1 = 25
	c_qreg_outputCU2 = 26

	c_isa0    = 27
	c_isa1    = 28
	c_isa2    = 29
	c_isa3    = 30

	c_isa4    = 31
	c_isa5    = 32
	c_isa6    = 33
	c_isa7    = 34

	c_op_fly    = 35
	c_op_set    = 36
	c_op_cpy    = 37
	c_op_phy    = 38

	c_dmy0    = 39
	c_dmy1    = 40
	c_dmy2    = 41

	c_qreg_phy_a0   = 42
	c_qreg_phy_a1   = 43
	c_qreg_phy_a2   = 44
	c_qreg_phy_b0   = 45
	c_qreg_phy_b1   = 46
	c_qreg_phy_b2   = 47
	c_qreg_phy_c0   = 48
	c_qreg_phy_c1   = 49
	c_qreg_phy_c2   = 50
	c_qreg_phy_d0   = 51
	c_qreg_phy_d1   = 52
	c_qreg_phy_d2   = 53
	c_qreg_phy_e0   = 54
	c_qreg_phy_e1   = 55
	c_qreg_phy_e2   = 56
	c_qreg_phy_f0   = 57
	c_qreg_phy_f1   = 58
	c_qreg_phy_f2   = 59
	c_qreg_phy_g0   = 60
	c_qreg_phy_g1   = 61
	c_qreg_phy_g2   = 62
	c_qreg_phy_h0   = 63
	c_qreg_phy_h1   = 64
	c_qreg_phy_h2   = 65


def ParamInitAlgo():
	global \
	algo_flipA0,algo_flipA1,algo_flipA2, \
	algo_flipB0,algo_flipB1,algo_flipB2, \
	algo_flipC0,algo_flipC1,algo_flipC2, \
	algo_flipS, \
	algo_maskA0,algo_maskA1,algo_maskA2, \
	algo_maskB0,algo_maskB1,algo_maskB2, \
	algo_maskC0,algo_maskC1,algo_maskC2, \
	algo_maskS, \
	algo_shiftA0,algo_shiftA1,algo_shiftA2, \
	algo_shiftB0,algo_shiftB1,algo_shiftB2, \
	algo_shiftC0,algo_shiftC1,algo_shiftC2,algo_shiftD0,algo_shiftD1, \
	algo_shiftS, \
	algo_equalA0,algo_equalA1,algo_equalA2, \
	algo_equalB0,algo_equalB1,algo_equalB2, \
	algo_equalC0,algo_equalC1,algo_equalC2,algo_equalD0, \
	algo_equalS, \
	algo_greaterA0,algo_greaterA1,algo_greaterA2, \
	algo_greaterB0,algo_greaterB1,algo_greaterB2, \
	algo_greaterC0,algo_greaterC1,algo_greaterC2, \
	algo_greaterS, \
	algo_addA0,algo_addA1,algo_addA2, \
	algo_addB0,algo_addB1,algo_addB2, \
	algo_addC0,algo_addC1,algo_addC2,algo_addC3, \
	algo_addS, \
	algo_mulA0,algo_mulA1,algo_mulA2, \
	algo_mulB0,algo_mulB1,algo_mulB2, \
	algo_mulC0,algo_mulC1,algo_mulC2,algo_mulC3,algo_mulC4,algo_mulC5, \
	algo_mulS


	algo_flipA0    = 99
	algo_flipA1    = 100
	algo_flipA2    = 101
	algo_flipB0    = 102
	algo_flipB1    = 103
	algo_flipB2    = 104
	algo_flipC0    = 105
	algo_flipC1    = 106
	algo_flipC2    = 107
	algo_maskA0    = 108
	algo_maskA1    = 109
	algo_maskA2    = 110
	algo_maskB0    = 111
	algo_maskB1    = 112
	algo_maskB2    = 113
	algo_maskC0    = 114
	algo_maskC1    = 115
	algo_maskC2    = 116
	algo_shiftA0   = 117
	algo_shiftA1   = 118
	algo_shiftA2   = 119
	algo_shiftB0   = 120
	algo_shiftB1   = 121
	algo_shiftB2   = 122
	algo_shiftC0   = 123
	algo_shiftC1   = 124
	algo_shiftC2   = 125
	algo_shiftD0   = 126
	algo_shiftD1   = 127
	algo_equalA0   = 128
	algo_equalA1   = 129
	algo_equalA2   = 130
	algo_equalB0   = 131
	algo_equalB1   = 132
	algo_equalB2   = 133
	algo_equalC0   = 134
	algo_equalC1   = 135
	algo_equalC2   = 136
	algo_equalD0   = 137
	algo_greaterA0 = 138
	algo_greaterA1 = 139
	algo_greaterA2 = 140
	algo_greaterB0 = 141
	algo_greaterB1 = 142
	algo_greaterB2 = 143
	algo_greaterC0 = 144
	algo_greaterC1 = 145
	algo_greaterC2 = 146
	algo_addA0     = 147
	algo_addA1     = 148
	algo_addA2     = 149
	algo_addB0     = 150
	algo_addB1     = 151
	algo_addB2     = 152
	algo_addC0     = 153
	algo_addC1     = 154
	algo_addC2     = 155
	algo_addC3     = 156
	algo_mulA0     = 157
	algo_mulA1     = 158
	algo_mulA2     = 159
	algo_mulB0     = 160
	algo_mulB1     = 161
	algo_mulB2     = 162
	algo_mulC0     = 163
	algo_mulC1     = 164
	algo_mulC2     = 165
	algo_mulC3     = 166
	algo_mulC4     = 167
	algo_mulC5     = 168
	algo_idleS     = 169
	algo_flipS     = 170
	algo_maskS     = 171
	algo_shiftS    = 172
	algo_equalS    = 173
	algo_greaterS  = 174
	algo_addS      = 175
	algo_mulS      = 176



def ParamQcRegsInit(circuit):	
	qr = QuantumRegister(1,'opaddr0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opaddr1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opaddr2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'isa0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'isa1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'isa2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'isa3')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'isa4')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'isa5')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'isa6')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'isa7')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'dmy0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'dmy1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'dmy2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'op_set')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_cpy')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_phy')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_fly')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'opa_regA')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opa_regB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opa_SG')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opa_inputA')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'opa_inputB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opa_inputS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opa_outputCL')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opa_outputCU')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'opb_regA')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_regB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_SG')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_inputA')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'opb_inputB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_inputS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_outputCL')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_outputCU')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_a0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_a1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_a2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_b0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_b1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_b2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_sg0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_sg1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_sg2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_inputA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_inputA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_inputA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_inputB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_inputB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_inputB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_inputS0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_inputS1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_inputS2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_outputCL0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_outputCL1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_outputCL2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_outputCU0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_outputCU1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_outputCU2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'opb_phy_regA')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_phy_regB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_phy_regC')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_phy_regD')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'opb_phy_regE')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_phy_regF')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_phy_regG')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'opb_phy_regH')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_phy_a0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_a1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_a2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_b0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_b1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_b2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_phy_c0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_c1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_c2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_d0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_d1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_d2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_phy_e0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_e1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_e2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_f0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_f1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_f2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'qreg_phy_g0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_g1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_g2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_h0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_h1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'qreg_phy_h2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'op_swap_regA')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_swap_regB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_swap_SG')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_swap_inputA')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'op_swap_inputB')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_swap_inputS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_swap_outputCL')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_swap_outputCU')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'op_jmp_swap')
	circuit.add_register( qr )

	
	qr = QuantumRegister(1,'algo_flipA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_flipB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_flipC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipC2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_maskA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_maskB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_maskC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskC2')
	circuit.add_register( qr )

	#------------------------
	qr = QuantumRegister(1,'algo_shiftA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_shiftB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_shiftC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftC2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftD0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftD1')
	circuit.add_register( qr )

	#------------------------
	qr = QuantumRegister(1,'algo_equalA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_equalB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_equalC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalC2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalD0')
	circuit.add_register( qr )

	#------------------------
	qr = QuantumRegister(1,'algo_greaterA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_greaterB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_greaterC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterC2')
	circuit.add_register( qr )

	#------------------------
	qr = QuantumRegister(1,'algo_addA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_addB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_addC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addC2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addC3')
	circuit.add_register( qr )

	#------------------------
	qr = QuantumRegister(1,'algo_mulA0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulA1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulA2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_mulB0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulB1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulB2')
	circuit.add_register( qr )

	qr = QuantumRegister(1,'algo_mulC0')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulC1')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulC2')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulC3')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulC4')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulC5')
	circuit.add_register( qr )
	
	qr = QuantumRegister(1,'algo_idleS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_flipS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_maskS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_shiftS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_equalS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_greaterS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_addS')
	circuit.add_register( qr )
	qr = QuantumRegister(1,'algo_mulS')
	circuit.add_register( qr )

	



	cr = ClassicalRegister(NUM_OF_CREGS,'cr')
	circuit.add_register( cr )

ParamInit()
ParamInitAlgo()
