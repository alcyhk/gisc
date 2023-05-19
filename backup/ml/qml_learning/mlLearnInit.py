from mlLearnParam import *
import numpy as np
from math import pi
def ML_LearnInit(trainPx):
	for n in range(NUM_GROUP):
	
		trainPx[0][n] = [[127.5,0,127.5],
				[127.5,0,127.5],
				[127.5,0,127.5],
				[127.5,0,127.5]
			]
			
	for n in range(NUM_GROUP):
		trainPx[1][n] = [[255,0,0],
				[255,0,0],
				[255,0,0],
				[255,0,0]
			]
	for n in range(NUM_GROUP):
		trainPx[2][n] = [[0,255,0],
				[0,255,0],
				[0,255,0],
				[0,255,0]
			]
	for n in range(NUM_GROUP):
		trainPx[3][n] = [[0,0,255],
				[0,0,255],
				[0,0,255],
				[0,0,255]
			]
			
			
	for n in range(NUM_GROUP):
		trainPx[4][n] = [[255,255,0],
				[255,255,0],
				[255,255,0],
				[255,255,0]
			]
	for n in range(NUM_GROUP):
		trainPx[5][n] = [[0,255,255],
				[0,255,255],
				[0,255,255],
				[0,255,255]
			]
	for n in range(NUM_GROUP):
		trainPx[6][n] = [[0,255,255],
				[0,255,255],
				[0,255,255],
				[0,255,255]
			]
			
	for n in range(NUM_GROUP):
		trainPx[7][n] = [[255,255,255],
				[255,255,255],
				[255,255,255],
				[255,255,255]
			]

	for i in range(8):
		for m in range(4):
			for n in range(4):
				for j in range(3):		
					trainPx[i][m][n][j] = pi*trainPx[i][m][n][j]/255
		