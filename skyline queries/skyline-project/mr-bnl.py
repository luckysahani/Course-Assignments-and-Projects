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

##-------------- Division Job  ------------------##

# Map Task
def divison_mapper(input_data):
	for point_i in input_data:
		flag_i = calculate_subspace_flag(point_i)

# Reduce Task


##-------------- Merging Job  ------------------##

# Map Task

# Reduce Task


#To calculate the subspace flag of each point
def calculate_subspace_flag(point):
	for i in range(0,len(point)):
		if(point[i]>dbit_flag[i]):
			result_flag[i]=1
		else:
			result_flag[i]=0
	return result_flag

if __name__ == '__main__':
	
	#inputfile initialized
	inputfile="sample_data_1.txt"

	#Get data from input file
	with open(inputfile) as f:
		data_list = [[float(x) for x in line.split()] for line in f]

	#initialize the dbit flag
	dbit_flag = numpy.median(data_list,axis=0)

	#printing dflag value
	print "Dbit flag is :",dbit_flag,"\n"