import numpy as np

class MODEL:
	def __init__(self, name):
		if name == "cube":
			self.name = name
			self.vertices = np.array([[1,1,1], [-1,1,1], [1,-1,1],[-1,-1,1],
									[1,1,-1], [-1,1,-1], [1,-1,-1], [-1,-1,-1]])
			self.edges = np.zeros((8,8))
			for i in range(8):
				for j in range(i+1, 8):
					diff = np.sum(self.vertices[i] == self.vertices[j])
					if diff == 2:
						self.edges[i,j] = 1
						self.edges[j,i] = 1

		elif name == "pyramid" or "tetrahedron":
			self.name = name
			self.vertices = np.array([[1,1,1], [1,-1,-1], [-1,1,-1], [-1,-1,1]])
			self.edges = np.zeros((4,4))
			for i in range(4):
				for j in range(i+1, 4):
					self.edges[i,j] = 1
					self.edges[j,i] = 1

		elif name == "octahedron":
			self.name = name
			self.vertices = np.array([[0,0,1],[1,0,0],[0,1,0],[-1,0,0],[0,-1,0], [0,0,-1]])
			self.edges = np.zeros((6,6))
			for i in range(6):
				for j in range(i+1, 6):
					diff = np.sum(self.vertices[i] == self.vertices[j])
					if diff == 1:
						self.edges[i,j], self[j,i] = 1,1


	def rotate(self, theta_x,theta_y,theta_z):
		Rx=np.array([[1,0,0],
			[0,np.cos(np.radians(theta_x)),-np.sin(np.radians(theta_x))],
			[0,np.sin(np.radians(theta_x)),np.cos(np.radians(theta_x))]])

		Ry=np.array([[np.cos(np.radians(theta_y)),0,np.sin(np.radians(theta_y))],
			[0,1,0],
			[-np.sin(np.radians(theta_y)),0,np.cos(np.radians(theta_y))]])

		Rz=np.array([[np.cos(np.radians(theta_z)),-np.sin(np.radians(theta_z)),0],
			[np.sin(np.radians(theta_z)),np.cos(np.radians(theta_z)),0],
			[0,0,1]])
		self.vertices  = self.vertices @ (Rx @ Ry @ Rz)

	def project2axis(self, axis= "z"):
		P = np.eye(3)
		i = {"x":0, "y":1, "z":2}[axis]
		P[i,i] = 0
		Projvert = self.vertices @ P.T
		cols = [c for c in range(3) if c!= {"x": 0, "y":1, "z":2}[axis]]
		return cols, Projvert





