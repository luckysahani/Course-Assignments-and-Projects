#!/usr/bin/env python

#--------------PSEUDO CODE -----------------#

# INPUT: the original data set S
# OUTPUT: the skyline of data set S
#
# Building Job
# Map Task
# for each point P i in data set S
# for each attribute A j in P i
# output (j, (A j , P i 's byte offsets))
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

##-------------- Building Job  ------------------##

# #to calculate an attribute byte offset
# def calculate_byte_offset(attribute_i):
# 	# return ((int(attribute_i)).bit_length() + 7 )/8
# 	# return (int(attribute_i)).bit_length()
# 	return None

# Mapping Task
if __name__ == '__main__':
	
	
	# Get data from stdin
	input_data = [[float(x) for x in line.split(',')] for line in sys.stdin]
	

	# #Storing number of dimensions
	# dim = len(input_data[0])
	
	# # Store maximum value of each dimension in this variable
	# max_val = [0]*dim 

	# # Calculate the max value from input data
	# for point in input_data:
	# 	for i in range(0,len(point)):


	for j in range(0,len(input_data)):
		point = input_data[j] 
		for i in range(0,len(point)):
			k = int(point[i]*100000)
			print i,"\t",[k,j]
