import sys
from collections import deque

len_matrix = int(input())
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(len_matrix)]
# print(matrix)

num_paves = {'00': 0}
root_node = [0, 0]



visit, queue = [], deque([root_node])
while queue:

    node = queue.popleft()
    idx_x, idx_y = node
    idx_xy_str = ''.join(map(str, node))
    visit.append(node)
    # print(node)

    tmpx, tmpy = ''.join(map(str, [idx_y, idx_x - 1])) in num_paves, ''.join(map(str, [idx_y - 1,idx_x])) in num_paves
    if tmpx and tmpy:
        num_paves[idx_xy_str] = max(num_paves[''.join(map(str, [idx_x - 1,idx_y]))]
                                    , num_paves[''.join(map(str, [idx_x, idx_y - 1]))])
    elif tmpx:
        num_paves[idx_xy_str] = num_paves[''.join(map(str, [idx_x - 1, idx_y]))]
    elif tmpy:
        num_paves[idx_xy_str] = num_paves[''.join(map(str, [idx_x, idx_y - 1]))]

    # print(num_paves[idx_xy_str], matrix[idx_y][idx_x])
    num_paves[idx_xy_str] += matrix[idx_y][idx_x]

    if idx_x < len_matrix - 1: queue.append([idx_x + 1, idx_y])
    if idx_y < len_matrix - 1: queue.append([idx_x, idx_y + 1])

# print(num_paves)
print(num_paves[''.join(map(str, [len_matrix - 1, len_matrix - 1]))])
