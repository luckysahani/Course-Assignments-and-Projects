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



##-------------- Building Job  ------------------##
# Hadoop sorts mapper output by key (here: flag) before it is passed to the reducer
# Reduce Task
if __name__ == '__main__':

	#Create a new file to store the output
	fo = open("building_job_reducer_output.txt", "w+");
	fo.truncate();

	# Variables used in thsi algorithm
	current_dim = -1
	dim = -1
	input_set_for_each_dim= []

	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
		dim, tuple = line.split('\t')
		dim  = ast.literal_eval(flag)
		tuple  = ast.literal_eval(tuple)

		#print flag,tuple
		
		# Reduce Task
		if current_dim == dim :
			input_set_for_each_dim.append(tuple)
		else :
			if current_flag != -1 :




				#write skylines to a file
				with open("building_job_reducer_output.txt", "a") as myfile:
					for skyline in skylines:
						myfile.write(str(current_flag)+'\t'+str(skyline)+'\n')
				for skyline in skylines:	
					print current_flag,'\t',skyline
			input_set_for_each_dim = []
			skylines = []
			current_dim = dim
			

			input_set_for_each_dim.append(tuple)

	# To output the skylines out of the remaining input to be processed
	if current_dim == dim :
		#print "Input Set = ",input_set_for_each_dim
		



		with open("building_job_reducer_output.txt", "a") as myfile:
			for skyline in skylines:
				myfile.write(str(current_flag)+'\t'+str(skyline)+'\n')
		for skyline in skylines:
			print current_flag,'\t',skyline
