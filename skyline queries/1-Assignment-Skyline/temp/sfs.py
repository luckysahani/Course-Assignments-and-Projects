import os
import time
import math
from operator import itemgetter
dimensions_skyline_list=[];
window_maxsize=0;
window_data=[];
data_list=[];
skylines=[];
timestamp=0;
file_counter=0;
flag3=0;
number_of_comparisions=0;
with open('sample_query.txt') as f:
    temp_list = [[int(x) for x in line.split()] for line in f];
    dimensions_skyline_list = temp_list[0];
    window_maxsize = temp_list[1][0]
with open('genfile2.txt') as f:
    data_list = [[float(x) for x in line.split()] for line in f];

def compare(element_1,element_2):
	global number_of_comparisions;
	number_of_comparisions=number_of_comparisions+1;
	flag1=0;
	flag2=0;
	for i in dimensions_skyline_list:
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

def find_skylines_using_BNL(sample_data):
	global window_data,timestamp,file_counter,flag3;
	flag3=0;
	all_skyline_before_time=0;
	data_tuple_with_timestamp=[];
	for data in sample_data:
		timestamp=timestamp+1;
		data_tuple_with_timestamp.append([timestamp,data]);
	for data in data_tuple_with_timestamp:
		if(len(window_data)==0):
			window_data.append(data);
		else:
			topush_data=False;
			new_window_data=[];
			for i in xrange(0,len(window_data)): 
				element=window_data[i];
				compare_result = compare(data,element);
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
		# print window_data;
		# print "File data=",temp_data_list,"\n";	
		find_skylines_using_BNL(temp_data_list);

def entropy(data):
	entropy=0;
	for i in dimensions_skyline_list:
		entropy=entropy+math.log(1+data[i]);
	return entropy;

def find_skylines_using_SFS(sample_data):
	temp_data_list=[];
	final_data_list_2=[];
	for data in sample_data:
		temp_data_list.append([entropy(data),data]);
	final_data_list_1=sorted(temp_data_list,key=itemgetter(0));
	for data in final_data_list_1:
		final_data_list_2.append(data[1]);
	find_skylines_using_BNL(final_data_list_2);


# Start time for the BNL function
start_time=int(round(time.time() * 1000));

# Calling main function for finding skylines
find_skylines_using_SFS(data_list);

# End time for the BNL function
end_time=int(round(time.time() * 1000));

#Calculating the total time
total_time=end_time-start_time;

#Printing the required Output
print "Total running time(ms) =",total_time,"\n";
print "Number of object-to-object comparisons = ",number_of_comparisions,"\n";
print "Size of skyline set = ",len(skylines),"\n";

#Printing the Skyline output into a file
with open("skyline_output.txt", "w+") as myfile:
	myfile.write("Total running time(ms) ="+str(total_time)+"\n");
	myfile.write("Number of object-to-object comparisons = "+str(number_of_comparisions)+"\n");
	myfile.write("Size of skyline set = "+str(len(skylines))+"\n");
	myfile.write("Indexes of Skyline Objects : ")
	for data in skylines:
		myfile.write(str(data[0]));
		myfile.write("\t");