#!/usr/bin/env python

#--------------PSEUDO CODE -----------------#

# INPUT: the original data set S
# OUTPUT: the skyline of data set S
#
# 1:// Generation of local skyline points within each partitioned subspace
# 2: for all service sn in dataset S do
# 3: compute the coordinates of sn using formula given in paper
# 4: compute the partition Pi that sn belongs to based on the service sn's coordinate value
# 5: output (Pi , sn)
# 6: end for
# 7: for all partitioned sectors Pi do
# 8: compute local skyline LSi using BNL
# 9: output (Pi,LSi) in file st
# 10: end for
# 11: // Merging of Many Skyline subsets
# 12: for all service si in file st do
# 13: output(null,si)
# 14: end for
# 15: compute the global skyline GS using BNL
# 16: output(GS)

import os
import time
import sys
import numpy as np
from math import pow

##-------------- Division Job  ------------------##

# To convert point in spherical coordinates
def convert_point_in_spherical_coordinate(point,dim):
	result = [0]*dim
	temp_point =  np.square(point)
	reversed_arr = temp_point[::-1]
	cum_array = np.cumsum(reversed_arr)
	square_root_cum_array = np.sqrt(cum_array)
	reversed_square_root_cum_array = square_root_cum_array[::-1]
	temp_result = [0]*dim
	for i in range(1,dim):
		temp_result[i] = reversed_square_root_cum_array[i] / point[i-1]
	result = np.arctan(temp_result)
	result[0] = reversed_square_root_cum_array[0]
	# print result,reversed_square_root_cum_array
	return result

# To calculate the flag for partitioning
def calculateflag(point , dim , count):
	ans = [0]*(dim-1)
	for i in range(1,dim):
		for j in range(0,count):
			# print np.pi/count , j , point[i]
			if (point[i] < (np.pi/(2*count))*(j+1)) and (point[i] >= (np.pi/(2*count))*(j)):
				ans[i-1] = j+1
	return ans

# Mapping Task

if __name__ == '__main__':
	
	number_of_reducer = 3
	#Get data from stdin
	for line in sys.stdin:
		point = [int(x) for x in line.split()]
		point_in_spherical_coordinate = convert_point_in_spherical_coordinate(point , len(point))
		# print point,point_in_spherical_coordinate

		partition_flag = calculateflag(point_in_spherical_coordinate,len(point),number_of_reducer)
		flagnumber = int(''.join([str(x) for x in partition_flag]))

		print flagnumber,'\t',point



	
