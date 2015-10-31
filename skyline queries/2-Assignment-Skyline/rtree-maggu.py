#!/usr/bin/python

import heapq
from random import uniform
import time
import sys


#check intersecting rectangles
#return 0 if it is not intersecting
#else it will return 1
def intersect(MBRa, MBRb):
	dimension = len(MBRa)/2
	
	#if its ith dimension value is greater than the maximum ith dimension value of MBR
	for i in range(0, dimension):
		if MBRa[i] > MBRb[i+d]:
			return 0

	for i in range(0,dimension):
		if MBRa[i+d] < MBRb[i]:
			return 0

	return 1

def contain(MBR1, MBR2):
	d = len(MBR1)/2
	for i in range(0,d):
		if MBR1[i] > MBR2[i]:
			return 0

	for i in range(0,d):
		if MBR1[i+d] < MBR2[i+d]:
			return 0
	return 1

#merges 2 bounding rectangles
def merge(MBRa, MBRb):
	if len(MBRa) == 0 :
		return MBRb
	if len(MBRb) == 0 :
		return MBRa

	#intialise MBR
	MBR = []
	dimension = len(MBRa)/2

	for i in range(0, d):
		MBR.append(min(MBRa[i], MBRb[i]))

	for i in range(d, 2*d):
		MBR.append(max(MBRa[i], MBRb[i]))

	# print MBR,"\n",MBRa,"\n",MBRb
	# sys.exit()
	return MBR	

def insert(root, Node):
	target = root.selectLeaf(Node)
	Node.parent = target
	target.leaves.append(Node)
	target.MBR = merge(target.MBR, Node.MBR)
	target.AdjustTree()
	if root.parent != None:
		root = root.parent
	return root

def notDominated(skylineSet, MBR, dims):
	global comparisons
	for skyline in skylineSet:
		comparisons += 1
		if dominating(skyline[1], MBR, dims):
			return False
	return True

def dominating(obj1, obj2, dims):
	for i in dims:
		index = i - 1
		if obj1[index] > obj2[index]:
			return False
	return True

def increaseVolume(MBR1, MBR2):
	d = len(MBR1)/2 
	currSpace = 1.0
	for i in range(0,d):
		currSpace = currSpace * (MBR1[i+d] - MBR1[i])

	newSpace = 1.0
	for i in range(0,d):
		newSpace = newSpace * (max(MBR1[i+d], MBR2[i+d]) - min(MBR1[i], MBR2[i]))

	return newSpace - currSpace   

def getSpace(MBR):
	d = len(MBR)/2 
	space = 1.0
	for i in range(0,d):
		space = space * (MBR[i+d] - MBR[i])
	return space

def indexingValue(MBR):
	d = len(MBR)/2
	indexValue = 0
	for i in range(0, d):
		indexValue = indexValue + MBR[i]
	return indexValue

#priority queue class to implement priority queue. Here heapq library is used to implement priority queue
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


class Node(object):
	"""docstring for node"""
	def __init__(self, MBR = [] , level = 0, index = None, parent = None):
		self.MBR = MBR
		self.level = level
		self.index = index
		self.parent = parent


