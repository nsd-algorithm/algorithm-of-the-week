def solution(TRI):
    len_TRI = len(TRI)
    for n in range(len_TRI - 1, 0, -1):
        for m in range(n):
            TRI[n - 1][ m] += max(TRI[n][m], TRI[n][m+1])

    answer = TRI[0][0]
    return answer
