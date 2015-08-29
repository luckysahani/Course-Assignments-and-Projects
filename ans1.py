dimensions_skyline_list=[];
window_maxsize=0;
window_data=[];
data_list=[];
data_tuple_with_timestamp=[];
with open('query1.txt') as f:
    temp_list = [[int(x) for x in line.split()] for line in f];
    dimensions_skyline_list = temp_list[0];
    window_maxsize = temp_list[0][0]
with open('sample1.txt') as f:
    data_list = [[int(x) for x in line.split()] for line in f];

def compare(element_1,element_2):
	temp_list=[];
	x=element_1[1];
	y=element_2[1];
	for i in dimensions_skyline_list:
		temp_list.append(x[i]-y[i]);
	flag1=1;
	flag2=2;
	for elem in temp_list:
		if(elem > 0):
			flag1 = 1;
		elif (elem < 0) :
			flag2 = 1;
	if(flag1 == 1 and flag2 == 1):
		return 0
	elif(flag1 == 1):
		return 1
	else :
		return 2

def find_skylines(sample_data):
	timestamp=0;
	global window_data;
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
			# print window_data,"\n\n";
			for i in xrange(0,len(window_data)): 
				# print window_data,i,window_data[i];
				element=window_data[i];
				compare_result = compare(data,element);
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
				new_window_data.append(data);
				window_data=new_window_data;








find_skylines(data_list);
print window_data;



