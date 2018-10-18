
from create_nodes import *

graph = create_nodes()
connect_nodes(graph)

def id(start, goal):
	visited_num = 0
	flag = True
	d = 0
	while flag :
		
		visited = []
		frontier = []
		start_node = graph.find_node(start)
		
		if(start_node.nodeId == goal):
			solution(start_node, start, visited_num)
			flag = False

		start_node.set_depth(0)
		frontier.append(start_node)
		visited_num = visited_num + 1
		visited.append(start_node)
		while frontier != []:
			node = frontier.pop()
			if(node.depth < d+1):
				for neighbor in node.neighbors:
					if(not (neighbor.node in visited)):
						
						visited_num = visited_num + 1
						neighbor.node.set_parent(node)
						if(neighbor.node.nodeId == goal):
							solution(neighbor.node, start, visited_num)
							flag = False
						# neighbor.node.visited = True
						neighbor.node.set_depth(node.depth + 1)
						frontier.append(neighbor.node)
			# if(node.nodeId == goal):
			# 	solution(node, start, visited_num)
			visited.append(node)
		d = d + 1
			


# id(str(5930756061), str(5930756084))
id(str(5930756061), str(5843293191))
