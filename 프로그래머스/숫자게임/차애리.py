def solution(A, B):
    A.sort()
    B.sort()
    idxA = 0
    idxB = 0
    answer = 0
    while(1):
        if A[idxA] < B[idxB] :
            answer+=1
            idxA+=1
            idxB+=1
        else:
            idxB +=1
        if idxA == len(A) or idxB == len(B) :
            break

    return answer
