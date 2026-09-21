from stack import Stack
from queue import CircularQueue

class UnstructredGraph:
	def __init__(self,vertex):
		self.size = vertex
		self.matrix = [ [0 for _ in range(vertex)] for _ in range(vertex)]

	def add_edge(self, sour, dest):
		if 0 <= sour < self.size and 0 <= dest < self.size:
			self.matrix[sour][dest] = 1
			self.matrix[dest][sour] = 1
		else:
			print("Invalid Edge")

	def print_graph(self):
		
		for i in range(0,self.size):
			for j in range(0,self.size):
				print(self.matrix[i][j], end=" ")
			print("\n")


	def dfs(self, sour):
		self.stk = Stack(self.size)
		self.stk.push(sour)
		self.visited = [False for _ in range(self.size)]

		while not self.stk.is_empty():

			ele = self.stk.pop()

			if self.visited[ele] == False:
				print(ele, end=" -> ")
				self.visited[ele] = True

			for j in range(self.size): 
				if self.matrix[ele][j] == 1 and self.visited[j] == False:
					self.stk.push(j)

	def bfs(self, sour):
		self.que = CircularQueue(self.size)
		self.visited = [False for _ in range(self.size)]
		self.que.enqueue(sour)

		while not self.que.is_empty():

			ele = self.que.dequeue()

			if self.visited[ele] == False:
				print(ele, end=" -> ")
				self.visited[ele] = True

			for i in range(self.size):
				if self.matrix[ele][i] == 1 and self.visited[i] == False:
					self.que.enqueue(i)


g1=UnstructredGraph(4)
g1.add_edge(0,2)
g1.add_edge(0,1)
g1.add_edge(1,3)
g1.add_edge(2,3)

g1.print_graph()

# g1.dfs(0)
g1.bfs(0)
