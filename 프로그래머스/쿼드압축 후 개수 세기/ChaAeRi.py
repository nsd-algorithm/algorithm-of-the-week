def solution(arr):
    answer = [0, 0]

    def dps(x, y, size):
        shape = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if (arr[i][j] != shape):
                    resize = size // 2
                    dps(x, y, resize)
                    dps(x, y + resize, resize)
                    dps(x + resize, y, resize)
                    dps(x + resize, y + resize, resize)
                    return
        answer[shape] += 1
    dps(0, 0, len(arr))
    return answer
