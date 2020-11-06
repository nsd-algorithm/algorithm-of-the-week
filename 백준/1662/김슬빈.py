from collections import deque


# S = deque(list("3(3(3(2(2)2(2))))"))
S = deque(input())

def solution(S):
    answer = 0

    # 앞에 카운트
    while len(S) > 1:
        if S[1] == "(": break
        S.popleft()
        answer += 1


    while len(S) > 0:
        if S[-1] == ")": break
        S.pop()
        answer += 1




    while len(S) > 0:
        s = S.pop()
        if s == ")":
            if len(S) > 3 and S[-4] == ")": # 3(1)3(1)
                if len(S) > 0: S.pop()
                if len(S) > 0: S.pop()
                if len(S) > 0:
                    k = int(S.pop())
                    answer += k


            else:
                if len(S) >= 3:
                    k = int(S.popleft())
                    S.popleft()

                    if len(S) == 1: # 3(1
                        answer += k
                        break
                    else:
                        answer += k*solution(S)
                        break
    return answer

print(solution(S))
