

def countIsland(w, h, map):
    move = [[-1, 0], [1, 0], [0, -1], [0, 1],
            [1, 1], [-1, -1], [-1, 1], [1, -1]]
    visited = [[0]*w for i in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            queue = []
            if(map[i][j] == 1 and visited[i][j] == 0):
                queue.append([i, j])

                while(queue):

                    tmp = queue.pop()
                    y, x = tmp[0], tmp[1]
                    visited[y][x] = 1
                    for dir in range(8):
                        ny, nx = y + move[dir][0], x + move[dir][1]
                        if(nx >= 0 and nx < w and ny >= 0 and ny < h):
                            if(visited[ny][nx] == 0 and map[ny][nx] == 1):
                                visited[ny][nx] == 1
                                queue.append([ny, nx])
                answer += 1
    return answer


while(1):
    w, h = map(int, input().split())
    myMap = [list(map(int, input().split())) for i in range(h)]
    if(w == 0 and h == 0):
        break

    else:

        result = countIsland(w, h, myMap)

        print(result)
