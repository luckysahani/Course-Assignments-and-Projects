#!/usr/bin/python

import heapq
from random import uniform
import time
import os
from math import floor


# Defining storage Object
class Node(object):
	# Object's location information is stored in MBR
	# Level is fixed at 0 for the bottom
	# Index for the object's index in the database
	# Parent for the object parent
	def __init__(self, MBR = [], level = 0, index = None, parent = None):
		self.MBR = MBR
		self.level = level
		self.index = index
		self.parent = parent

#Definition of R tree node 
class RTree(object):
	#The location information in MBR
	#level of its layers(default is 1 for leaf node)
	#minimum_childs and maximum_childs for minimum and maximum number of children's
	#parent to identify any object parent
	def __init__ (self, leaves =None, MBR = [],level=1, minimum_childs=4,maximum_childs=8,parent=None):
		self.leaves=[]
		self.MBR=MBR
		self.level=level
		self.minimum_childs=minimum_childs
		self.maximum_childs=maximum_childs
		self.parent=parent

	def choose_leaf(self, Node) :
		#If the current node layer is equal to the layer of the node to be inserted,then return that node.
		if self.level == Node.level + 1 :
			return self
		else :
			minimum_increase_in_volume= 10000000000
			minimum_increase_in_volume_index = -1
			for i in range(0, len(self.leaves)) :
				temp_increase_in_volume= increase_in_volume(self.leaves[i].MBR, Node.MBR)
				if temp_increase_in_volume < minimum_increase_in_volume :
					minimum_increase_in_volume = temp_increase_in_volume
					minimum_increase_in_volume_index= i
			return self.leaves[minimum_increase_in_volume_index].choose_leaf(Node)

	#Search for a given rectangle.
	def search(self,MBR):
		result = []
		# If you have reached a leaf node, then add the result objects directly.
		if self.level == 1:
			for leaf in self.leaves:
				if intersect (MBR, leaf.MBR):
					result.append (leaf.index)
			return result
		# Otherwise, the target for MBR intersects child nodes. So, search and add it to the result.
		else:
			for leaf in self.leaves:
				if intersect (MBR, leaf.MBR):
					result = result + leaf.Search (MBR)
			return result
				
	# Locate a given node. 
	def find_leaf_node (self, node):
		result = []
		# If the current node is a leaf node, then do a direct traversal of the leaves to determine the node
		if self.level == 1:
			for leaf in self.leaves:
				if leaf.index == node.index:
					return self
		# If the current node is not a leaf node, all child nodes are recursively searched the MBR contains the target.
		else:
			for leaf in self.leaves:
				if contain(leaf.MBR, node.MBR):
					result.append (leaf.find_leaf_node(node))
			for x in result:
				if x != None:
					return x

	#Find skyline using BBS
	#Algorithm BBS (R-tree R)
	def find_skylines_using_bbs(self,dimensions):
		q=PriorityQueue()
		# 1. S=nill // list of skyline points
		skylines = []
		# 2. insert all entries of the root R in the heap/queue
		for leaf in self.leaves:
			q.push(leaf,indexingValue(leaf.MBR))
		# 3. while heap/queue not empty
		while q.empty() != 0:
			# 4. remove top entry e
			some_object = q.pop()
			# 5. if e is dominated by some point in S discard e
			#print IsDominated_by_skylines(skylines,some_object.MBR,dimensions_skyline_list)
			if (IsDominated_by_skylines(skylines,some_object.MBR,dimensions_skyline_list) == False):
				# 7. if e is an intermediate entry
				if some_object.level>0:
					# 8. for each child ei of e
					for leaf in some_object.leaves:
						# 9. if ei is not dominated by some point in S
						if (IsDominated_by_skylines(skylines,leaf.MBR,dimensions_skyline_list) == False):
							# 10. insert ei into heap/queue
							q.push(leaf,indexingValue(leaf.MBR))

				# 11. else // e is a data point
				else :
					# 12. insert ei into S
					#print "Adding this object to skyline :",some_object.MBR,"\n"
					skylines.append((some_object.index,some_object.MBR))
		return skylines

	#To split a node into two when the maximum number of child is reached by that node
	def split_node(self):
		# If the current node has no parent
		if (self.parent == None):
			# Parent node created and then the current node is appended 
			self.parent = RTree(level = self.level +1,minimum_childs=self.minimum_childs,maximum_childs=self.maximum_childs)
			self.parent.leaves.append(self)

		# Create new nodes such that the level, min child and max child are the same as the current node.
		leaf1 = RTree(level = self.level, minimum_childs = self.minimum_childs, maximum_childs = self.maximum_childs, parent = self.parent)
		leaf2 = RTree(level = self.level, minimum_childs = self.minimum_childs, maximum_childs = self.maximum_childs, parent = self.parent)

		# Call pick_the_seeds to leaf1 and leaf2 for distribution of child nodes
		self.pick_the_seeds(leaf1, leaf2)
		while len (self.leaves)> 0:
			# Move the remaining child nodes into a group in order to make the set of nodes greater than minimum childs
			if len(leaf1.leaves) > len(leaf2.leaves) and len (leaf2.leaves) + len(self.leaves) == self.minimum_childs :
				for leaf in self.leaves:
					leaf2.MBR = merge ( leaf2.MBR,leaf.MBR)
					leaf2.leaves.append(leaf)
					leaf.parent = leaf2
				self.leaves = []
				break
			if len(leaf2.leaves) > len(leaf1.leaves) and len (leaf1.leaves) + len(self.leaves) == self.minimum_childs :
				for leaf in self.leaves:
					leaf1.MBR = merge ( leaf1.MBR,leaf.MBR)
					leaf1.leaves.append(leaf)
					leaf.parent = leaf1
				self.leaves = []
				break
			# Otherwise call choose_next for the next leaf1 and leaf2 
			self.choose_next(leaf1,leaf2)

		# Remove yourself as the child of your parent and append the two new nodes to be the new childs
		self.parent.leaves.remove(self)
		self.parent.leaves.append(leaf1)
		self.parent.leaves.append(leaf2)
		# Merge the parent's MBR with the two new child's MBR
		self.parent.MBR = merge (self.parent.MBR, leaf1.MBR)
		self.parent.MBR = merge (self.parent.MBR, leaf2.MBR)


	#To find the leaves with maximum distance betweeen them
	def pick_the_seeds(self,leaf1,leaf2):
		distance=0
		node_id_1=0
		node_id_2=0	  
		# Through all the possible combinations of child nodes, to find the leaves which has the maximum difference between them.
		for i in range(0,len(self.leaves)):
			for j in range(i+1,len(self.leaves)):
				temp_MBR=merge(self.leaves[i].MBR, self.leaves[j].MBR)
				space_of_temp_MBR = get_space_of_MBR(temp_MBR)
				space_of_leave_i= get_space_of_MBR(self.leaves[i].MBR)
				space_of_leave_j= get_space_of_MBR(self.leaves[j].MBR)
				if space_of_temp_MBR - space_of_leave_i - space_of_leave_j > distance:
					node_id_1=i
					node_id_2=j
					distance = space_of_temp_MBR - space_of_leave_j -space_of_leave_i

		new_2=self.leaves.pop(node_id_2)
		new_2.parent =leaf1
		leaf1.leaves.append(new_2)
		leaf1.MBR = leaf1.leaves[0].MBR

		new_1=self.leaves.pop(node_id_1)
		new_1.parent = leaf2
		leaf2.leaves.append(new_1)
		leaf2.MBR=leaf2.leaves[0].MBR

	#To choose the next two leaf's which has maximum difference between them in terms of volume
	def choose_next(self,leaf1,leaf2):
		distance=0
		node_id=0
		# Traverse the child nodes to find the one leaf with which the maximum area is obtained with any one of them
		for i in range(0, len(self.leaves)):
			distance_1= increase_in_volume(merge(leaf1.MBR,self.leaves[i].MBR),leaf1.MBR)
			distance_2= increase_in_volume(merge(leaf2.MBR,self.leaves[i].MBR),leaf2.MBR)
			if abs(distance_1 - distance_2) > abs(distance):
				distance=distance_1 - distance_2
				node_id = i

		if distance > 0:
			final_leaf = self.leaves.pop(node_id)
			leaf2.MBR = merge(leaf2.MBR,final_leaf.MBR)
			final_leaf.parent=leaf2
			leaf2.leaves.append(final_leaf)
		else:
			final_leaf = self.leaves.pop(node_id)
			leaf1.MBR = merge(leaf1.MBR,final_leaf.MBR)
			final_leaf.parent=leaf1
			leaf1.leaves.append(final_leaf)

	# Adjust the tree in bottom upward fashion
	def adjustTree(self):
			current=self
			while current!=None :
				if len(current.leaves) > current.maximum_childs:
					current.split_node()
				else:
					if current.parent!=None:
						current.parent.MBR=merge(current.parent.MBR,current.MBR)
				current=current.parent

