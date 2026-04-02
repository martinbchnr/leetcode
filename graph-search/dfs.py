from collections import deque
graph = {"a": ["b","c"], "b": ["d", "e"]}

def dfs_recursive(graph, node, target="e", visited=None):
    if visited == None:
        visited = set()
    
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor == target:
            return target
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited

def dfs_iterative(graph, start, target):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == target:
                    return target
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

