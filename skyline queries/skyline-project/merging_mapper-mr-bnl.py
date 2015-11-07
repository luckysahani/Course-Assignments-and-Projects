#--------------PSEUDO CODE -----------------#

# INPUT: the original data set S
# OUTPUT: the skyline of data set S
#
# Division Job
# Map Task
# for each point P i in dataset S
# compute P i's subspace flag F i
# output (F i ,P i )
# Reduce Task
# for each subspace flag F i
# compute local Skyline SP k using BNL
# output (F i , SP k ) in file t

# Merging Job
# Map Task
# for each point P i in file t
# output (null, (F i , P i ))
# Reduce Task
# compute global Skyline SP k using BNL with pre-comparison
# output (SP k , null)

import os
import time
import sys
import numpy
import ast

##-------------- Merging Job  ------------------##
# Map Task
if __name__ == '__main__':

	with open('divison_job_reducer_output.txt') as f:
		for line in f:
			# remove leading and trailing whitespace
			line = line.strip()
			flag, point = line.split('\t')
			flag  = ast.literal_eval(flag)
			point  = ast.literal_eval(point)
			tuple = [flag,point]
			print None,'\t',tuple
			