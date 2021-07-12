def top_sort_khan(adjacency_list):
    degree_list = create_dict(adjacency_list)

    s = []
    solution = []

    for location in degree_list:
        if degree_list[location] == 0:
            s.append(location)

    while len(s) > 0:
        location = s.pop()
        solution.append(location)

        for neighbor in adjacency_list[location]:
            degree_list[neighbor] -= 1
            if degree_list[neighbor] == 0:
                s.append(neighbor)

    return solution


def create_dict(adj_list):
    myDict = {}

    for location in adj_list:
        myDict[location] = 0

    for key, val in adj_list.items():
        for item in val:
            myDict[item] += 1

    return myDict


# TESTING
adjacency_list = {
    "temple of time": ["kakariko village", "death mountain"],
    "kakariko village": ["zora's domain"],
    "death mountain": ["zora's domain"],
    "zora's domain": ["castle town"],
    "castle town": ["lon lon ranch"],
    "lon lon ranch": []}
print(top_sort_khan(adjacency_list))
