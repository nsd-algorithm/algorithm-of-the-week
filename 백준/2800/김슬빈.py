from itertools import combinations
from copy import deepcopy

def string_del12(a, idx1, idx2):
    a = list(a)
    a[idx1] = " "
    a[idx2] = " "
    a = "".join(a)
    return a

def solution(mathex):
    STACK, BRACKET_IDX = [], []
    # 1. 쌍이 맞는 괄호 찾기
    for n in range(len(mathex)):
        s = mathex[n]
        if s == "(": STACK.append(n)

        if s == ")":
            idx_left, idx_right = STACK.pop(), n
            BRACKET_IDX.append([idx_left, idx_right])

    # 2. 괄호쌍 1개 ~ len(BRACKET_IDX) 개까지 적용해서 문자열 적용
    answer = []
    for n in range(1, len(BRACKET_IDX) + 1):
        COMBS =  list(combinations(BRACKET_IDX, n))
        for n in range(len(COMBS)):
            mathex_tmp = deepcopy(mathex)
            for m in range(len(COMBS[n])):
                idx1, idx2 = COMBS[n][m]
                mathex_tmp = string_del12(mathex_tmp, idx1, idx2)
            answer.append(mathex_tmp.replace(" ", ""))
    return answer



mathex = input()

answer = sorted(list(set(solution(mathex))))

for mathex in answer:
    print(mathex)
