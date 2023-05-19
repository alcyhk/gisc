import numpy as np
from mlParam import *

sample = np.empty((NUM_PICS,NUM_PX,NUM_COE))

sample[NOT][0] = [9,230,255]
sample[NOT][1] = [9,230,255]
sample[NOT][2] = [9,230,255]
sample[NOT][3] = [9,230,255]

imagePx = [[0]*NUM_COE]*NUM_PX

sample[BAD][0] = [128,0,112]
sample[BAD][1] = [30,100,132]
sample[BAD][2] = [150,20,16]
sample[BAD][3] = [50,40,10]

sample[KINDA0][0] = [128,0,112]
sample[KINDA0][1] = [130,100,132]
sample[KINDA0][2] = [150,20,160]
sample[KINDA0][3] = [150,40,100]

sample[KINDA1][0] = [128,0,112]
sample[KINDA1][1] = [130,100,132]
sample[KINDA1][2] = [150,20,160]
sample[KINDA1][3] = [150,40,100]

sample[KINDA2][0] = [128,0,112]
sample[KINDA2][1] = [130,100,132]
sample[KINDA2][2] = [150,20,160]
sample[KINDA2][3] = [150,40,100]

sample[GOOD][0] = [150,40,122]
sample[GOOD][1] = [137,26,122]
sample[GOOD][2] = [129,19,122]
sample[GOOD][3] = [133,26,122]

sample[PERFECT][0] = [137,26,122]
sample[PERFECT][1] = [137,26,122]
sample[PERFECT][2] = [137,26,122]
sample[PERFECT][3] = [137,26,122]
