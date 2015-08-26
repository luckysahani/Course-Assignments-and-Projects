s = raw_input();
[a,b] = map(int, s.split(' '));
wsize = input()

LL = [];
LL1 = [];

def compare(l1, l2):
	# print l1,l2
	l = [];
	for z in range(0, len(l1)):
		l.append([l1[z] - l2[z]]);
	flag1 = 0;
	flag2 = 0;
	for elem in l:
		if(elem > 0):
			flag1 = 1;
		elif (elem < 0) :
			flag2 = 1;
	if(flag1 == 1 and flag2 == 1):
		return 0
	elif(flag1 == 1):
		return 1
	else :
		return -1

for k in range(0,b):
	s = raw_input()
	numbers = map(float, s.split(' '))
	LL1= [];
	flag3 = 0;
	if len(LL) == 0:
		LL.append(numbers)
	else:
		for i in range(0,len(LL)):
			# print LL[i],numbers;
			temp1 = compare(LL[i],numbers);
			if (temp1 == -1):
				flag3 = 1;
				for j in range(i,len(LL)) :
					LL1.append(LL[j])
				break;
			elif (temp1 == 0):
				LL1.append(LL[i]);
		LL= LL1;
		if (flag3 == 0):
			LL.append(numbers)
	print LL;
