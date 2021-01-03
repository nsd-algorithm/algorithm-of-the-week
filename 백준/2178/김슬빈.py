from collections import deque

height, width = list(map(int, input().split()))
matrix = [input() for _ in range(height)]

def bfs_maze(root_node, end_node, matrix):
    visit, queue = [], deque([root_node])


    while queue:
        node = queue.popleft()
        h, w = node
        if node not in visit:
            visit.append(node)
            if node == end_node: break

            if w > 0 and matrix[h][w - 1] == '1':
                queue.append([h, w - 1])
            if w < width - 1 and matrix[h][w + 1] == '1':
                queue.append([h, w + 1])

            if h > 0 and matrix[h - 1][w] == '1':
                queue.append([h - 1, w])
            if h < height - 1 and matrix[h + 1][w] == '1':
                queue.append([h + 1, w])


    answer = 1
    for n in range(1, len(visit)):
        h1, w1 = visit[n]
        h2, w2 = visit[n - 1]

        diff = abs(h1 - h2) + abs(w1 - w2)
        if diff % 2 != 0: answer += 1


    return answer

print(bfs_maze([0, 0], [height - 1, width - 1], matrix))
