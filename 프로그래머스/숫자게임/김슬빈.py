def solution(A, B):
    A, B = sorted(A), sorted(B)

    length = len(A)
    answer = 0
    # 0. 전체 비교

    if B[0] > A[-1]: return length  # B 전체가 A보다 클 경우
    if A[0] >= B[-1]: return 0  # A 전체가 B보다 크거나 같을 경우

    # 1. 한칸씩 이동하며 반복
    answer = 0
    idx_a = 0
    for n in range(length):
        if A[idx_a] < B[n]:
            answer += 1
            idx_a += 1

    return answer
