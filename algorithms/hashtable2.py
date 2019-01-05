class HashTable:
	def __init__(self, size):
		self.elem = [[] for i in range(size)]
		self.count = size

	def hash(self, key):
		return key % self.count

    def insert_hash(self, key):
    	address = self.hash(key)
    	self.elem[key].append[key]

    def search_hash(self, key):
    	address = self.hash(key)
    	for value in self.elem[address]:
    		if value == key:
    			return True
    	return False