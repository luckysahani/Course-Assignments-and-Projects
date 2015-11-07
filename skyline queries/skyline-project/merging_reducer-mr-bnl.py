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

# Reduce Task
def divison_reducer(input_data):
	for flag_i in 
##-------------- Merging Job  ------------------##

# Map Task

# Reduce Task



if __name__ == '__main__':
	
	#Initialize all variables here
	data_tuple_with_flag=[]

	#Get data from stdin
	input_data = [[float(x) for x in line.split()] for line in sys.stdin]
	
	#initialize the dbit flag
	dbit_flag = numpy.median(input_data,axis=0)

	#printing dflag value
	print "Dbit flag is :",dbit_flag,"\n"

	#calling divison_mapper
	data_tuple_with_flag=divison_mapper()

	#printing the resultant mapping
	for data_tuple in data_tuple_with_flag:
		print data_tuple