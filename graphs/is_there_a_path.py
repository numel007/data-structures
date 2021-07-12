def create_adjacency_list(locations):
    '''Returns a dictionary adjacency list of edges'''
    adjList = {}

    for line in locations:
        start = line.split(', ')[0]
        end = line.split(', ')[1].strip('\n')

        if start not in adjList:
            adjList[start] = [end]
        else:
            adjList[start].append(end)

    return adjList


def is_there_a_path(location_start, location_end, adjList):
    '''Uses a BFS to check if a path exists from locatin start to location end, returns True if a path exists, False if not'''
    queue = []
    visited = []

    queue.append(location_start)

    while len(queue) > 0:

        if queue[0] == location_end:
            return True
        else:
            visited.append(queue[0])

            if queue[0] in adjList and len(adjList[queue[0]]) > 0:
                for location in adjList[queue[0]]:
                    if location not in visited:
                        queue.append(location)
            queue.pop(0)

    return False


# ----TESTING----
with open('Transporter - traversal/locations.txt') as file:
    adjList = create_adjacency_list(file)

for key, val in adjList.items():
    print(key, val)

print()
print(is_there_a_path('Dawnstar', 'Morthal', adjList))
print(is_there_a_path('Dawnstar', 'Riften', adjList))
print(is_there_a_path('Dawnstar', 'Windhelm', adjList))
