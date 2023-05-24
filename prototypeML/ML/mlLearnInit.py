from mlParam import *
import numpy as np
from math import pi
def ML_LearnInit():

	a = np.loadtxt('trainingSet.txt',comments='#')
	a = a.reshape((ML_NUM_MODEL,ML_NUM_GROUP,ML_NUM_PX,ML_NUM_COE))


	for i in range(ML_NUM_MODEL):#8 8 set
		for m in range(ML_NUM_GROUP):#4 group
			for n in range(ML_NUM_PX):#4 pixel
				for j in range(ML_NUM_COE):		
					a[i][m][n][j] = pi*a[i][m][n][j]/255

	return a
		