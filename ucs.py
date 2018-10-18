
from create_nodes import *
from operator import attrgetter
from queue import PriorityQueue

graph = create_nodes()
connect_nodes(graph)

def ucs(start, goal):
	frontier = PriorityQueue()
	visited = []
	cost = 0
	visited_num = 0
	start_node = graph.find_node(start)
	if(start_node.nodeId == goal):
		solution(start_node, start, visited_num)
	start_node.set_cost(0)
	frontier.put(start_node)
	start_node.inFrontier = True
	visited_num = visited_num + 1
	while frontier:
		node = frontier.get()

		if(node.nodeId == goal):
			cost = node.cost
			solution(node, start, visited_num)
			break
		
		for neighbor in node.neighbors:
			# (neighbor.node in visited)
			if(not neighbor.node.visited):

				visited_num = visited_num + 1
				if(neighbor.node.cost == 0 or (neighbor.distance + node.cost)<neighbor.node.cost):
					neighbor.node.cost = neighbor.distance + node.cost
					neighbor.node.parent = node
				
				if(not neighbor.node.inFrontier):
					frontier.put(neighbor.node)
					neighbor.node.inFrontier = True

		node.visited = True
		# visited.append(node)
		

ucs(str(5930756061), str(5843293191))