#To check whether the skyline set dominated the object or not
def IsDominated_by_skylines(skyline_set,MBR_1,dimensions_skyline_list):
	global	number_of_comparisions
	for skyline in skyline_set:
		number_of_comparisions=number_of_comparisions+1
		temp = compare(skyline[1],MBR_1,dimensions_skyline_list)
		if(temp == 1):
			return True
	return False

#Comparing two objects to check for domination
def compare(element_1,element_2,dimensions_skyline_list):
	flag1=0
	flag2=0
	#print element_1,element_2,dimensions_skyline_list
	for j in dimensions_skyline_list:
		i=j-1
		if(element_1[i]>element_2[i]):
			return 2
	return 1

#To check whether the two MBR's have a common volume or not
def intersect(MBR_1,MBR_2):
	total_number_of_dimensions=len(MBR_1)/2
	for i in range(0, total_number_of_dimensions):
		if MBR_1[i] > MBR_2[i+d]:
			return 0

	for i in range(0,total_number_of_dimensions):
		if MBR_1[i+d] < MBR_2[i]:
			return 0

	return 1

# Insert a new node, return to the root node after the update.			
def insert (root, node):
	target = root.choose_leaf (node)
	node.parent = target
	target.leaves.append (node)
	target.MBR = merge (target.MBR, node.MBR)
	target.adjustTree ()
	if root.parent!= None:
		root = root.parent
	return root


