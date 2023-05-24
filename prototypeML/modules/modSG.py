from qiskit import transpile
from qiskit.visualization import plot_histogram
import sys,os
sys.path.append('../')
from param import *
from queue import Queue

from collections import OrderedDict

def ModSG(cregs,repo,mlMode):
	if(cregs[c_qreg_sg0] == '1'):
		repoRead = repo[int(cregs[c_qreg_a2] + cregs[c_qreg_a1] + cregs[c_qreg_a0],2)]
		c_qreg_phy_c2,c_qreg_phy_c1,c_qreg_phy_c0 = repoRead

	if(cregs[c_qreg_sg1] == '1'):
		repo[int(cregs[c_qreg_a2] + cregs[c_qreg_a1] + cregs[c_qreg_a0],2)] = [cregs[c_qreg_b2],cregs[c_qreg_b1],cregs[c_qreg_b0]]

	if(cregs[c_qreg_sg2] == '1'):#Learning mode
		mlMode = 1
		#print("Learning")
	else:#Mapping Mode
		mlMode = 0
		#print("Mapping")

	return mlMode