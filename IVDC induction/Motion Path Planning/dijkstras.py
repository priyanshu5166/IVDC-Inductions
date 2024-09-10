import heapq

def dijkstra(graph, start, goal):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return path[::-1]

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return None

graph = {
    (0, 0): {(0, 1): 2, (1, 0): 3},
    (0, 1): {(0, 0): 2, (0, 2): 4, (1, 1): 5},
    (0, 2): {(0, 1): 4, (1, 2): 7},
    
    (1, 0): {(0, 0): 3, (1, 1): 6, (2, 0): 2},
    (1, 1): {(0, 1): 5, (1, 0): 6, (1, 2): 1, (2, 1): 8},
    (1, 2): {(0, 2): 7, (1, 1): 1, (2, 2): 3},
    
    (2, 0): {(1, 0): 2, (2, 1): 4},
    (2, 1): {(1, 1): 8, (2, 0): 4, (2, 2): 5},
    (2, 2): {(1, 2): 3, (2, 1): 5}
}

start_node = (0, 0)
goal_node = (2, 2)
path = dijkstra(graph, start_node, goal_node)

print("Shortest path from start to goal:")
print(path)