#To check whether MBR_1 contains MBR_2 or not. If true, then 1 is returned , o/w 0 is returned
def contain(MBR_1,MBR_2):
	total_number_of_dimensions=len(MBR_1)/2
	for i in range(0, total_number_of_dimensions):
		if MBR_1[i]>MBR_2[i] :
			return 0

	for i in range(total_number_of_dimensions,2*total_number_of_dimensions):
		if MBR_1[i]<MBR_2[i] :
			return 0

	return 1

#To get the indexing value of an MBR
def indexingValue(MBR):
	indexValue = 0
	for dim in dimensions_skyline_list:
		indexValue = indexValue + MBR[dim-1]
	return indexValue

#Merge two MBR's and return the new merged MBR
def merge(MBR_1,MBR_2):
	#If length of any anyone is 0, then return the other MBR
	if len(MBR_1) == 0 :
		return MBR_2
	if len(MBR_2)==0:
		return MBR_1
	#Initialize the new MBR
	MBR=[]
	total_number_of_dimensions=len(MBR_1)/2
	#print len(MBR_1),"hi\n",MBR_1
	#Merging the mim of all dimensions in this loop
	for i in range(0,total_number_of_dimensions):
		MBR.append(min(MBR_1[i],MBR_2[i]))
	#Merging the max of all dimensions in this loop
	for i in range(total_number_of_dimensions,2*total_number_of_dimensions):
		MBR.append(max(MBR_1[i],MBR_2[i]))
	#returning the final MBR
	return MBR

