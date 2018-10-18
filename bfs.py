
from create_nodes import *

graph = create_nodes()
connect_nodes(graph)

def bfs(start, goal):
	frontier = []
	path_cost = 0
	visited_num = 0
	start_node = graph.find_node(start)
	if(start_node.nodeId == goal):
		solution(start_node, start, visited_num)

	frontier.append(start_node)
	visited_num = visited_num + 1
	for node in frontier:
		
		for neighbor in node.neighbors:
			
			if(not neighbor.node.visited):
				visited_num = visited_num + 1
				neighbor.node.set_parent(node)
				if(neighbor.node.nodeId == goal):
					solution(neighbor.node, start, visited_num)
				neighbor.node.visited = True
				frontier.append(neighbor.node)

# bfs(str(5930756061), str(5930756084))
bfs(str(5930756061), str(5843293191))
