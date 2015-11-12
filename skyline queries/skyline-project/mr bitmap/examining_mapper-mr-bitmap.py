#!/usr/bin/env python

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
import ast

##-------------- Merging Job  ------------------##
# Map Task
if __name__ == '__main__':

	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
		flag, point = line.split('\t')
		flag  = ast.literal_eval(flag)
		point  = ast.literal_eval(point)
		tuple = [flag,point]
		print None,'\t',tuple
			