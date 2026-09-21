class Stack:
	
	def __init__(self, size):
		self.stk = []
		self.size = size

	def push(self, item):
		if len(self.stk) < self.size:
			self.stk.append(item)
			return item
		else: 
			print("Stack Overflow")
			return None


	def pop(self):
		if len(self.stk) != 0:
			item = self.stk.pop()
			return item  
		else: 
			print("Stack Empty")
			return None

	def is_empty(self):
		return len(self.stk) == 0

	def __str__(self):
		return str(self.stk)