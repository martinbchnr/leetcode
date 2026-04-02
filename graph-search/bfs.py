from collections import deque
from typing import Dict

def bfs_iterative(graph: Dict, start: str, target: str):
    visited = set()
    stack = deque()

    stack.append(start)
    visited.add(start)
    
    while stack:
        node = stack.popleft()
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor == target:
                return target
            if neighbor not in visited:
                stack.append(neighbor)
    
    return False

def bfs_shortest_path(graph, start, goal):
    visited = set([start])
    queue = deque([[start]])     # queue of paths, not just nodes

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path          # return the first (shortest) path found

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None  # no path found


if __name__ == "__main__":
    graph = {"a": ["b","c"], "b": ["d", "e"], "c": ["f"], "d": [], "e": ["f"], "f": []}
    print(bfs_iterative(graph, "a", "e"))
    print(bfs_shortest_path(graph, "a", "f"))