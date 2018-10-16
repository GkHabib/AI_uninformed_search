from math import sin, cos, sqrt, atan2, radians

def calc_distance(node1, node2):
	R = 6373.0
	lat1 = radians(node1.lat)
	lon1 = radians(node1.lon)
	lat2 = radians(node2.lat)
	lon2 = radians(node2.lon)
	
	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c
	return distance


def create_nodes():
	nodes_file = open('nodes.txt', 'r')
	graph = Graph()
	while True :
		try:
			line = nodes_file.readline()
			if(line == ''): raise(Exception("End of File!"))
			line = line[:-1]
			line = list(line.split(' '))
			temp_node = Node(line[0], line[1], line[2])
			graph.add_node(temp_node)

		except Exception as e:
			break;
		else:
			pass
		finally:
			pass
			
	return graph

def solution(node, start, visited_num):
	path = []
	current_node = node
	path_cost = 0
	while current_node.nodeId != start:
		path.append(current_node.nodeId)
		path_cost = path_cost + (current_node.find_neighbor(current_node.parent.nodeId)).distance
		current_node = current_node.parent
	print('visited: ', visited_num)
	print('path: ', len(path))
	print('distance: ', path_cost)
	for node in reversed(path):
		print(node, end=', ')

def connect_nodes(graph):
	edges_file = open('edges.txt', 'r')
	while True:
		try:
			line = edges_file.readline()
			if(line == ''): raise(Exception("End of File!"))
			line = line[:-1]
			line = list(line.split(' '))
			node1 = graph.find_node(line[0])
			node2 = graph.find_node(line[1])
			node1.add_neighbor(Neighbor(node2, calc_distance(node1, node2)))
			node2.add_neighbor(Neighbor(node1, calc_distance(node1, node2)))
		except Exception as e:
			break
		else:
			pass
		finally:
			pass

class Node:
	
	def __init__(self, _id='', _lat=0.0, _lon=0.0):

		self.nodeId = _id
		self.lat = float(_lat)
		self.lon = float(_lon)
		self.neighbors = []
		self.visited = False


	def __str__(self):

		return( self.nodeId + '\nlat: 	' + str(self.lat) + '\nlon: 	' + str(self.lon))

	def add_neighbor(self, _neighbor):
		self.neighbors.append(_neighbor)

	def set_parent(self, _parent):
		self.parent = _parent

	def find_neighbor(self, _id):
		for neighbor in self.neighbors:
			if neighbor.node.nodeId == _id : return neighbor

class Neighbor:

	def __init__(self, _node, _distance):
		self.node = _node
		self.distance = _distance

class Graph:
	def __init__(self):
		self.nodes = {}

	def add_node(self, node):
		self.nodes[node.nodeId] = node
	
	def size(self):
		return len(self.nodes)

	def find_node(self, _id):
		return self.nodes[_id]

