import sys


def min_distance(dist, sptSet, V):
    min_index = -1
    min_dist = sys.maxint
    for v in range(V):
        if dist[v] < min_dist and not sptSet[v]:
            min_dist = dist[v]
            min_index = v

    return min_index


def dijkstra(node, graph, trusted_nodes, dist_threshold):
    num_of_vertex = len(graph)
    dist = [sys.maxint] * num_of_vertex
    dist[node] = 0
    sptSet = [False] * num_of_vertex

    for _ in range(num_of_vertex):
        u = min_distance(dist, sptSet, num_of_vertex)

        sptSet[u] = True

        for v in range(num_of_vertex):
            if graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    for every_node in trusted_nodes:
        if dist[every_node] <= dist_threshold:
            return True
    return False


def is_node_trusted(node, graph, pretrusted_peers, trust_threshold):
    return dijkstra(node, graph, pretrusted_peers, trust_threshold)


def tests():
    node = 0
    graph = [[0,2], [2,0]]
    trusted_peers = [1]
    trust_threshold = 5

    print(is_node_trusted(node, graph, trusted_peers, trust_threshold))

    node = 0
    graph = [[0,2], [2,0]]
    trusted_peers = [1]
    trust_threshold = 1

    print(is_node_trusted(node, graph, trusted_peers, trust_threshold))

    node = 0
    graph = [[0]]
    trusted_peers = [0]
    trust_threshold = 1
    print(is_node_trusted(node, graph, trusted_peers, trust_threshold))