class UnionFind():
	def __init__(self, size):
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

uf = UnionFind(9)
uf.printArray()
uf.union(0,1)
uf.printArray()
uf.union(1,3)
uf.printArray()
print(uf.find(0,1))
print(uf.find(8,3))
uf.union(2,3)
print(uf.printArray())
print(uf.find(2,3))

