#!/usr/bin/env python

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
from math import pow

# To check whether the two flags can be compared or not
def iscomparable_flag(element_1,element_2):
	flag1=0;
	flag2=0;
	try:
		for i in range(0,len(element_1)):
			if((element_1[i]-element_2[i])>0):
				if(flag2==1):
					return False;
				flag1 = 1;
			elif((element_1[i]-element_2[i])<0):
				if(flag1==1):
					return False;
				flag2 = 1;
		return True
	except:
		print element_1,element_2

# To compare two numbers and return which one is dominant over other 
def compare(element_1,element_2):
	if(iscomparable_flag(element_1[0],element_2[0]) == True):
		flag1=0;
		flag2=0;
		for i in range(0,len(element_1[1][1])):
			if((element_1[1][1][i]-element_2[1][1][i])>0):
				if(flag2==1):
					return 0;
				flag1 = 1;
			elif((element_1[1][1][i]-element_2[1][1][i])<0):
				if(flag1==1):
					return 0;
				flag2 = 1;
		if(flag1 == 1 and flag2 == 0):
			return 2
		else :
			return 1
	else:
		return 0

#Initialize variables for BNL
def initialize_var():
	global window_data,timestamp,file_counter,flag3,window_maxsize,data_list,skylines;
	window_maxsize=1000;
	window_data=[];
	data_list=[];
	skylines=[];
	timestamp=0;
	file_counter=0;
	flag3=0;

# To find skyline using Block Nested Loop Algorithm
def find_skylines_using_BNL(sample_data):
	#print sample_data
	global window_data,timestamp,file_counter,flag3;
	temp_data_list=[];
	flag3=0;
	all_skyline_before_time=0;
	data_tuple_with_timestamp=[];
	for data in sample_data:
		timestamp=timestamp+1;
		data_tuple_with_timestamp.append([data[0],[timestamp,data[1]]]);
	for data in data_tuple_with_timestamp:
		#print "Window data is :",window_data,"\n","Data to be compared is :",data
		if(len(window_data)==0):
			window_data.append(data);
		else:
			topush_data=False;
			new_window_data=[];
			for i in xrange(0,len(window_data)): 
				element=window_data[i];
				compare_result = compare(data,element);
				#print "Comparing data :",data," and element :",element," and result is :",compare_result
				if (compare_result == 1):
					topush_data=True;
				elif (compare_result == 2):
					topush_data=False;
					for j in range(i,len(window_data)) :
						new_window_data.append(window_data[j]);
					break;
				elif (compare_result == 0):
					topush_data=True;
					new_window_data.append(window_data[i]);
			if(topush_data==True):
				if(len(new_window_data)<window_maxsize):
					new_window_data.append(data);
				else:
					if(flag3==0):
						all_skyline_before_time=data[1][0];
						flag3=1;
					temp_data_list.append([data[0],data[1][1]])
			window_data=new_window_data;
	if(len(temp_data_list)== 0):
		for data in window_data:
			skylines.append(data[1][1]);
	else:
		new_window_data=[];
		for data in window_data:
			if(all_skyline_before_time > data[1][0]):
				skylines.append(data[1][1]);
			else:
				new_window_data.append(data);
		window_data=new_window_data;	
		find_skylines_using_BNL(temp_data_list);

#To convert the flag into Bits
def convert_flag_to_bits(flag,dim):
	count = dim
	result = [0] * dim
	while (flag>0):
		a=int(float(flag%2))
		result[count - 1] = a
		count = count -1
		flag=(flag-a)/2
	return result

##-------------- Merging  Job  ------------------##
# Hadoop sorts mapper output by key (here: flag) before it is passed to the reducer
# Reduce Task
if __name__ == '__main__':

	#Variables used in BNL
	window_maxsize=1000;
	window_data=[];
	data_list=[];
	skylines=[];
	timestamp=0;
	file_counter=0;
	flag3=0;

	# Variables used in thsi algorithm
	input_set= []
	zero_all_exists = False

	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
		a = line.split('\t',1)[1]
		tuple = ast.literal_eval(a)
		flag = tuple[0]
		point = tuple[1]
		converted_flag = convert_flag_to_bits(flag,len(point))

		#print flag,point
		
		if ( flag == 0) :
			zero_all_exists = True

		if not(( flag == pow(2,len(point)) - 1) and zero_all_exists == True ):
			input_set.append([converted_flag,point])
				

	#print input_set
	find_skylines_using_BNL(input_set)
	for skyline in skylines:
		print skyline
