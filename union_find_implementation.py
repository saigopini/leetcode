class UnionFindQuickFind():
	def __init__(self, size):
		"""
		Each array id corresponds to the node and the self.parent[id] = parent/root of id
		"""
		self.parent = [i for i in range(size)]

	def printArray(self):
		print(self.parent)

	def union(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: None
		"""
		change_from = self.parent[p]
		change_to = self.parent[q]
		for i in range(len(self.parent)):
			if self.parent[i] == change_from:
				self.parent[i] = change_to


	def find(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: boolean
		"""
		if self.parent[p] == self.parent[q]:
			return True
		else:
			return False

class UnionFindQuickUnion():
	def __init__(self, size):

		"""
		Each array id corresponds to the node and the self.parent[id] = parent/root of id
		"""
		self.parent = [i for i in range(size)]

	def printArray(self):

		print(self.parent)

	def __root__(self, i):
		"""
		:type i: int
		:purpose: find root of i
		:type i: int 
		"""
		
		while i != self.parent[i]:
			i = self.parent[i]
		return i

	def find(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: boolean
		"""

		return self.__root__(p) == self.__root__(q)

	def union(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: None
		"""

		change_from = self.__root__(p)
		change_to = self.__root__(q)
		self.parent[change_from] = change_to

class WeightedQuickUnionFind():

	def __init__(self,size):
		"""
		With Weighted Quick Find, each node has a weight, which is the size of the tree;
		this prevents the tree from getting too tall. The smaller tree becomes the child 
		of the larger tree.
		Each array id corresponds to the node and the self.parent[id] = parent/root of id
		"""

		self.parent = [i for i in range(size)]
		self.size = [1 for i in range(size)]

	def printArray(self):
		print("parent: " + str(self.parent))
		print("size: " + str(self.size))

	def __root__(self, i):
		"""
		:type i: int
		:purpose: find root of i
		:type i: int 
		"""
		while i != self.parent[i]:
			i = self.parent[i]

		return i

	def union(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: None
		"""
		#check the size of the trees
		#whatever is the larger tree becomes the root/parent of the smaller tree
		if self.size[p] < self.size[q]:
			change_from = self.__root__(p)
			change_to = self.__root__(q)
			self.parent[change_from] = change_to
			self.size[change_to] += self.size[change_from]

		else:
			change_from = self.__root__(q)
			change_to = self.__root__(p)
			self.parent[change_from] = change_to
			self.size[change_to] += self.size[change_from]

	def find(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: boolean
		"""
		return self.__root__(p) == self.__root__(q)

class PathCompressionUnionFind():
	def __init__(self, size):
		self.parent = [i for i in range(size)]

	def printArray(self):
		print("parent: " + str(self.parent))

	def __root__(self, i):
		"""
		:type i: int
		:purpose: find root of i
		:type i: int 
		"""
		#two pass implementation; every parent of i becomes a direct child of root(i)
		visited = []
		while i != self.parent[i]:
			visited.append(self.parent[i])
			i = self.parent[i]
		for j in range(len(visited)):
			self.parent[j] = i
		return i

	def union(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: None
		"""
		change_to = self.__root__(p)
		change_from = self.__root(q)
		self.parent[change_to] = change_from

	def find(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: boolean
		"""
		return self.__root__(p) == self.__root__(q)


class PathCompressionUnionFind2():
	def __init__(self, size):
		self.parent = [i for i in range(size)]

	def printArray(self):
		print("parent: " + str(self.parent))

	def __root__(self, i):
		"""
		:type i: int
		:purpose: find root of i
		:type i: int 
		"""
		#1 pass implemenetation
		while i != self.parent[i]:
			self.parent[i] = self.parent[self.parent[i]] #setting each node to point to it's grand parent
			i = self.parent[i]

		return i

	def union(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: None
		"""
		change_from = self.__root__(p)
		change_to = self.__root(q)
		self.parent[change_from] = change_to

	def find(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: boolean
		"""
		return self.__root__(p) == self.__root__(q)

class UnionFind():
	"""
	Path Compression Weighted Quick-Union Find
	"""
	def __init__(self, size):
		self.parent = [i for i in range(size)]
		self.size = [1 for i in range(size)]

	def printArray(self):
		print("parent: " + str(self.parent))
		print("size: " + str(self.size))

	def __root__(self, i):
		"""
		:type i: int
		:purpose: find root of i
		:type i: int 
		"""
		while i != self.parent[i]:
			self.parent[i] = self.parent[self.parent[i]]
			i = self.parent[i]
		return i

	def find(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype
		"""
		return self.__root__(p) == self.__root__(q)

	def union(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: None
		"""
		if self.size[p] < self.size[q]:
			change_from = self.__root__(p)
			change_to = self.__root__(q)
			self.parent[change_from] = change_to
			self.size[change_to] += self.size[change_from]
		else:
			change_from = self.__root__(q)
			change_to = self.__root__(p)
			self.parent[change_from] = change_to
			self.size[change_to] += self.size[change_from]


uf = UnionFind(9)
uf.printArray()
uf.union(0,1)
uf.printArray()
uf.union(1,3)
uf.printArray()
print(uf.find(0,1))
print(uf.find(8,3))
uf.union(2,3)
print(uf.find(2,3))

