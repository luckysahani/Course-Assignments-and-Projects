import os
dimensions_skyline_list=[];
window_maxsize=0;
window_data=[];
data_list=[];
skylines=[];
timestamp=0;
with open('query1.txt') as f:
    temp_list = [[int(x) for x in line.split()] for line in f];
    dimensions_skyline_list = temp_list[0];
    window_maxsize = temp_list[1][0]
with open('sample2.txt') as f:
    data_list = [[int(x) for x in line.split()] for line in f];

def compare(element_1,element_2):
	temp_list=[];
	x=element_1[1];
	y=element_2[1];
	for i in dimensions_skyline_list:
		temp_list.append(x[i]-y[i]);
	# print x,y,temp_list;
	flag1=0;
	flag2=0;
	for elem in temp_list:
		if(elem > 0):
			flag1 = 1;
		elif (elem < 0) :
			flag2 = 1;
	if(flag1 == 1 and flag2 == 1):
		return 0
	elif(flag1 == 1):
		return 2
	else :
		return 1

def find_skylines(sample_data):
	global window_data,timestamp;
	data_tuple_with_timestamp=[];
	for data in sample_data:
		timestamp=timestamp+1;
		data_tuple_with_timestamp.append([timestamp,data]);
	for data in data_tuple_with_timestamp:
		if(len(window_data)==0):
			window_data.append(data);
		else:
			topush_data=False;
			flag1=0;
			new_window_data=[];
			# print "\n",window_data;
			for i in xrange(0,len(window_data)): 
				# print window_data,i,window_data[i];
				element=window_data[i];
				compare_result = compare(data,element);
				# print compare_result;
				if (compare_result == 1):
					flag1=1;
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
						# print window_data,data;
						for integer in data[1]:
							myfile.write(str(integer));
							myfile.write(" ");
						myfile.write("\n");
			window_data=new_window_data;
			print window_data;
	print "\nIteration Complete\n";
	if(os.stat("skyline_temporary_file.txt").st_size == 0):
		print "Done";
		for data in window_data:
			skylines.append(data);
	else:
		# print "Size=",os.stat("skyline_temporary_file.txt").st_size;
		temp_data_list=[];
		new_window_data=[];
		with open('skyline_temporary_file.txt') as f:
			temp_data_list = [[int(x) for x in line.split()] for line in f];
		fo = open("skyline_temporary_file.txt", "rw+");
		fo.truncate();
		for data in window_data:
			# print temp_data_list[0][0] , data[0];
			if(temp_data_list[0][0] > data[0]):
				skylines.append(data[0]);
			else:
				new_window_data.append(data);
		window_data=new_window_data;
		print "File data=",temp_data_list,"\n";	
		find_skylines(temp_data_list);
			


find_skylines(data_list);
print skylines;



