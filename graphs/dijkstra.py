import math


def build_shortest_path(graph, start):
    table = {}

    for vertex in graph:
        if vertex == start:
            table[vertex] = [0, ""]
        else:
            table[vertex] = [math.inf, ""]

    visited = []
    unvisited = [key for key in table]
    current = start
    neighbors = graph[current]

    while len(unvisited) > 0:
        for neighbor in neighbors:

            if neighbor[0] not in visited:
                distance = neighbor[1]
                total_distance = table[current][0] + distance

                if total_distance < table[neighbor[0]][0]:
                    table[neighbor[0]][0] = total_distance
                    table[neighbor[0]][1] = current

        visited.append(current)
        unvisited.remove(current)

        min_distance = math.inf
        for vertex in unvisited:
            if table[vertex][0] < min_distance and table[vertex][0] != 0:
                min_distance = table[vertex][0]

        for vertex in table:
            if table[vertex][0] == min_distance:
                current = vertex

        neighbors = graph[current]

    return table


def get_shortest_path(table, start, end):
    # return the shortest path given the table
    path = []
    current = end

    while table[current][0] != 0:
        path.append(current)
        current = table[current][1]

    path.append(start)
    path.reverse()

    return path


example_graph = {
    "Port Sarim": [("Darkmeyer", 10), ("Al Kharid", 4)],
    "Darkmeyer": [("Port Sarim", 10), ("Al Kharid", 4), ("Varrock", 3), ("Nardah", 2)],
    "Al Kharid": [("Port Sarim", 4), ("Darkmeyer", 4), ("Varrock", 2)],
    "Varrock": [("Al Kharid", 2), ("Darkmeyer", 3), ("Nardah", 3)],
    "Nardah": [("Varrock", 3), ("Darkmeyer", 2)]
}

table = build_shortest_path(example_graph, "Port Sarim")
print(get_shortest_path(table, "Port Sarim", "Nardah"))
