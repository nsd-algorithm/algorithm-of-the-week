def solution(n):
    answer = 1
    # 1부터 n/2까지 더하기 시작하는 수 for문으로 돌리기
    # n/2까지만 하는 이유는 n/2 + (n/2) + 1 이 되는 순간 무조건 n보다 크기 때문에 그 이후 부터는 할 의미가 없음
    for i in range(1, int(n/2) + 1):

        tmp = 0
        # i부터 차례로 더함. 더하면서 n이 되면 멈추고 answer를 증가 시키고, 커지면 break
        for j in range(i, n):
            tmp += j
            if(tmp > n):
                break
            if(tmp == n):
                answer += 1
                break
    return answer