class RTree(object):
	"""docstring for RTree"""
	def __init__(self, leaves = None, MBR = [], level = 1, minEle = 4, maxEle = 8, parent = None):
		self.MBR = MBR
		self.minEle = minEle
		self.maxEle = maxEle
		self.level = level
		self.parent = parent
		self.leaves = []

	#search for the intersection with the minimum bounding rectangle
	def search(self, MBR):
		res = []
		if not self.level == 1 :
			for leaf in self.leaves:
				if intersect(MBR, leaf.MBR):
					res += leaf.Search(MBR)
			return res
		else :
			for leaf in self.leaves:
				 if intersect(MBR, leaf.MBR):
				 	res.append(leaf.index)
			return res

	#fid the leaf node
	def findLeafNode(self, Node):
		res = []

		if self.level == 1 : 
			for leaf in self.leaves:
				if leaf.index == Node.index :
					return self
		else :
			for leaf in self.leaves:
				if contain(leaf.MBR, Node.MBR):
					res.append(leaf.findLeafNode(Node))
			for val in res:
				if val != None :
					return val

	#start skyline algorithm
	def findSkylinesStart(self, dims):
		queue = PriorityQueue()
		global comparisons
		skyline = []
		for leaf in self.leaves:
			queue.push(leaf,indexingValue(leaf.MBR))

		while queue.empty() != 0:
			obj = queue.pop()
			if notDominated(skyline, obj.MBR, dims) :
				if obj.level > 0 :
					for leaf in obj.leaves:
						queue.push(leaf,indexingValue(leaf.MBR))
				else :
					skyline.append((obj.index, obj.MBR))
		return skyline, comparisons  

	#select leaf node
	def selectLeaf(self, Node):
		#if already a leaf node
		if self.level == Node.level + 1 :
			return self
		else :
			minIncreaseInVolume = 100000000
			minIncreaseInVolumeIdx = -1
			for i in range(0, len(self.leaves)):
				increaseInVolume = increaseVolume(self.leaves[i].MBR, Node.MBR)
				if increaseInVolume < minIncreaseInVolume :
					minIncreaseInVolume = increaseInVolume
					minIncreaseInVolumeIdx = i
			return self.leaves[minIncreaseInVolumeIdx].selectLeaf(Node)


	def splitNode(self):
		#if parent is not present
		if self.parent == None :
			self.parent = RTree(level = self.level + 1, minEle = self.minEle, maxEle = self.maxEle)
			self.parent.leaves.append(self)

		leafa = RTree(level = self.level, minEle = self.minEle, maxEle = self.maxEle, parent = self.parent)
		leafb = RTree(level = self.level, minEle = self.minEle, maxEle = self.maxEle, parent = self.parent)
		self.getSeed(leafa, leafb)
		while len(self.leaves) > 0:
			if len(leafa.leaves) > len(leafb.leaves) and len(leafb.leaves) + len(self.leaves) == self.minEle:
				for leaf in self.leaves:
					leafb.MBR = merge(leafb.MBR, leaf.MBR)
					leafb.leaves.append(leaf)
					leaf.parent = leafb
				self.leaves = []
				break
			if len(leafb.leaves) > len(leafa.leaves) and len(leafa.leaves) + len(self.leaves) == self.minEle:
				for leaf in self.leaves:
					leafa.MBR = merge(leafa.MBR, leaf.MBR)
					leafa.leaves.append(leaf)
					leaf.parent = leafa
				self.leaves = []
				break
			self.pickNext(leafa, leafb)

		self.parent.leaves.remove(self)
		self.parent.leaves.append(leafa)
		self.parent.leaves.append(leafb)
		self.parent.MBR = merge(self.parent.MBR, leafa.MBR)
		self.parent.MBR = merge(self.parent.MBR, leafb.MBR)


	def getSeed(self, leaf1, leaf2):
		a = 0
		b1 = 0
		b2 = 0

		for i in range(0, len(self.leaves)):
			for j in range(i+1, len(self.leaves)):
				newMBR = merge(self.leaves[i].MBR, self.leaves[j].MBR)
				S_new = getSpace(newMBR)
				S1 = getSpace(self.leaves[i].MBR)
				S2 = getSpace(self.leaves[j].MBR)
				if S_new - S1 - S2 > a:
					b1 = i
					b2 = j
					a = S_new - S1 - S2
		n2 = self.leaves.pop(b2)
		n2.parent = leaf1
		leaf1.leaves.append(n2)
		leaf1.MBR = leaf1.leaves[0].MBR
		n1 = self.leaves.pop(b1)
		n1.parent = leaf2
		leaf2.leaves.append(n1)
		leaf2.MBR = leaf2.leaves[0].MBR


	def pickNext(self, leaf1, leaf2):
		d = 0
		t = 0
		
		for i in range(0,len(self.leaves)):
			d1 = increaseVolume(merge(leaf1.MBR, self.leaves[i].MBR), leaf1.MBR)
			d2 = increaseVolume(merge(leaf2.MBR, self.leaves[i].MBR), leaf2.MBR)
			if abs(d1 - d2) > abs(d):
				d = d1 - d2
				t = i
		if d > 0:
			target = self.leaves.pop(t)
			leaf2.MBR = merge(leaf2.MBR, target.MBR)
			target.parent = leaf2
			leaf2.leaves.append(target)
		else:
			target = self.leaves.pop(t)
			leaf1.MBR = merge(leaf1.MBR, target.MBR)
			target.parent = leaf1
			leaf1.leaves.append(target)


	def AdjustTree(self):
		p = self
		while p != None:
			if len(p.leaves) > p.maxEle:
				p.splitNode()
			else:
				if p.parent != None:
					p.parent.MBR = merge(p.parent.MBR, p.MBR)
			p = p.parent

def getBlockParametersDimension(queryfile, dims, blocksize):
	query = open(queryfile, 'r')
	line1 = query.readline().rstrip()
	dims = line1.split('\t')
	dims = map(int, dims)
	line2 = query.readline().rstrip()
	blocksize = int (line2)
	query.close()
	return dims, blocksize

if __name__ == '__main__':
	startTime = time.time()
	data = {}
	#get dimension on which skylines are to be found and memory blocksize 	
	queryfile = 'query2.txt'
	dims = []
	blocksize  = 2
	root = RTree(minEle = blocksize/2, maxEle = blocksize)
	dims, blocksize = getBlockParametersDimension(queryfile, dims, blocksize)
	

	#get input file of objects
	infilename = 'sample_ant.txt'
	outfilename = 'output_ant.txt'
	inputfile = open(infilename, 'r')
	n = []
	for line in inputfile:
		line = line.rstrip().lstrip()
		words = line.split('\t')
		obj = words[1:]
		obj = map(float, obj)		#converts string list to int list
		index = int (words[0])
		data = {}
		d = len(obj)
		for j in range(0, d):
			data[j] = obj[j]
			data[j+d] = obj[j]
		n.append(Node(MBR = data, index = index))
	inputfile.close()

	for i in range(0, len(n)):
		root = insert(root, n[i])

	comparisons = 0
	skylines, comparisons = root.findSkylinesStart(dims)

	skyIndex = []
	for obj in skylines:
		skyIndex.append(obj[0])
	skyIndex = sorted(skyIndex)
	endTime = time.time()

	#print results
	outfile = open(outfilename, 'w')
	outfile.write("Total running time: "+ str(endTime - startTime) + " sec\n")
	outfile.write("Comparisons: "+ str(comparisons)+"\n")
	outfile.write("Size of skyline set: "+str(len(skyIndex)) + "\n")
	outfile.write("Ids of the skyline objects: \n")
	outfile.write(str(skyIndex))
	outfile.write("\n")
	outfile.close()