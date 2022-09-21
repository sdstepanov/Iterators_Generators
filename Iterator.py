class FlatIterator(list):
	def __iter__(self):
		self.item = 0
		self.item_1 = -1
		return self

	def __next__(self):
		self.item_1 += 1
		if len(self[self.item]) > 1:
			self.new_list = self[self.item]
		if self.item_1 == len(self[self.item]):
			self.item += 1
			self.item_1 = 0
		if self.item == len(self):
			raise StopIteration
		return self[self.item][self.item_1]


class FlatIterator2:
	def __init__(self, new_list):
		self.new_list = new_list

	def __iter__(self):
		self.list_item = []
		self.elements_item = iter(self.new_list)
		return self

	def __next__(self):
		while True:
			try:
				self.element = next(self.elements_item)
			except StopIteration:
				if not self.list_item:
					raise StopIteration
				else:
					self.elements_item = self.list_item.pop()
					continue
			if isinstance(self.element, list):
				self.list_item.append(self.elements_item)
				self.elements_item = iter(self.element)
			else:
				return self.element
