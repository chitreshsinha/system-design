class Item:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashMap:
	def __init__(self, size):
		self.size = size
		self.table = [[] for _ in range(self.size)]

	def _hashfunction(self, key):
		return key % self.size

	def set(self, key, value):
		hash = self._hashfunction(key)
		for x in self.table[hash]:
			if(x.key == key):
				x.value = value
				return

		print self.table, key
		self.table[hash].append(Item(key, value))

	def get(self, key):
		hash = self._hashfunction(key)
		for x in self.table[hash]:
			if(x.key == key):
				return x.value

		raise KeyError("Key not present")

## TESTING
h = HashMap(10)
print h
print h.size
print h.table
#print h.get(4)
print h.set(4, "four")
print h.get(4)
print h.set(14, "four-4")
print h.get(14)
print h.size
print h.table

