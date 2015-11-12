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
		dim  = ast.literal_eval(dim)
		tuple  = ast.literal_eval(tuple)
		# attribute = tuple[0]

		# print dim,tuple
		
		#Reduce Task
		if current_dim == dim :
			input_set_for_each_dim.append(tuple)
		else :
			if current_dim != -1 :
				distinct_input_set = list (set ([attr[0] for attr in input_set_for_each_dim]))
				sorted_distinct_input_set = sorted( distinct_input_set )
				number_of_distinct_elements = len(sorted_distinct_input_set)
				# print current_dim,sorted_distinct_input_set,number_of_distinct_elements

				dictionary_with_bitvector = {}

				for i in range(0,number_of_distinct_elements):
					a = BitVector.BitVector( size = number_of_distinct_elements )
					for j in range(number_of_distinct_elements - i - 1,number_of_distinct_elements):
						a[j]=1
					dictionary_with_bitvector[sorted_distinct_input_set[i]]=a


				array_of_all_bitvectors = []
				sorted_input_set_for_each_dim=sorted(input_set_for_each_dim,key=itemgetter(1))
				# print sorted_input_set_for_each_dim
				for i in range(0,len(sorted_input_set_for_each_dim)):
					array_of_all_bitvectors.append(dictionary_with_bitvector[sorted_input_set_for_each_dim[i][0]])
				# for i in array_of_all_bitvectors:
				# 	print i

				bitslice={}
				for i in range(0,len(sorted_distinct_input_set)):
					index = number_of_distinct_elements - i-1 
					# print sorted_distinct_input_set[number_of_distinct_elements-1]
					bitslice[sorted_distinct_input_set[index]]=[row[i] for row in array_of_all_bitvectors]
					# print index,bitslice[index]
				
				# write bitmap to a file
				with open("building_job_reducer_output.txt", "a") as myfile:
					for key, value in bitslice.iteritems():
						myfile.write(str(current_dim)+'\t'+str(key)+'\t'+str(value)+'\n')
				for key, value in bitslice.iteritems():	
					print current_dim,'\t',key,'\t',value
			input_set_for_each_dim = []
			current_dim = dim
			input_set_for_each_dim.append(tuple)

	# To output the key value pair along with dimension to be processed for calculating skyline
	if current_dim == dim :
		distinct_input_set = list (set ([attr[0] for attr in input_set_for_each_dim]))
		sorted_distinct_input_set = sorted( distinct_input_set )
		number_of_distinct_elements = len(sorted_distinct_input_set)
		# print current_dim,sorted_distinct_input_set,number_of_distinct_elements

		dictionary_with_bitvector = {}

		for i in range(0,number_of_distinct_elements):
			a = BitVector.BitVector( size = number_of_distinct_elements )
			for j in range(number_of_distinct_elements - i - 1,number_of_distinct_elements):
				a[j]=1
			dictionary_with_bitvector[sorted_distinct_input_set[i]]=a


		array_of_all_bitvectors = []
		sorted_input_set_for_each_dim=sorted(input_set_for_each_dim,key=itemgetter(1))
		# print sorted_input_set_for_each_dim
		for i in range(0,len(sorted_input_set_for_each_dim)):
			array_of_all_bitvectors.append(dictionary_with_bitvector[sorted_input_set_for_each_dim[i][0]])
		# for i in array_of_all_bitvectors:
		# 	print i

		bitslice={}
		for i in range(0,len(sorted_distinct_input_set)):
			index = number_of_distinct_elements - i-1 
			# print sorted_distinct_input_set[number_of_distinct_elements-1]
			bitslice[sorted_distinct_input_set[index]]=[row[i] for row in array_of_all_bitvectors]
			# print index,bitslice[index]
		
		# write bitmap to a file
		with open("building_job_reducer_output.txt", "a") as myfile:
			for key, value in bitslice.iteritems():
				myfile.write(str(current_dim)+'\t'+str(key)+'\t'+str(value)+'\n')
		for key, value in bitslice.iteritems():	
			print current_dim,'\t',key,'\t',value
