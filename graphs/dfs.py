graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
stack = []


def dfs(graph, start):

    # Add start node to stack and visited
    stack.append(start)
    visited.append(start)

    # If stack has children
    if len(graph[start]) >= 1:

        for child in graph[start]:
            # If child hasn't already been visited, then visit it
            if child not in visited:
                dfs(graph, child)
    else:
        # If there are no children, pop from the stack and try the parent's next child
        stack.pop()
        return visited

    return visited


print(dfs(graph, 'A'))
