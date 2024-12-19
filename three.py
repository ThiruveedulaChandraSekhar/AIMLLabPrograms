from collections import deque

def dfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return []

#Graph
graph = {
    0: [3],
    1: [0, 2, 4],
    2: [7],
    3: [4, 5],
    4: [6],
    5: [6],
    6: [7],
    7: []
}

# Find the path from node 0 to node 7
path = dfs(graph, 0, 7)
print(f"Path from node 0 to node 7: {path}")
