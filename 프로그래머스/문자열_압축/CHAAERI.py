def solution(s):
    answer = len(s)
    # 최대 자를 수 있는 단위는 글자 수의 1/2까지임

    for i in range(1, len(s)//2 + 1):
        result = ""
        tmp = s[0:i]
        count = 1
        for j in range(i, len(s) + 1, i):
            # 만약 i단위 별 잘랐을 때 같은 글자들이면
            if(tmp == s[j:j+i]):
                count += 1

            else:
                # 만약 다르고 count가 1이면 글자 그대로 result에 추가
                if(count == 1):
                    result += tmp
                # 반복된 횟수 + 반복된 글자를 기존 result 글자에 추가
                else:
                    result = result + str(count) + tmp

                # tmp는 비교했던 다음 글자들로 대체
                tmp = s[j:j+i]
                # count 초기화
                count = 1
        # i개 단위로 자르고 남은 나머지 글자들을 result에 추가
        result += s[(len(s)//i)*i:]
        # 압축된 result와 answer 중에 작은 값을 answer에 갱신
        answer = min(answer, len(result))
    return answer
