import heapq

def heuristic():
    pass

def a_star_search(graph, start, goal):
    """
    Performs targeted A* search on a weighted graph
    
    :param graph: input graph
    :param start: starting node contained in graph
    :param goal: target node contained in graph
    """

    if start == goal:
        return 0, [start]
    
    visited = set()
    visited.add(start)

    pqueue = [(heuristic(start, goal), 0, start, [start])]

    while pqueue:
        heur_cost, graph_cost, node, path = heapq.heappop(pqueue)

        if node == goal:
            return graph_cost, path
        
        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            new_graph_cost = weight + graph_cost
            new_cost = new_graph_cost + heuristic(neighbor, goal)
            heapq.heappush(pqueue, (new_cost, new_graph_cost, neighbor, path + [neighbor]))

    
    
