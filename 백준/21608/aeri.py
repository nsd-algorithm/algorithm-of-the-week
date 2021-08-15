n = int(input())
studentList = [list(map(int, input().split())) for i in range(n*n)]
myMap = [[0] * n for i in range(n)]

move = [[-1, 0], [1, 0], [0, 1], [0, -1]]

answer = 0


def find_empty(student):
    queue = []
    for i in range(n):
        for j in range(n):
            if(myMap[i][j] == 0):
                countEmpty = 0
                countFavorite = 0
                for dir in range(4):
                    nx, ny = i + move[dir][0], j + move[dir][1]
                    if(nx >= 0 and nx < n and ny >= 0 and ny < n):
                        if(myMap[nx][ny] == 0):
                            countEmpty += 1
                        elif myMap[nx][ny] in student[1:]:
                            countFavorite += 1
                queue.append([countFavorite, countEmpty, i, j])

    queue.sort(reverse=True)
    emptyMax = queue[0][0]
    queue.sort()
    favoriteMax = 0
    for i in range(len(queue)):
        if(queue[i][0] == emptyMax):
            if(favoriteMax < queue[i][1]):
                favoriteMax = queue[i][1]
    for i in range(len(queue)):
        if(queue[i][0] == emptyMax and queue[i][1] == favoriteMax):
            myMap[queue[i][2]][queue[i][3]] = student[0]
            return


for i in range(len(studentList)):
    find_empty(studentList[i])

studentList.sort()
for i in range(n):
    for j in range(n):
        count = 0
        for dir in range(4):
            nx, ny = i+move[dir][0], j + move[dir][1]
            if(nx >= 0 and nx < n and ny >= 0 and ny < n):
                # print("studentList[myMap[i][j]-1]", studentList[myMap[i][j]-1])
                if(myMap[nx][ny] in studentList[myMap[i][j]-1][1:]):
                    count += 1
        # print("count", count)
        if(count == 4):
            answer += 1000
        elif(count == 3):
            answer += 100
        elif(count == 2):
            answer += 10
        elif(count == 1):
            answer += 1
print(answer)