#To calculate the increase in MBR_1 area after MBR_2 is merged with MBR_1
def increase_in_volume(MBR_1,MBR_2):
	total_number_of_dimensions = len(MBR_1)/2
	currSpace = 1.0
	for i in range(0,total_number_of_dimensions):
		currSpace = currSpace * (MBR_1[i+total_number_of_dimensions] - MBR_1[i])

	newSpace = 1.0
	for i in range(0,total_number_of_dimensions):
		newSpace = newSpace * (max(MBR_1[i+total_number_of_dimensions], MBR_2[i+total_number_of_dimensions]) - min(MBR_1[i], MBR_2[i]))

	return newSpace - currSpace

#To calculate the space i.e. product of all the edges of the MBR
def get_space_of_MBR(MBR_1):
	total_number_of_dimensions = len(MBR_1)/2
	x = 1.0
	for i in range(0,total_number_of_dimensions):
		x = x * (MBR_1[i+total_number_of_dimensions] - MBR_1[i])
	return x

#Priority queue class to implement priority queue
class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]

	def empty(self):
		return len(self._queue)


if __name__ == '__main__':
	
	dimensions_skyline_list=[]
	blocksize=2
	diskpagesize=0
	pointer_size=0
	key_size=0
	number_of_comparisions = 0
	queryfile="query2.txt"
	outputfile="output-ind-2.txt"
	inputfile="sample_ind.txt"

	#Get data from query file
	with open(queryfile) as f:
		temp_list = [[int(x) for x in line.split()] for line in f]
		dimensions_skyline_list = temp_list[0]
		diskpagesize = temp_list[1][0]
		pointer_size = temp_list[2][0]
		key_size = temp_list[2][1]

	#Get data from input file
	with open(inputfile) as f:
		data_list = [[float(x) for x in line.split()] for line in f]

	#Calculating the number of entries that can be stored in a page i.e the block size
	# Number of index entries per leaf page = Floor( Page_size / (size(search key value) + size(reference to tuple))) 
	blocksize = floor(diskpagesize/(pointer_size+key_size))

	#Initializing the root with the calculate blcoksize as its max childs
	root = RTree(minimum_childs = int(blocksize)/2, maximum_childs = int(blocksize))
	l = []
	for data in data_list:
		a= {}
		for j in range(1,len(data)):
			a[j-1] = data[j]
			a[j-1+len(data)-1]=data[j]
		l.append(Node(MBR = a,index = data[0]))

	for i in range(0, len(l)):
		root = insert(root, l[i])

	#start the timer
	start_time=int(round(time.time() * 1000))

	skylines=root.find_skylines_using_bbs(dimensions_skyline_list)
	
	#end the timer
	end_time=int(round(time.time() * 1000))

	#Calculating the total time
	total_time=end_time-start_time

	#Printing the required Output
	print "Total running time =",total_time,"\n"
	print "Number of object-to-object comparisons = ",number_of_comparisions,"\n"
	print "Size of skyline set = ",len(skylines),"\n"

	#Printing skylines if required
	# for data in (skylines):
	# 	print "\n"
	# 	for dim in dimensions_skyline_list:
	# 		print data[0],data[1][dim-1]

	#Printing the Skyline output into a file
	with open(outputfile, "w+") as myfile:
		myfile.write("Total running time ="+str(total_time)+"\n")
		myfile.write("Number of object-to-object comparisons = "+str(number_of_comparisions)+"\n")
		myfile.write("Size of skyline set = "+str(len(skylines))+"\n")
		myfile.write("List of ids of the skyline objects in sorted manner : \n")
		for data in sorted(skylines):
			myfile.write(str(data[0]));
			myfile.write("\n");