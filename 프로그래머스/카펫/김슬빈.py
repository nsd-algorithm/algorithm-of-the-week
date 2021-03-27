def solution(brown, yellow):
    def get_divisor(n):
        n = int(n)
        divisors = []
        divisors_back = []

        for i in range(1, int(n ** (1 / 2)) + 1):
            if (n % i == 0):
                divisors.append(i)
                if (i != (n // i)):
                    divisors_back.append(n // i)

        return divisors + divisors_back[::-1]

    # 1. Yellow의 약수 구하기
    YD = get_divisor(yellow)

    # 2. 이진 탐색으로 width, height 구하기
    left_idx, right_idx = 0, len(YD) - 1
    mid_idx = (left_idx + right_idx) // 2
    width, height = YD[mid_idx] + 2, (yellow // YD[mid_idx]) + 2
    brown_tmp = width * height - (width -2) * (height - 2)
    while brown_tmp != brown:
        if brown_tmp < brown: right_idx = mid_idx
        else: left_idx = mid_idx
        mid_idx = (left_idx + right_idx) // 2
        width, height = YD[mid_idx] + 2, (yellow // YD[mid_idx]) + 2
        brown_tmp = width * height - (width - 2) * (height - 2)

    if width < height: width, height = height, width # height가 더 클 경우 width와 height를 바꾸어 줌

    answer = [width, height]
    return answer
