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
import numpy
import ast


# To compare two numbers and return which one is dominant over other 
def compare(element_1,element_2):
	flag1=0;
	flag2=0;
	for i in range(0,len(element_1[1])):
		if((element_1[1][i]-element_2[1][i])>0):
			if(flag2==1):
				return 0;
			flag1 = 1;
		elif((element_1[1][i]-element_2[1][i])<0):
			if(flag1==1):
				return 0;
			flag2 = 1;
	if(flag1 == 1 and flag2 == 0):
		return 2
	else :
		return 1

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
	flag3=0;
	all_skyline_before_time=0;
	data_tuple_with_timestamp=[];
	for data in sample_data:
		timestamp=timestamp+1;
		data_tuple_with_timestamp.append([timestamp,data]);
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
					#print "\n\n\n\n\n\nn\n\n\n\n"
					with open("skyline_temporary_file.txt", "a") as myfile:
						if(flag3==0):
							all_skyline_before_time=data[0];
							flag3=1;
						for integer in data[1]:
							myfile.write(str(integer));
							myfile.write(" ");
						myfile.write("\n");
			window_data=new_window_data;
	open("skyline_temporary_file.txt", "a");
	if(os.stat("skyline_temporary_file.txt").st_size == 0):
		#print "windowdata =",window_data,"\n"
		for data in window_data:
			skylines.append(data[1]);
	else:
		temp_data_list=[];
		new_window_data=[];
		with open('skyline_temporary_file.txt') as f:
			temp_data_list = [[float(x) for x in line.split()] for line in f];
		fo = open("skyline_temporary_file.txt", "rw+");
		fo.truncate();
		for data in window_data:
			if(all_skyline_before_time > data[0]):
				skylines.append(data[1]);
			else:
				new_window_data.append(data);
		window_data=new_window_data;	
		print window_data;
		print "File data=",temp_data_list,"\n";	
		find_skylines_using_BNL(temp_data_list);


##-------------- Division Job  ------------------##
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

	#Create a new file to store the output
	fo = open("divison_job_reducer_output.txt", "w+");
	fo.truncate();

	# Variables used in thsi algorithm
	current_flag = -1
	flag = -1
	input_set_for_each_flag= []

	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
		# print line
		flag, point = line.split('\t')
		flag  = ast.literal_eval(flag)
		point  = ast.literal_eval(point)

		#print flag,point
		
		# Reduce Task
		if current_flag == flag :
			input_set_for_each_flag.append(point)
		else :
			if current_flag != -1 :
				#write skylines to a file
				#print "Input Set = ",input_set_for_each_flag
				initialize_var()
				find_skylines_using_BNL(input_set_for_each_flag)
				with open("divison_job_reducer_output.txt", "a") as myfile:
					for skyline in skylines:
						myfile.write(str(current_flag)+'\t'+str(skyline)+'\n')
				for skyline in skylines:	
					print current_flag,'\t',skyline
			input_set_for_each_flag = []
			skylines = []
			current_flag = flag
			input_set_for_each_flag.append(point)

	# To output the skylines out of the remaining input to be processed
	if current_flag == flag :
		#print "Input Set = ",input_set_for_each_flag
		initialize_var()
		find_skylines_using_BNL(input_set_for_each_flag)
		with open("divison_job_reducer_output.txt", "a") as myfile:
			for skyline in skylines:
				myfile.write(str(current_flag)+'\t'+str(skyline)+'\n')
		for skyline in skylines:
			print current_flag,'\t',skyline
