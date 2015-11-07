#--------------PSEUDO CODE -----------------#

# INPUT: the original data set S
# OUTPUT: the skyline of data set S
#
# Building Job
# Map Task
# for each point P i in data set S
# for each attribute A j in P i
# output (j, (A j , P i ’s byte offsets))
# Reduce Task
# for each dimension k
# generate sorted attribute list L k in descending order
# for each distinct value v in L k
# generate bit-slice and write to HDFS

# Examining Job
# Map Task
# for each point P i in data set S
# assign P i to a reducer R i
# Reduce Task
# for each reducer R i
# load bitmap b into memory as much as possible
# for each point P i in R i
# check P i using bitmap b

import os
import time
import sys
import numpy
from math import pow

##-------------- Division Job  ------------------##

# Mapping Task
def divison_mapper():
	for point_i in input_data:
		flag_i = calculate_subspace_flag(point_i)
		flagnumber = calculate_flagnumber_from_flag_i(flag_i)
		print flagnumber,'\t',point_i

#To calculate the subspace flag number for each point
def calculate_flagnumber_from_flag_i(flag_i):
	flagnumber=0
	for i in range(0,len(flag_i)):
		flagnumber=flagnumber+flag_i[i]*pow(2, len(flag_i) - i - 1)
	return flagnumber

#To calculate the subspace flag of each point
def calculate_subspace_flag(point):
	result_flag=point[:]
	for i in range(0,len(point)):
		if(point[i]>dbit_flag[i]):
			result_flag[i]=1
		else:
			result_flag[i]=0
	return result_flag

if __name__ == '__main__':
	
	#Get data from stdin
	input_data = [[float(x) for x in line.split()] for line in sys.stdin]
	
	#initialize the dbit flag
	dbit_flag = numpy.median(input_data,axis=0)

	#calling divison_mapper
	divison_mapper()
