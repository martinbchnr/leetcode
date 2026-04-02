import heapq
def uniform_cost_search(graph, start, goal):
    p_queue = [(0, start, [start])]
    visited = set()

    while p_queue:
        curr_cost, curr_node, curr_path = heapq.heappop(p_queue)

        if curr_node in visited:
            continue
        visited.add(curr_node)

        if curr_node == goal:
            return curr_cost, curr_path
        
        for neighbor, weight in graph[curr_node]:
            if neighbor not in visited:
                p_queue.append((curr_cost + weight, neighbor, curr_path + [neighbor]))

    return float('inf'), []

