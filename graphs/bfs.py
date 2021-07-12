graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

to_visit = []


def bfs(graph, start):
    if len(to_visit) <= 0:
        to_visit.append(start)

    while len(to_visit) > 0:
        if len(graph[start]) > 0:
            for neighbor in graph[to_visit[0]]:
                if neighbor not in to_visit:
                    to_visit.append(neighbor)

        print(f'Visited {to_visit[0]}')
        to_visit.pop(0)
        for item in to_visit:
            bfs(graph, item)
    return


bfs(graph, 'A')
