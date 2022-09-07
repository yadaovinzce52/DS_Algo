from collections import deque

adj_list = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


# Similar to BST, if you want to print(traverse) left -> right
# You must put the right value in the stack first
def dfs(graph, start):
    stack = [start]
    while stack:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current][::-1]:
            stack.append(neighbor)


def dfs_rec(graph, current):
    print(current)
    for neighbor in graph[current]:
        dfs_rec(graph, neighbor)


def bfs(graph, start):
    queue = deque([start])
    while queue:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)


def bfs_rec(graph, current):
    pass


print('Iterative dfs using user stack')
dfs(adj_list, 'a')
print('\nRecursive dfs using call stack')
dfs_rec(adj_list, 'a')
print('\nIterative bfs using user stack')
bfs(adj_list, 'a')
print('\nRecursive bfs using call stack')
bfs_rec(adj_list, 'a')
