from mlParam import *
import numpy as np
from math import pi
def ML_SampleInit():

	a = np.loadtxt('sample.txt',comments='#')
	a = a.reshape((ML_NUM_MODEL,ML_NUM_PX,ML_NUM_COE))


	for i in range(ML_NUM_MODEL):#8
		for n in range(ML_NUM_PX):#4
			for j in range(ML_NUM_COE):		
				a[i][n][j] = pi*a[i][n][j]/255

	return a
	