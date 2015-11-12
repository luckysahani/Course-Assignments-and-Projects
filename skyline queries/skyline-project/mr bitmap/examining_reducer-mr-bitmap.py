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
import ast
import BitVector
from operator import itemgetter

##-------------- Examining Job  ------------------##
# Hadoop sorts mapper output by key (here: flag) before it is passed to the reducer
# Reduce Task
if __name__ == '__main__':

	bitmap = {}
	with open('building_job_reducer_output.txt') as f:
		for line in f:
			dim, val, bitval = line.split('\t')
			dim = ast.literal_eval(dim)
			val = ast.literal_eval(val)
			bitval = ast.literal_eval(bitval)
			if not(dim in bitmap):
				bitmap[dim]={}
			bitmap[dim][val]=BitVector.BitVector(bitlist = bitval) 
			# bitmap.setdefault(dim, []).append([val,bitval])
	# print bitmap

	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
		
		reducer, point = line.split('\t')
		point = ast.literal_eval(point)
		print '\n\n',point

		for i in range(0,len(point)):
			bitvalue = bitmap[i][point[i]]
			print bitvalue
			

		