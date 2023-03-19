import sys,os
sys.path.append('../')
from param import *

def ModOpaddr(circuit):
	circuit.mcx([opaddr0,opaddr1],opaddr2)
	circuit.cx(opaddr0,opaddr1)
	circuit.x(opaddr0)
