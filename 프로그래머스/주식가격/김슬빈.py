def solution(PRICES):
    answer = [n for n in range(len(PRICES) - 1, -1, -1)]

    idx_price = []
    for idx, price in enumerate(PRICES):
        # 1. 스택 인덱스, 가격정보 추가
        idx_price.append([idx, price])

        # 2. 가격이 올랐을 경우 -> 변화 X
        #    가격이 떨어졌을 경우 -> 변화 O
        if len(idx_price) >= 2:
            idx_gijun, price_gijun = idx_price[-1]

            if  idx_price[-2][1] > price_gijun: # 가격이 떨어졌을 때
                idx_price_t = []
                for n in range(len(idx_price) - 1):
                    idx,price = idx_price[n]
                    if price > price_gijun:
                        answer[idx] = idx_gijun - idx # 기준 가격보다 높을 경우 결과값 변경

                    else: # 기준 가격보다 낮을 경우 스택에 저장
                        idx_price_t.append([idx,price])
                idx_price_t.append([idx_gijun, price_gijun])
                idx_price = idx_price_t

    return answer
