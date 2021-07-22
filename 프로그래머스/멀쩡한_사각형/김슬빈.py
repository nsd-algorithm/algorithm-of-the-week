import math
def solution(width, height):
    width, height = [width, height] if width < height else [height, width]
    gcd = math.gcd(width, height)
    gcd_w, gcd_h = width // gcd, height // gcd

    gradient = height / width
    if width == height:
        answer = width * height - width 
    else:
        y_prev = 0
        answer = 0
        for w in range(1, gcd_w + 1):
            y_now = gradient * w
            if w % gcd_w == 0:
                y_now = gcd_h 
                # print('good', y_now, y_prev)
                answer += y_now - y_prev
            else:
                y_now = int(y_now)
                answer += y_now - y_prev + 1
                
            y_prev = y_now
            # print(w, answer)
            
        answer *= gcd

        answer = width * height - answer

    return answer
