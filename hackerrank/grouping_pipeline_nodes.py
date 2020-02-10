from collections import defaultdict


def is_cycle(node, visited, rec, graph):
    visited[node] = True
    rec[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if is_cycle(neighbour, visited, rec, graph):
                return True
        elif rec[neighbour]:
            return True

    rec[node] = False

    return False


def check_route(graph, n):
    visited = [False] * (1+n)
    rec = [False] * (1+n)
    for node in xrange(1, 1+n):
        if not visited[node]:
            if is_cycle(node, visited, rec, graph):
                return False

    return True


def grouping_pipeline_nodes(n, g, v):
    if not v:
        return True

    graph = defaultdict(set)
    for src, dst in g:
        graph[src].add(dst)

    prev = v[0]
    while v:
        try:
            new = v[1]
            v.pop(0)
        except:
            return True

        # rebuild route
        w = list(graph[prev])
        del graph[prev]
        for ww in w:
            if ww != new:
                graph[new].add(ww)

        for k in graph:
            if prev in graph[k]:
                graph[k].remove(prev)
                if new != k:
                    graph[k].add(new)

        if not check_route(graph, n):
            return False

        prev = new

    return True


n = 6
g = [[1,2], [2,3], [2,4], [2,5], [4,6], [5,6]]
v = [1, 2, 4]

assert grouping_pipeline_nodes(n, g, v) is True


n = 6
g = [[1,2], [2,3], [2,4], [2,5], [4,6], [5,6]]
v = [2, 6]

assert grouping_pipeline_nodes(n, g, v) is False

n = 6
g = [[1,2], [2,3], [2,4], [2,5], [4,6], [5,6]]
v = [1, 2, 4]

assert grouping_pipeline_nodes(n, g, v) is True


n = 2
g = [[1,2]]
v = [1, 2]

assert grouping_pipeline_nodes(n, g, v) is True


n = 10
g = [[5,10], [8,2], [5,2], [4,6], [8,9], [5,2], [8,2], [8,9], [8,9], [8,5], [5,10], [2,6], [3,9], [9,10], [1,3], [8,5],
 [6,9], [4,9], [1,7]]
v = [3, 6, 8]

assert grouping_pipeline_nodes(n, g, v) is False


n = 10
g = [[8,1], [10,4], [7,9], [8,6], [3,7], [8,1], [10,4], [8,2], [3,4], [6,7], [6,9], [2,5], [8,2], [4,9]]
v = [9, 1, 5, 7, 4]
assert grouping_pipeline_nodes(n, g, v) is True
