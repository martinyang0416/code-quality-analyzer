import heapq

def dijkstra(graph, start, num_nodes):
    dist = [float('inf')] * (num_nodes + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    visited = [False] * (num_nodes + 1)
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for (v, w) in graph[u]:
            if dist[v] > current_dist + w:
                dist[v] = current_dist + w
                heapq.heappush(heap, 