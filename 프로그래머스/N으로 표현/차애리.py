def solution(N, number):
    answer = -1
    # i개를 이용한 조합 =>
    #i* str(N) +  N*(i-1) + (i-1)로 만든 사칙연산 조합, (i-1)로 만든 사칙연산 조합 + N*(i-1)
    # N을 i만큼 사용 +    a   +              b       또는        a               +      b
    
    DP = [] #각 i번째 계산된 값들의 집합이 중복없이 저장됨
    for i in range(1,9):
        hubo = set() # 각 i번째 조합들이 저장됨
        hubo.add(int(str(N)*i)) # N을 i만큼 사용
        
        for j in range(0,i-1):
            for x in DP[j]: #(i-1)로 만든 조합
                for y in DP[-j-1]:#(i-1)로 만든 조합(뒤에서)
                    hubo.add(x+y)
                    hubo.add(x-y)
                    hubo.add(x*y)
                    
                    if(y !=0):
                        hubo.add(x//y)      
        
        if ( number in hubo):
            answer = i
            break
        DP.append(hubo) # 동적계획법 Memorization 사용
        
    
    
    return answer
