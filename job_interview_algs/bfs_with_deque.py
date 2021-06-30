from collections import deque


def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        # The oldest seen (but not yet visited) node will be the left most one.
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                # When we see a new node, we add it to the right side of the queue.
                q.append(neighbor)
    return distances


if __name__ == '__main__':
    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
    print(bfs(graph, 1))
    print(bfs(graph, 3))
